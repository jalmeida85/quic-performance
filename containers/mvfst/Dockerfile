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

#mvfst specific stuff

RUN apt-get update &&  apt-get install -y \
    libboost-all-dev         \
    libevent-dev             \
    libdouble-conversion-dev \
    libgoogle-glog-dev       \
    libgflags-dev            \
    libiberty-dev            \
    liblz4-dev               \
    liblzma-dev              \
    libsnappy-dev            \
    libjemalloc-dev          \
    libssl-dev               \
    libsodium-dev

WORKDIR /quic

COPY certificate.pem .
COPY key.pem .

RUN mkdir -p mvfst
RUN cd mvfst \
    && git clone -b quic-demos https://github.com/jalmeida85/proxygen.git

# Docker sudo abilities

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

# Build

RUN cd mvfst/proxygen/proxygen \
    && sudo ./build.sh -j 1 --with-quic