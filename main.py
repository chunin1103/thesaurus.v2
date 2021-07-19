from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        form        = request.form
        key_word    = form['search_engine']



@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)