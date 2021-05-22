import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
	con = psycopg2.connect(database="database", user="admin", password="admin1", host="senti1_db", port=5432)
	return "Database opened successfully"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')