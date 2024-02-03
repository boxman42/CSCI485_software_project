"""
This is the main script for the project. it contains the nessary functions for the website to run
"""
from flask import Flask, redirect, url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)