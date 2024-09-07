import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"<p>Hello {os.getenv("BACKEND")} World from {os.getenv("ENVIRONMENT")}!</p>"
