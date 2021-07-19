# to start, terminal initiate: pipenv shell -> flask run
from flask import Blueprint, request
from flask.templating import render_template
import requests

main = Blueprint('main', __name__)

# not yet dohne
@main.route('/', methods = ["GET", "POST"])
def index():
        if request.method == "GET":
            return render_template("index.html")
        
        elif request.method == "POST":
            form        = request.form
            key_word    = form['search_engine']
            from .result import final_list
            return final_list


