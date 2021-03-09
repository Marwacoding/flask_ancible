from flask import Flask, render_template, jsonify, request
from flask_cors import CORS 
from postgres import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome(): 
    return render_template("index.html")

@app.route('/inc', methods=['GET'])
def increment_id():

    logging.info("[FLASK] Insert data in table : start")
    cursor.execute("""SELECT * FROM my_table""")
    output = cursor.fetchall()
    logging.info("[FLASK] Insert data in table : end")
    return jsonify(output)


@app.route('/id', methods=['GET'])
def get_current_id():
    logging.info("[FLASK] get current id : start")
    cursor.execute("""INSERT INTO my_table (id) values(default) RETURNING id;""")
    output = cursor.fetchall()
    logging.info("[FLASK] returning last id : end")
    return jsonify(output)



if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)