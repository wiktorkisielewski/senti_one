import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/post_to_psql_db', methods=['POST', 'GET'])
def post_it():
	con = psycopg2.connect(database="database", user="admin", password="admin1", host="senti1_db", port=5432)
	if request.method == 'POST':
	    data = request.form['n']
	    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')