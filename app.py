from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "done": False},
    {"id": 2, "title": "Deploy to AWS", "done": False}
]

@app.route("/")
def home():
    return {"message": "Mini Task API is running!"}

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)