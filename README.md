# Backend para obtener los datos (beta)

## Requisitos
* Python 3.10
* venv

El IDE usado es PyCharm

## Para arrancar el servidor

```
python app.py
```

Debería devolver lo siguiente:
```
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: off
   2021-11-12 14:52:40,321 INFO sqlalchemy.engine.Engine SELECT * FROM location WHERE location.imei = '111111111111'
   2021-11-12 14:52:40,322 INFO sqlalchemy.engine.Engine [raw sql] ()
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Documentación en construcción...