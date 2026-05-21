from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    username = request.args.get("username")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)

    return "Executed query"

app.run(host="0.0.0.0", port=5000)
