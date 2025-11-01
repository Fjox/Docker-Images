# Mitra

### Repos used:
https://git.fjox.win/Mirror/mitra \
https://git.fjox.win/Mirror/mitra-web 

Use the config in this repo as example instead of the one in mitra [config.yaml](./config.yaml)

### Build args explantation:
MITRA_VERSION= what branch/tag to use when pulling mitra from repo. Default=main\
NODE_VERSION= What version of node to get to compile mitra-web. Default=20\
DEBIAN_VERSION= What rust docker image to pull, NOTE: Only use debian images. Default=bookworm

### Build command example:
```
docker build -t git.fjox.win/fjox/mitra:4.12.0 --build-arg MITRA_VERSION=v4.12.0 --build-arg NODE_VERSION=24 --build-arg DEBIAN_VERSION=bookworm --no-cache .
```

### media-storage-s3

Dockerfile for that branch can be found at [Dockerfile_S3](./Dockerfile_S3)\