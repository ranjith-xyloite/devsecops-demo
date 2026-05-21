from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Demo"

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

app.run(host="0.0.0.0", port=5000)
