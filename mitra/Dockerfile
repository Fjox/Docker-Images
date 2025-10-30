# Start from an Debian image with the latest version of Rust installed
FROM rust:bookworm as build-env

LABEL maintainer="info@fjox.win"
# Install git
RUN apt update && apt install -y git make

# Build mitra
RUN git clone https://git.fjox.win/mirror/mitra && mv -v mitra /temp && cd /temp && cargo build --release --features production && mkdir /app && mv /temp/target/release/mitra /app/mitra && cd /app && rm -rfv /temp && touch FJOX.WIN && git clone https://git.fjox.win/mirror/mitra-web && mv mitra-web /temp && curl -o- https://fnm.vercel.app/install | bash && fnm install 24 && npm install --no-save && npx allow-scripts && npm run build && mv /temp/dist /app/www && cd /app && rm -rfv /temp

# Distributed image
FROM debian:12-slim
RUN apt update && apt install curl -y

# Copy compiled vulpes-porto into working directory
WORKDIR /app
COPY --from=build-env /app /app

# make sure libssl.so.1.1 is available
RUN apt update && apt install -y curl

# Run the app by default when the container starts
CMD ["/app/mitra","server"]
