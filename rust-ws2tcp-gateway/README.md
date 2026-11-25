# rust-ws2tcp-gateway

### Repos used:
https://github.com/bouroo/rs-wsProxy

### Enviroment Variables

| Description | Default | Environment Variable |
|-------------|---------|---------------------|
| Port to bind | `5999` | `WSPROXY_PORT` |
| Tokio worker threads | `1` | `WSPROXY_THREADS` |
| Enable TLS | `false` | `WSPROXY_SSL` |
| SSL private key path | `./default.key` | `WSPROXY_KEY` |
| SSL certificate path | `./default.crt` | `WSPROXY_CERT` |
| Comma-separated allowed targets (`ip:port`) | empty (open proxy) | `WSPROXY_ALLOW` |
| Comma-separated redirects (`source=target`) | empty | `WSPROXY_REDIRECT` |
| Default target for RebuildClient `/ws` route | empty | `WSPROXY_DEFAULT_TARGET` |

### Build args explantation:
VERSION= what branch/tag to use when pulling rs-wsProxy from repo. Default=main\
DEBIAN_VERSION= What rust docker image to pull, NOTE: Only use debian images. Default=bookworm

### Build command example:
```
docker build -t git.fjox.win/fjox/rust-ws2tcp-gateway:1.1.1 --build-arg VERSION=v1.1.1 --build-arg DEBIAN_VERSION=trixie --no-cache .
```