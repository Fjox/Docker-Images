FROM python:slim-bookworm
LABEL maintainer="info@fjox.win"

# Define some defaults
ENV HASH_DIR /hashdir/
ENV DRY_RUN "N"
ENV MASTODON_VISIBILITY "public"
ENV SKIP_TAGS ""

# Install deps and create basedirs
RUN pip install feedparser requests && mkdir /app && mkdir /app/hashdir

COPY run.py /app/

WORKDIR /app
CMD ["python","/app/run.py"]