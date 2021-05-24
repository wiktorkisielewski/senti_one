FROM postgres:latest

ENV POSTGRES_PASSWORD=admin1
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=database

RUN apt-get update && apt-get install -y curl

COPY create.sql /docker-entrypoint-initdb.d/create.sql

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*