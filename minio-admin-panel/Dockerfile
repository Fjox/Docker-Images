# Start from an Debian image with the latest version of Go installed
FROM golang:bookworm as build-env

LABEL maintainer="info@fjox.win"
# Install git
RUN apt update && apt install -y git make

# Build minio-admin-panel
RUN git clone https://git.fjox.win/mirror/minio-admin-panel && mv -v minio-admin-panel /temp && cd /temp && go mod download && CGO_ENABLED=0 GOOS=linux go build -a -o minio-admin-panel . && mkdir /app && mv /temp/minio-admin-panel /app/minio-admin-panel && mv /temp/translations /app/translations && mv /temp/web /app/web && cd /app && touch FJOX.WIN

# Distributed image
FROM debian:12
RUN apt update && apt install curl -y

# Copy compiled minio-admin-panel into working directory
WORKDIR /app
COPY --from=build-env /app /app

# Run the app by default when the container starts
CMD ["/app/minio-admin-panel"]
