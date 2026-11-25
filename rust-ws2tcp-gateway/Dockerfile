#add build args
ARG DEBIAN_VERSION="bookworm"

# Start from an Debian image with the latest version of Rust installed
FROM rust:${DEBIAN_VERSION} as build-env

#args
ARG VERSION="main"
#add build env
ENV VERSION="${VERSION}"

LABEL maintainer="info@fjox.win"
# Install git
RUN apt update && apt install -y git make

# Build mitra
RUN git clone https://github.com/bouroo/rs-wsProxy --branch=$VERSION && mv -v rs-wsProxy /temp && cd /temp && cargo build --release && mkdir /app && mv /temp/target/release/rs-wsProxy /app/rust-ws2tcp-gateway && cd /app && rm -rfv /temp && touch FJOX.WIN

# Distributed image
FROM debian:${DEBIAN_VERSION}
LABEL maintainer="info@fjox.win"
RUN apt update && apt install curl -y

# Copy compiled rs-wsProxy into working directory
WORKDIR /app
COPY --from=build-env /app /app

# make sure libssl.so.1.1 is available
RUN apt update && apt install -y curl

# Run the app by default when the container starts
ENTRYPOINT ["/app/rust-ws2tcp-gateway"]
CMD ["-p","8080"]