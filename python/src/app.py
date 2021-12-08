from flask import Flask, jsonify, request
import sqlite3
import json
import sqlalchemy
from . import db

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)


@app.route('/')
def index():
    return "Welcome to Sports Hub!", 200


def get_conn():
    conn = sqlite3.connect(app.config['activity.db'])
    return conn


@app.route('/activity', methods=['POST'])
def activity():
    try:
        data = request.get_json()
        db = get_conn()
        db.execute('INSERT INTO activity (date, name, duration, distance) VALUES (?, ?, ?, ?)', [data['date'], data['name'], data['duration'], data['distance']])
        db.commit()
        message = "Record Added!"
        return message, 200
    except Exception as e:
        message = "Error " + str(e)
        return message, 200


@app.route('/activity', methods=['GET'])
def activities():
    db = get_conn()
    activities = db.execute('SELECT * FROM activity').fetchall()
    return jsonify(activities)


if __name__ == "__main__":
    create_table()
    app.run(host='127.0.0.1', port=5000)
