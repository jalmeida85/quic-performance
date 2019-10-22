# Container Content Server - Speedtest

This is a Docker container with a content server from `speedtest.net`. This image creates a speedtest server binded with port 8080 (please make sure the port is available).

- [Requirements](#requirements)
- [Usage](#usage)
    - [HTTPS](#https)
    - [Install](#install)
    - [Requests](#requests)
      - [GET](#get)
      - [POST](#post)
- [Disclaimer](#disclaimer)
- [License](#license)

## Requirements

- Docker Engine

## Usage

Following we described how you can use the server.

### HTTPS

The server is running HTTPS with a self signed certificate and respective key, that is provided (`certificate.pem` and `key.pem`) for testing purposes.

If you want to use a different certificate and key, you can replace the ones we provide before the [install](#install) process. If yours certificate and key has a different name then the ones we provide, don't forget to change the names in the `Dockerfile`:

```bash
COPY <your_certificate_name.pem> .
COPY <your_key_name.pem> .
```

and in the `OoklaServer.properties` file:

```bash
# To use a custom certificate, create a certificate and private key and set the path to them here:
# (Note, this will disable Let's Encrypt certificate generation)
openSSL.server.certificateFile = <your_certificate_name.pem>
openSSL.server.privateKeyFile = <your_key_name.pem>
```

### Install

To create and run the container you use the following command:

```sh
$ docker build -t codavel .
```

```sh
$ docker run -dit --restart always --name cvl-speedtest -d -p 8080:8080 codavel
```

To check the status of the image:
```sh
$ docker ps
```

### Requests

These are the available request methods in the server:

#### GET

List of available files:
- **10B file** (used to test latency)
    - http://localhost:8080/speedtest/latency.txt
    - Size: 10 B

- **245KB file**
    - http://localhost:8080/speedtest/random350x350.jpg
    - Size: 245388 B

- **505KB file**
    - http://localhost:8080/speedtest/random500x500.jpg
    - Size: 505544 B

- **1.1MB file**
    - http://localhost:8080/speedtest/random750x750.jpg
    - Size: 1118012 B

- **1.9MB file**
    - http://localhost:8080/speedtest/random1000x1000.jpg
    - Size: 1986284 B

- **4.4MB file**
    - http://localhost:8080/speedtest/random1500x1500.jpg
    - Size: 4468241 B

- **7.9MB file**
    - http://localhost:8080/speedtest/random2000x2000.jpg
    - Size: 7907740 B

- **12.4MB file**
    - http://localhost:8080/speedtest/random2500x2500.jpg
    - Size: 12407926 B

- **17.8MB file**
    - http://localhost:8080/speedtest/random3000x3000.jpg
    - Size: 17816816 B

- **24.2MB file**
    - http://localhost:8080/speedtest/random3500x3500.jpg
    - Size: 24262167 B

- **31.6MB file**
    - http://localhost:8080/speedtest/random4000x4000.jpg
    - Size: 31625365 B

- **49.4MB file**
    - http://localhost:8080/speedtest/random5000x5000.jpg
    - Size: 49454450 B

- **71.1MB file**
    - http://localhost:8080/speedtest/random6000x6000.jpg
    - Size: 71154024 B  

- **96.9MB file**
    - http://localhost:8080/speedtest/random7000x7000.jpg
    - Size: 96912152 B


#### POST

> http://localhost:8080/speedtest/upload.php

Posting data to the server. The body response gives the size of the uploaded file.

## Disclaimer

This docker image is a similar version than the one made available by [NextHop](https://github.com/nexthopsolutions/docker-speedtest/blob/master/Dockerfile).

## License

Copyright © 2019 Codavel

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at:

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 