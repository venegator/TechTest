# Using ubuntu 22.04 as base image.
FROM ubuntu:22.04
RUN apt-get update && \
    # Installing nmap and ndiff.
    apt-get install --no-install-suggests --no-install-recommends --yes nmap ndiff && \
    # Liberating some space.
    rm -rf /var/lib/apt/lists/* && \
    # Creating workdir.
    mkdir /app
COPY scanner.sh /app
WORKDIR /app
ENTRYPOINT ["./scanner.sh"]