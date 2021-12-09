import sqlite3
import json
import jsonify
from flask import Flask, Response, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(database.db)
    conn.row_factory = sqlite3.Row
    return conn

def valid(activity):
    try:
        name = activity.get("name")
        date = activity.get("date")
        duration = activity.get("duration")
        distance = activity.get("distance")
        assert name is not None
        assert date is not None
        assert isinstance(duration, int)
        assert isinstance(distance, int)
    except:
        return False
    return True

@app.route('/')
def index():
    return "Welcome to Sports Hub!", 200

@app.route('/activity', methods=['GET', 'POST'])
def activity():
    conn = get_db_connection()
    if request.method == 'GET':
        current = db.execute("SELECT name, duration, date, distance FROM activities")
        entries = [{"name":row[0], "duration":row[1], "date":row[2], "distance":row[3]} for row in current.fetchall()]
        return jsonify(entries), 200
    elif request.method == 'POST':
        activity = request.get_json()
        if activity is None:
            abort(400)
        entries = (activity["date"], activity["duration"], activity["distance"], activity["name"])
        conn.execute("INSERT INTO activities(date, duration, distance, name) values (?,?,?,?)", entries)
        conn.commit()
        return "Record Added!", 200
    else:
        return 'Error', 400

if __name__ == "__main__":
    
    app.run(host="127.0.0.1", port=5000, debug=True)