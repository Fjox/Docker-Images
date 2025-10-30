# Start from an Debian image with the latest version of Go installed
FROM golang:bookworm as build-env

LABEL maintainer="info@fjox.win"
# Install git
RUN apt update && apt install -y git make

# Build bloat
RUN git clone https://git.fjox.win/Fjox/8bloat && mv -v 8bloat /app && cd /app && touch FJOX.WIN && make 

# Distributed image
FROM debian:12
RUN apt update && apt install curl -y

# Copy compiled bloat into working directory
WORKDIR /app
COPY --from=build-env /app /app

# Run the app by default when the container starts
CMD ["/app/bloat"]
