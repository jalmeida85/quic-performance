FROM ubuntu

WORKDIR /quic

RUN apt-get update &&  apt-get install -y \
    software-properties-common \
    net-tools \
    iproute2 \
    iputils-ping \
    build-essential \
    iptables \
    git \
    sudo \
    wget \
    curl \
    python3 \
    iperf3 \
    python3-dev \
    python3-pip

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install requests urllib3

COPY certificate.pem .
COPY key.pem .
COPY OoklaServer-linux64.tgz .
COPY OoklaServer.properties .
COPY install_server.sh .

RUN cp OoklaServer.properties OoklaServer.properties.default
RUN chmod a+x install_server.sh
RUN ./install_server.sh install -f

EXPOSE 8080
EXPOSE 5060