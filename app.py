from flask import Flask, render_template, request, session
from api import google
import urllib2, json

Key = AIzaSyAuLnW45Bedo3D1QRAs0DkqQkDPQW4ykDI

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    search = request.args.get('search')
    google = google.query(search)
    return render_template(
      "home.html",
      search=search,
      google=google
    )

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8000)
