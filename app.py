
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tips")
def tips():
    return jsonify([
        "Study daily with focus",
        "Revise before sleeping",
        "Practice coding hands-on",
        "Teach others to learn faster"
    ])

@app.route("/quiz", methods=["POST"])
def quiz():
    answer = request.json.get("answer")
    return jsonify({"correct": answer.lower() == "def"})

@app.route("/notes", methods=["GET", "POST"])
def notes():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS notes (content TEXT)")
    if request.method == "POST":
        cur.execute("INSERT INTO notes VALUES (?)", (request.json["note"],))
        conn.commit()
    cur.execute("SELECT content FROM notes")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
