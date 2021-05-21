FROM postgres:latest
ENV POSTGRES_PASSWORD=admin1
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=database
COPY create.sql /docker-entrypoint-initdb.d/create.sql
