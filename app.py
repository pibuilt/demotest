from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the AI Test Case Generator!"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"sum": a + b})

@app.route("/status")
def status():
    return jsonify({"status": "Running", "code": 200})

if __name__ == "__main__":
    app.run(debug=True)
