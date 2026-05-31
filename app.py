from flask import Flask, jsonify
import time

app = Flask(__name__)
counter = 0

@app.route('/time')
def get_time():
    global counter
    counter += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": counter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)