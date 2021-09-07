from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

#HELPER FUNCTION
def request_auth(cid):
    url = "https://accounts.spotify.com/authorize"
    payload = {
        "client_id": cid,
        "response_type": "code",
        "redirect_uri": "http://127.0.0.1:5000/",
        "show_dialog": "true"
    }

    return requests.get(url, payload)


#ROUTES 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/reroute/', methods=['GET', 'POST'])
def reroute():
    
    cid = request.form['cid']
    r = request_auth((cid))
    return redirect(r.url)
