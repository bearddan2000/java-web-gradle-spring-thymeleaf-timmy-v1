FROM ubuntu:22.04

WORKDIR /workspace

RUN apt update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    pdftk

WORKDIR /code

COPY bin .

CMD ./code/run.sh