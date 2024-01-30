"""
This is the main script for the project. it contains the nessary functions for the website to run
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is the home page"














if __name__ == "__main__":
    app.run(debug=True, port=8000)