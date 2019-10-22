import requests
import subprocess
import sys
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) != 2:
    print("Wrong arguments.\nusage: python run_demo.py <config_file>")
    sys.exit(-1)

with open(sys.argv[1]) as json_file:
    try:
        data = json.load(json_file)
        server_ip = data['server_ip']
        server_name = data['server_name']
        port = data['mvfst_port']
        req_bytes = data['requests']['bytes']
        latency = data['latency']
        loss_percentage = data['loss_percentage']
        iface = data["iface"]
        nruns = data['nruns']
    except:
        print("Could not parse config file...")
        sys.exit(-1)

for p in loss_percentage:
    for l in latency:
        for b in req_bytes:

            #####################################################
            ################ APPLY NETWORK RULES ################
            #####################################################

            file_url = 'https://' + server_name + ':8443/speedtest/' + b
            url = 'http://' + server_ip + ':8888/config/'
            payload = {"INTERFACE": 'eth0', "OUTGOING": {"LATENCY": float(l), "PACKET_LOSS": float(p)},
                       "INCOMING": {"LATENCY": float(l), "PACKET_LOSS": float(p)}}
            r = requests.post(url, json=payload)
            if (r.status_code != 200):
                continue

            #####################################################
            ################ REMOVE SESSION FILES ###############
            #####################################################

            try:
                cmd = ["sudo", "rm", "-rf", "mvfst_psk"]
                return_code = subprocess.call(cmd, timeout=300)
                cmd = ["sudo", "rm", "-rf", "mvfst_psk"]
                return_code = subprocess.call(cmd, timeout=300)
            except:
                print("Unable to delete session files...")

            #####################################################
            ################## PERFORM TEST #####################
            #####################################################

            for i in range(0, nruns):

                try:
                    cmd = ["sudo", "./mvfst/proxygen/proxygen/_build/proxygen/httpserver/hq", "-lat=" + str(l),
                           "-plr=" + str(p), "-bytes=" + str(b), "-mode=client", "-host=" + str(server_ip),
                           "-port=" + str(port), "-congestion=newreno", "-path=/" + str(b), "-v", "1",
                           "-early_data=true", "-psk_file=mvfst_psk", "-logdir=./"]

                    return_code = subprocess.call(cmd, timeout=300)
                except Exception as e:
                    print(e)
                    return_code = -1
                    print("Exception in process call...")

            #####################################################
            ################ REMOVE SESSION FILES ###############
            #####################################################

            try:
                cmd = ["sudo", "rm", "-rf", "mvfst_psk"]
                return_code = subprocess.call(cmd, timeout=300)
                cmd = ["sudo", "rm", "-rf", "mvfst_psk"]
                return_code = subprocess.call(cmd, timeout=300)
            except:
                print("Unable to delete session files...")
