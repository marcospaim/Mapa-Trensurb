from cx_Freeze import setup, Executable

includefiles = [ 'templates/', 'static/', 'index.py', 'config.py', 'Configurações.csv','estacoes.csv','sentido.py','TUE 102.csv']
include = [ 'jinja2', 'jinja2.ext',]

setup(
 name='Mapa Trensurb',
 version = '0.1',
 description = 'Aplicação Flask com mapa de trens em tempo real',
 options = {'build_exe':   {'include_files':includefiles, 'includes': include,}},
 executables = [Executable('Servidor.py')]
)
