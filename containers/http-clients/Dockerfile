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
    binutils-dev                \
    openjdk-11-jdk              \
    wget                        \
    gradle

RUN apt-get update &&  apt-get install -y \
    libssl-dev              \
    libcurl4-openssl-dev

RUN wget https://dl.bintray.com/boostorg/release/1.71.0/source/boost_1_71_0.tar.bz2 \
    && tar --bzip2 -xf boost_1_71_0.tar.bz2 \
    && cd boost_1_71_0/ \
    && ./bootstrap.sh --with-libraries=system \
    && ./b2 install

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

WORKDIR /quic

COPY certificate.pem .
COPY key.pem .

RUN mkdir -p http-clients

COPY src/ /quic/http-clients/

# Docker sudo abilities

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

# Build

RUN cd http-clients/ \
    && sudo chmod +x build.sh \
    && sudo ./build.sh