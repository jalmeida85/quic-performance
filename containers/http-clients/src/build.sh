#!/bin/bash

ROOT=${PWD}

cd http-asio
cmake . && make

cd ${ROOT}
cd http-curl
cmake . && make

cd ${ROOT}
cd http-okhttp
gradle build

cd ${ROOT}
cp http-asio/http-asio /quic
cp http-curl/http-curl /quic
cp http-okhttp/build/libs/http-okhttp.jar /quic