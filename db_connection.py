from sqlalchemy import create_engine, select
from sqlalchemy.exc import SQLAlchemyError

DB_PATH = 'sqlite:///db/location.db'
TABLE_NAME = 'location'

engine = create_engine(DB_PATH, echo=True)


def add_location(imei, latitude, longitude):
    """
    :param imei: Unique smartphone identifier.
    :param latitude: Only send data in decimal degrees. ex: 12.33321
    :param longitude: Only send data  in decimal degrees ex: -23.3334
    :return:  should prompt in console:
                No of records added  :  1
                Id of last record added :  1
    """
    q = 'INSERT INTO {} VALUES(\'{}\', \'{}\', \'{}\')'.format(TABLE_NAME, imei, latitude, longitude)
    try:
        r_set = engine.execute(q)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print('ERROR {}, IMEI = {}'.format(error, imei))
    else:
        print('Actualizada la ubicación de {}\n'.format(imei))


def get_location(imei):
    """

    :param imei: The unique identifier of the smartphone
    :return: Return the latitude and longitude (decimal) in a tuple
    """
    stmt = 'SELECT * FROM location WHERE location.imei = \'{}\''.format(imei)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            return row
