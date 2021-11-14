# TransMAP API

## Guía de referencia

### Lista

| METHODS | URL                    | DESCRIPTION                           |
|---------|------------------------|---------------------------------------|
|GET      |/location/?imei=        | Recibe un IMEI como parámetro de la URL y envía un fichero JSON con las keys ``imei``, ``latitude``,``longitude`` |
|POST     |/location               | Enviar un JSON con las keys ``imei``, ``latitude``, ``longitude``|


#### Como debe de ser el JSON
````json5
{
  "imei": "35xxxxxxxxx",  // IMEI estándar de 11 dígitos
  "latitude": "xx.xxxxx", // Latitud del dispositivo en formato decimal
  "longitude": "xx.xxxxx" // Longitud geográfica del dispositivo en formato decimal
}
````