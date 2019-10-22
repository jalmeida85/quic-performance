FROM ubuntu:18.04

# System dependencies

# dev stuff

RUN apt-get update &&  apt-get install -y \
    software-properties-common  \
    build-essential             \
    sudo                        \
    git                         \
    xutils-dev                  \
    g++                         \
    cmake                       \
    make                        \
    curl                        \
    python3-dev                 \
    python3-pip                 \
    pkg-config                  \
    autoconf                    \
    autotools-dev               \
    automake                    \
    libtool                     \
    zlib1g-dev                  \
    binutils-dev

# network stuff

RUN apt-get update &&  apt-get install -y \
    net-tools       \
    iproute2        \
    iputils-ping    \
    iptables        \
    iperf3

# scripting stuff

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install requests urllib3

RUN apt-get update &&  apt-get install -y \
    faketime \
    libscope-guard-perl \
    libtest-tcp-perl \
    libssl-dev

WORKDIR /quic

# Quic picoquic github projects

RUN mkdir -p picoquic
RUN cd picoquic \
    && git clone -b quic-demos https://github.com/jalmeida85/picotls.git \
    && git clone -b quic-demos https://github.com/jalmeida85/picoquic.git

# Docker sudo abilities

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

# Build

RUN cd picoquic/picotls \
    && sudo git submodule init \
    && sudo git submodule update \
    && sudo cmake . \
    && sudo make \
    && sudo make check \
    && cd ../picoquic \
    && sudo cmake . \
    && sudo make

COPY certificate.pem .
COPY key.pem .