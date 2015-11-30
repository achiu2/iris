from flask import Flask, render_template, request, session
import utils

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("home.html")
    else:
        query = request.form['search']
        results = utils.Search(query)
        return render_template("results.html", results=results, query=query)

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8000)
