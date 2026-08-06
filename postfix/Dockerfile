FROM debian:bookworm

RUN apt update && \
    apt install -y \
        postfix \
        postfix-mysql \
        postfix-pcre \
        rsyslog \
        ca-certificates && \
    apt clean

CMD ["/usr/sbin/postfix","start-fg"]