#!/bin/bash

apt update && apt upgrade

apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

apt update && apt upgrade

apt install -y python3 zlib1g-dev npm docker python-pip cmake docker-ce docker-ce-cli containerd.io

# python requests
pip install requests

# docker-compose
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# googletest
git clone https://github.com/google/googletest.git
cd googletest/
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON -DBUILD_GMOCK=ON -DINSTALL_GTEST=ON ../
make
make install