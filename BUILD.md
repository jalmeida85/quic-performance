## Building the quic-performance project

1. Clone the quic-performance project
2. Install system dependencies
3. Install the network emulator
4. Setup certificates
5. Setup configuration files

### Clone the quic-performance project (client and server)

To clone the quic-performance project just run the following commands:

~~~~~
git clone https://github.com/jalmeida85/quic-performance.git
cd quic-performance
git submodule update --init --recursive
export QUIC_PERF=$(pwd)
~~~~~
### Install system dependencies (client and server)

The project depends on the following packages/libraries:

 * zlib 
 * npm
 * docker and docker-ce
 * python-pip and package requests
 * cmake 
 * googletest

To install all dependencies you can use the script `setup.sh`.

**If you don't want to install some of the dependencies, you should 
install them without the script** 

~~~~~
cd ${QUIC_PERF}/scripts
chmod +x setup.sh
./setup.sh
~~~~~

### Install network emulator (server only)

To install the network emulator run the following commands:

~~~~~
cd ${QUIC_PERF}/network-emulator
cmake . && make && make install
mkdir -p rest_api/emulator
cp -R build/include/ build/lib/ rest_api/emulator/
cd rest_api
npm install
npm run build
~~~~~

### Setup certificates (client and server)

If your machine does not have certificates you can generate them using certbot.

~~~~~
sudo add-apt-repository -y ppa:certbot/certbot
apt update
apt install -y certbot

sudo certbot certonly --standalone --preferred-challenges http --register-unsafely-without-email --agree-tos -d <server_name>
~~~~~

By default, certbot places the certificates in `/etc/letsencrypt/live/<server_name>/`

You'll need to copy the certificates to the folder `config/certs`

If you already have certificates in place for your machine just copy them to `config/certs`.

The private key should be named `key.pem` and the certificate `certificate.pem`

For instance, for keys generated through certbot you would have to run the following command:
~~~~~
mkdir -p ${QUIC_PERF}/config/certs/

cp /etc/letsencrypt/live/<server_name>/privkey.pem ${QUIC_PERF}/config/certs/key.pem
cp /etc/letsencrypt/live/<server_name>/fullchain.pem ${QUIC_PERF}/config/certs/certificate.pem
~~~~~

Then use the following commands to copy the certificates to the container folders:

~~~~~
cp ${QUIC_PERF}/config/certs/key.pem ${QUIC_PERF}/containers/ookla-server/key.pem
cp ${QUIC_PERF}/config/certs/key.pem ${QUIC_PERF}/containers/http-clients/key.pem
cp ${QUIC_PERF}/config/certs/key.pem ${QUIC_PERF}/containers/mvfst/key.pem
cp ${QUIC_PERF}/config/certs/key.pem ${QUIC_PERF}/containers/ngtcp2/key.pem
cp ${QUIC_PERF}/config/certs/key.pem ${QUIC_PERF}/containers/picoquic/key.pem

cp ${QUIC_PERF}/config/certs/certificate.pem ${QUIC_PERF}/containers/ookla-server/certificate.pem
cp ${QUIC_PERF}/config/certs/certificate.pem ${QUIC_PERF}/containers/http-clients/certificate.pem
cp ${QUIC_PERF}/config/certs/certificate.pem ${QUIC_PERF}/containers/mvfst/certificate.pem
cp ${QUIC_PERF}/config/certs/certificate.pem ${QUIC_PERF}/containers/ngtcp2/certificate.pem
cp ${QUIC_PERF}/config/certs/certificate.pem ${QUIC_PERF}/containers/picoquic/certificate.pem
~~~~~

### Setup docker .env file (server only)

In `${QUIC_PERF}/config/.env` you have a docker configuration file, 
where you should configure both your server IP and the ports
to be used for each of the QUIC implementations.

Change them to reflect you server IP and the ports you want to use. Then copy them 
to the folders that will be orchestrating the servers:

~~~~~
cp ${QUIC_PERF}/config/.env ${QUIC_PERF}/performance/servers/quic/mvfst/
cp ${QUIC_PERF}/config/.env ${QUIC_PERF}/performance/servers/quic/ngtcp2/
cp ${QUIC_PERF}/config/.env ${QUIC_PERF}/performance/servers/quic/picoquic/
~~~~~

### Setup config.json file (client only)

In `${QUIC_PERF}/config/config.json` you have a configuration file, 
where you can configure both your server IP and server name, interface upon which network 
rules will be applied and the ports to be used for each of the QUIC implementations.

**Be sure that these match the configurations you setup in the server side**

You can also configure the test itself, including latency ranges, packet loss ranges
and files to be tested.

### Running QUIC benchmark tests

First you need to start the **network emulator**. To do this, use the following commands:

~~~~~
cd ${QUIC_PERF}/network-emulator/rest_api
npm start
~~~~~

Then you need to start the server side. The docker-compose orchestrating 
the server side is located in `${QUIC_PERF}/performance/servers/quic/<quic_implementation>`.

To run the **server** just go to the quic implementation you want and run 

~~~~~
docker-compose up --build
~~~~~

Finally, you should start the client. The docker-compose orchestrating the client side is 
located in `${QUIC_PERF}/performance/clients/quic/<quic_implementation>`.

To run the **client** just go to the quic implementation you want and run

~~~~~
docker-compose up --build
~~~~~


### Running HTTP benchmark tests

First you need to start the **network emulator**. To do this, use the following commands:

~~~~~
cd ${QUIC_PERF}/network-emulator/rest_api
npm start
~~~~~

Then you need to start the server side. The docker-compose orchestrating 
the server side is located in `${QUIC_PERF}/performance/servers/http/ookla`.

To run the **server** just go to the folder and run 

~~~~~
docker-compose up --build
~~~~~

Finally, you should start the client. The docker-compose orchestrating the client side is 
located in `${QUIC_PERF}/performance/clients/http/<http_implementation>`.

To run the **client** just go to the http implementation you want and run

~~~~~
docker-compose up --build
~~~~~