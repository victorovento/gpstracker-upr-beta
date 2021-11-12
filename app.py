from flask import Flask, jsonify, request
import db_connection

app = Flask(__name__)


@app.route('/location=<string:imei>')
def get(imei):
    locationtuple = db_connection.get_location(imei)
    locationdict = {
        "imei": locationtuple[0],
        "latitude": locationtuple[1],
        "longitude": locationtuple[2]
    }

    return jsonify(locationdict)


def post():
    pass


if __name__ == '__main__':
    app.run()
