from flask import Flask, request
import subprocess
import os
from config import *

app = Flask(__name__)

# Debug ligado em produção (vulnerável)
app.config["DEBUG"] = True

@app.route("/")
def home():
    return "Aplicação extremamente insegura 😈"

# Execução insegura de comando
@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.getoutput(f"ping -c 1 {host}")  # Command Injection

# Uso inseguro de eval
@app.route("/calc")
def calc():
    expression = request.args.get("exp")
    return str(eval(expression))  # RCE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
