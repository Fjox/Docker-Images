FROM python:slim-bookworm
LABEL maintainer="info@fjox.win"

# Define some defaults
ENV HASH_DIR /hashdir/
ENV DRY_RUN "N"
ENV MASTODON_VISIBILITY "public"
ENV SKIP_TAGS ""

# Install deps and create basedirs
RUN mkdir /app && mkdir /app/hashdir && cd /app && pip install feedparser requests && apt install curl -y && curl https://git.fjox.win/Fjox/rss-to-mastodon/raw/branch/main/run.py

WORKDIR /app
CMD ["python","/app/run.py"]