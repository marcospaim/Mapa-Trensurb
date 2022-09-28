
import requests
from requests.auth import HTTPBasicAuth
from config import get_estacoes, get_path
from math import pi

def radian2degree(radian):
    return radian*180/pi

def add_sentido(response):
    
    #response = requests.get("http://gps-trens.trensurb.gov.br:5244/coordenadas/api/v1.0/GPS",auth=HTTPBasicAuth('susan', 'bye'))
    #response = response.json()
    #response["Coordenadas"][:] = [d for d in response["Coordenadas"] if not polygon.contains(Point(float(d.get("Latitude")), float(d.get("Longitude"))))] # filtra trens no estacionamento

    estacoes = get_estacoes()
    estacoes = sorted(estacoes.items(), key=lambda e: float(e[1][1]))
    estacoes = [x[1] for x in estacoes]
    for d in response["Coordenadas"]:
        sentido = '-'
        
        for i in range(len(estacoes)-1):
            if(radian2degree(float(d["Latitude"])) > float(estacoes[i][1]) and radian2degree(float(d["Latitude"])) < float(estacoes[i+1][1])):
                if(d["Orientacao"] > 120 and d["Orientacao"] < 300): #sul
                    sentido = f"{estacoes[i+1][0]} → {estacoes[i][0]}"
                else:
                    sentido = f"{estacoes[i][0]} → {estacoes[i+1][0]}"
        
            
        d["sentido"] = sentido
    #print(response)
    return response
        
    