# Start from an Debian image with the latest version of Rust installed
FROM rust:bookworm as build-env

LABEL maintainer="info@fjox.win"
# Install git
RUN apt update && apt install -y git make

# Build vulpes-porto
RUN git clone https://git.fjox.win/mirror/vulpes-porto && mv -v vulpes-porto /temp && cd /temp && cargo build --release && mkdir /app && mv /temp/target/release/vulpes_porto /app/vulpes_porto && cd /app && rm -rfv /temp && touch FJOX.WIN && ls -laRh

# Distributed image
FROM debian:12-slim
RUN apt update && apt install curl -y

# Copy compiled vulpes-porto into working directory
WORKDIR /app
COPY --from=build-env /app /app

# make sure libssl.so.1.1 is available
RUN apt update && apt install -y curl

# Run the app by default when the container starts
CMD ["/app/vulpes_porto","--config","/app/config.yaml"]
