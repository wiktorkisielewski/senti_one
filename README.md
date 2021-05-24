# senti_one

## BUILD & RUN

Please clone this repository and execute:
```
docker-compose up --build
```
while in your local directory `../senti_one`


( In case you don't have `docker compose` plese install it:
```https://docs.docker.com/compose/install/``` )

## APP

To use the app, go to:
```
localhost:8080
```
Use the buttons and text input to insert something into postgresql database (via `POST`) or to test what happens if `GET` request is sent.

## DATABASE
To enter the database please enter the container:
```
docker exec -it senti1_db bash
```
and then:
```
psql -h localhost -p 5432 -d database -U admin --password
```
password `admin1`

To show the tables type:
```
\dt
```
To show data from table type:
```
SELECT * FROM PSQLDATA;
```
Try this before and after submiting some data at `localhost:8080` 
