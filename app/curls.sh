#GET
echo $'\nexecuting:\n\ncurl -X GET "http://localhost:8080/post_to_psql_db"\n\noutput:\n'
echo $(curl -X GET "http://localhost:8080/post_to_psql_db")

echo $'\n\n\n'
#POST
echo $'executing:\n\ncurl -X POST -F "n=test_response" "http://localhost:8080/post_to_psql_db"\n\noutput:\n'
echo $(curl -X POST -F "n=test_response" "http://localhost:8080/post_to_psql_db")
echo $'\ngo to database and check if "test_response" is saved (instructions in github readme)'