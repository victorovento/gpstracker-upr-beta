import flask
from flask import Flask, jsonify, request
import db_connection
import datetime

SERVER_HOST = '127.0.0.1'
SERVER_PORT = '5000'
DEBUG = True

app = Flask(__name__)


@app.route('/location', methods=["GET"])
def get():
    imei = request.args["imei"]
    locationtuple = db_connection.get_location(imei)
    locationdict = {
        "imei": locationtuple[0],
        "latitude": locationtuple[1],
        "longitude": locationtuple[2]
    }

    return jsonify(locationdict)


@app.route('/location', methods=["POST"])
def post():
    json_data = flask.request.json
    imei = json_data["imei"]
    latitude = json_data["latitude"]
    longitude = json_data["longitude"]
    try:
        db_connection.add_location(imei, latitude, longitude)
    except Exception as e:
        error = str(e)
        print(error)
        return error
    else:
        return '{"message:"added"}'


# TODO Guardar rutas
# TODO Crear clases para los recursos.
# TODO Meterle seguridad
# TODO Base de datos decente

if __name__ == '__main__':
    print('\nBienvenido al servidor de *******\n')
    print('---------------------------------\n')
    print('Hoy es {}\n'.format(datetime.datetime.now()))
    app.run(debug=DEBUG, host=SERVER_HOST, port=SERVER_PORT)

