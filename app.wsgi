import sys
import site

# Añadir el entorno virtual
#site.addsitedir('/ruta/a/tu/nombre_entorno/lib/python3.x/site-packages')
site.addsitedir('/var/www/spotify-ia-ml/venv/lib/python3.x/site-packages')

#sys.path.insert(0, '/ruta/a/tu/proyecto_donde_esta_endpoint')
sys.path.insert(0, '/var/www/project/spotify-ia-ml')

#from <nombre_endpoint.py> import app as application
from app.py import app as application 
