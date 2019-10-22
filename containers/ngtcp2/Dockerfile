FROM ubuntu:18.04

# System dependencies

# dev stuff

RUN apt-get update && apt-get install -y \
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

RUN apt-get update && apt-get install -y \
    net-tools       \
    iproute2        \
    iputils-ping    \
    iptables        \
    iperf3

# ngtcp stuff

RUN apt-get update && apt-get install -y \
    libcunit1-dev \
    libev-dev

# scripting stuff

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install requests urllib3

WORKDIR /quic

COPY certificate.pem .
COPY key.pem .

# Quic ngtcp2 github projects

RUN mkdir -p ngtcp2
RUN cd ngtcp2 \
    && git clone -b quic-demos https://github.com/jalmeida85/openssl.git \
    && git clone -b quic-demos https://github.com/jalmeida85/nghttp3.git \
    && git clone -b quic-demos https://github.com/jalmeida85/ngtcp2.git

# Docker sudo abilities

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

# Build

RUN cd ngtcp2/openssl \
    && sudo ./config enable-tls1_3 --prefix=$PWD/build \
    && sudo make \
    && sudo make install_sw \
    && cd ../nghttp3 \
    && sudo autoreconf -i \
    && sudo ./configure --prefix=$PWD/build --enable-lib-only \
    && sudo make \
    && sudo make install \
    && cd ../ngtcp2 \
    && sudo autoreconf -i \
    && sudo ./configure PKG_CONFIG_PATH=$PWD/../openssl/build/lib/pkgconfig:$PWD/../nghttp3/build/lib/pkgconfig LDFLAGS="-Wl,-rpath,$PWD/../openssl/build/lib" \
    && sudo make check