from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)



def request_auth(cid="ae94085f9ba742fc811ec3ecfbc1e864"):
    url = "https://accounts.spotify.com/authorize"
    payload = {
        "client_id": cid,
        "response_type": "code",
        "redirect_uri": "http://127.0.0.1:5000/",
        "show_dialog": "true"
    }

    return requests.get(url, payload)



@app.route("/")
def hello_world():

    

    if request.method == "GET":
        cid = request.form.get('cid')
        r = request_auth(cid)
        return redirect("/submit")

    return render_template('index.html')


@app.route("/submit/", methods=['GET', 'POST'])
def submit():
    return redirect(request_auth().url)

    # return r.url
    # return redirect(r.url)