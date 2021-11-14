# Backend para TransMap (alpha release)
## Referencia de la API

* [Ir a la documentación de la API Rest](doc/reference.md)
## Descripción

El servidor está diseñado para recibir y almacenar datos enviados en forma de JSON por una aplicación de Android que se
ejecutará continuamente en segundo plano, como un servicio.

El JSON tiene el siguiente formato:

````json5
{
  "imei": "35xxxxxxxxx",  // IMEI estándar de 11 dígitos
  "latitude": "xx.xxxxx", // Latitud del dispositivo en formato decimal
  "longitude": "xx.xxxxx" // Longitud geográfica del dispositivo en formato decimal
}
````
## Instalación

* Clonar este repositorio

````shell
git clone https://github.com/victorovento/gpstracker-upr-beta.git
````
* Instalar las dependencias
````shell
pip install -r requirements.txt
````

Recomiendo usar virtualenv:  --> https://docs.python.org/3/library/venv.html

## Instrucciones

Escribir en la consola:
````shell
python app.py
````

Debería devolver lo siguiente:

````shell
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: off
   2021-11-12 14:52:40,321 INFO sqlalchemy.engine.Engine SELECT * FROM location WHERE location.imei = '111111111111'
   2021-11-12 14:52:40,322 INFO sqlalchemy.engine.Engine [raw sql] ()
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
````

## Configuraciones del servidor
Puedes ajustar los parámetros del servidor a tu gusto cambiando el valor de algunas variables de entorno:
* En ``db_conection.py``
````python
DB_PATH = 'sqlite:///db/location.db' # Ruta de la base de datos SQlite
TABLE_NAME = 'location' # Nombre de la tabla para guardar las ubicaciones
````

* En ``app.py``

````python
SERVER_HOST = '127.0.0.1' # IP del servidor
SERVER_PORT = '5000' # Puerto del servidor
DEBUG = False # Trastear tanto es malo
````

# Próximamente
* Compatibilidad con rutas GPS
* Agrupar los endpoints de la API en resources
* ... etc
### Documentación en construcción...
