# senti_one

## PREREQUISITS
- docker version `20.10.6`

- docker-compose version `3.9`

## BUILD & RUN

Please clone this repository and execute:
```
docker-compose up --build
```
while in your local directory `../senti_one`


( In case you don't have `docker compose` plese install it:
```https://docs.docker.com/compose/install/``` )

In `docker-compose.yml` version is set as `3.9`, please use this version or change this number to your local version.

## APP

To use the app, open your internet browser and go to:
```
localhost:8080
```
Use the buttons and text input to insert something into postgresql database (via `POST`) or to test what happens if `GET` request is sent.

## DATABASE
To enter the database please enter the container:
```
docker exec -it senti1_db bash
```
(do this in another terminal session, while containers are running)

and then:
```
psql -h localhost -p 5432 -d database -U admin --password
```
password: `admin1`

To show the tables type:
```
\dt
```
To show data from table type:
```
SELECT * FROM PSQLDATA;
```
Try this before and after submiting some data at `localhost:8080`

Press `ctrl + D` to exit database, again to exit the container.
## CURL REQUESTS
To test curl requesests (`GET|POST`) please enter the senti1_app container by:
```
docker exec -it senti1_app bash
```
and execute:
```
chmod +x curls.sh && ./curls.sh
```
The `curls.sh` will send `GET` and `POST` requests. 

Responses and requests syntax should appear bellow the executed command.

Docker will also output logs:
```
senti1_app | 127.0.0.1 - - [24/May/2021 08:11:45] "GET /post_to_psql_db HTTP/1.1" 405 -
senti1_app | 127.0.0.1 - - [24/May/2021 08:11:45] "POST /post_to_psql_db HTTP/1.1" 302 -
```
`POST` request has default input: `n=test_response`, it will be saved in database (steps to check it above ⬆️)

You can also check curls manually, by:
```
curl -X GET "http://localhost:8080/post_to_psql_db" && curl -X POST -F "n=test_response" "http://localhost:8080/post_to_psql_db"
```
<br><br>
If You have any questions or problems with runing this build, please dont hasitate to ask at any moment!
