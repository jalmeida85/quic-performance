import requests
import subprocess
import sys
import json
import time

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
        port = data['http_port']
        req_bytes = data['requests']['files']
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

            file_url = 'https://' + server_name + ':' + str(port) + '/speedtest/' + b
            url = 'http://' + server_ip + ':8888/config/'
            payload = {"INTERFACE": 'eth0', "OUTGOING": {"LATENCY": float(l), "PACKET_LOSS": float(p)},
                       "INCOMING": {"LATENCY": float(l), "PACKET_LOSS": float(p)}}
            r = requests.post(url, json=payload)
            if (r.status_code != 200):
                continue

            for i in range(0, nruns):

                try:
                    start = int(round(time.time() * 1000))
                    cmd = ["sudo", "java", "-jar", "http-okhttp.jar", server_name, '/speedtest/' + b, str(port)]
                    return_code = subprocess.call(cmd, timeout=300)
                    start = int(subprocess.getoutput('cat out | head -n 10 | grep Start | awk \'{ print $2}\''))
                    stop = int(subprocess.getoutput('cat out | head -n 10 | grep Stop | awk \'{ print $2}\''))
                    rate = float(subprocess.getoutput('cat out | head -n 10 | grep Rate | awk \'{ print $2}\''))
                    size = int(subprocess.getoutput('cat out | head -n 10 | grep ength | awk \'{ print $2}\''))
                    print("benchmark\tokhttp\t0\t" + str(l) + "\t" + str(p) + "\t" + str(start) + "\t" + str(
                        stop) + "\t" + str(size) + "\t\t" + "{:.2f}".format(rate))
                except Exception as e:
                    print(e)
                    return_code = -1
                    print("Exception in process call...")
