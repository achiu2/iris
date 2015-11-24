from flask import Flask, render_template, request, session
import google
import urllib2, json
import bs4, re

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("home.html")
    else:
        search = request.form["search"]
        results = google.search(search, num=10, start=0, stop=10)
        print search
        
        rlist = []
        for r in results:
            rlist.append(r)
        
        url = urllib2.urlopen(rlist[0])
        page = url.read()
        soup = bs4.BeautifulSoup(page, 'html')
        raw = soup.get_text()
        clean = 

        return render_template(
            "home.html",
            search=search,
            results=results
            )

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8000)
