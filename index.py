from flask import Flask, render_template
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import sys
from config import get_estacoes, get_path, get_config
from shapely.geometry import Polygon, Point
from sentido import add_sentido
from configData import config_data

app = Flask(__name__)

gps_dict = {}
last_request = datetime.now()

USER, PASSWORD, PORTA, IP_HOST = get_config()

@app.route("/")
def hello_world():
    return render_template("page.html")

@app.route("/estacoes")
def estacoes():
    data = get_estacoes()
    return data, 200

@app.route("/path")
def path():
    data = get_path()
    return data, 200

@app.route("/gps")
def gps():
    global last_request
    global gps_dict
    #poligono do estacionamento:
    polygon = Polygon([[-0.5233351925190677, -0.893288167243242], [-0.523312262618596, -0.8932787109408987], [-0.5232951714345575, -0.8932726486086261], [-0.5232563456389547, -0.893260570756533], [-0.5232255885036832, -0.8932530103954536],
[-0.5232075840737014, -0.893247580043467], [-0.5231970307147245, -0.8932528114385831], [-0.5232884707521295, -0.8933067404506981], [-0.5233315128073881, -0.893339439591996]])
                    
    now = datetime.now()
    response = None
    if(now-last_request > timedelta(seconds=10)):
        #try:
        response = requests.get("http://10.0.0.43:5244/coordenadas/api/v1.0/GPS",auth=HTTPBasicAuth(USER, PASSWORD))
        response = response.json()
        response["Coordenadas"][:] = [d for d in response["Coordenadas"] if not polygon.contains(Point(float(d.get("Latitude")), float(d.get("Longitude"))))] # filtra trens no estacionamento
        response = add_sentido(response)
        config_data(response)
        gps_dict = response
        last_request = datetime.now()
        #except:
            #print("Nao foi possivel conectar-se com a api")
    
    return gps_dict, 200

if __name__ == '__main__':
    app.run(port=5000)