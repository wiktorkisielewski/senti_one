import psycopg2
import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/post_to_psql_db', methods=['POST', 'GET'])
def post_it():
	con = psycopg2.connect(database="database", user="admin", password="admin1", host="senti1_db", port=5432)
	cur = con.cursor()
	if request.method == 'POST':
	    data = request.form['n']
	    cur.execute("INSERT INTO psqldata (RESPONSE, TIME_STAMP) VALUES ('{}', '{}');".format(str(data), str(datetime.datetime.now())))
	    con.commit()
	    con.close()
	    return redirect(url_for('main'))

@app.route('/get_request')
def get_req():
	if request.method == 'GET':
		return render_template('index.html')

if __name__ == '__main__':
    app.run()