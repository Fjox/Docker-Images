# rust-ws2tcp-gateway

### Repos used:
https://github.com/bouroo/rs-wsProxy

### Enviroment Variables
see https://github.com/bouroo/rs-wsProxy#configuration

### Build args explantation:
VERSION= what branch/tag to use when pulling rs-wsProxy from repo. Default=main\
DEBIAN_VERSION= What rust docker image to pull, NOTE: Only use debian images. Default=bookworm

### Build command example:
```
docker build -t git.fjox.win/fjox/rust-ws2tcp-gateway:1.1.1 --build-arg VERSION=v1.1.1 --build-arg DEBIAN_VERSION=trixie-slim --no-cache .
```