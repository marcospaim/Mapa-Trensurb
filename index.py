from flask import Flask, render_template
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

app = Flask(__name__)

gps_dict = {}
last_request = datetime.now()


@app.route("/")
def hello_world():
    return render_template("page.html")

@app.route("/gps")
def gps():
    global last_request
    global gps_dict
    now = datetime.now()
    response = None
    if(now-last_request > timedelta(seconds=3.9)):
        try:
            response = requests.get("http://gps-trens.trensurb.gov.br:5244/coordenadas/api/v1.0/GPS",auth=HTTPBasicAuth('susan', 'bye'))
            gps_dict = response.json()
            last_request = datetime.now()
        except:
            print("Nao foi possivel conectar-se com a api")
    
    return gps_dict, 200

#if __name__ == '__main__':
#    app.run()