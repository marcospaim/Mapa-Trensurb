# Servidor do Sistema
# Chama a Aplicação Flask
# 25_11_2020
# Riboldi

from gevent.pywsgi import WSGIServer
#from yourapplication import app
from index import app
import config
import os 

abs_path = os.path.abspath('.')
#print(abs_path)
app.template_folder = abs_path + '/templates'
app.static_folder = abs_path + '/static'

USER, PASSWORD, PORTA, IP_HOST = config.get_config()
PORTA = int(PORTA)

http_server = WSGIServer((IP_HOST, PORTA), app)# PODERÁ AJUSTAR O IP E PORTA
http_server.serve_forever()
