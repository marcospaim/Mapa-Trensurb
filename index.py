from flask import Flask, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("page.html")

@app.route("/gps")
def gps():
    response = None
    #try:
    response = requests.get("http://gps-trens.trensurb.gov.br:5244/coordenadas/api/v1.0/GPS",auth=HTTPBasicAuth('susan', 'bye'))
    response = response.json()
    #except:
        #print("Nao foi possivel conectar-se com a api")
    
    return response, 200

#if __name__ == '__main__':
#    app.run()