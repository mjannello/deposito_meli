# Proyecto Depósito Meli

API Restful hecha en Flask con su respectivo documento Swagger para la gestión del Negocio de MercadoEnvíos relacionado al ingreso de productos a los depósitos.

Integración con las extensiones  Flask-restplus, Flask-SQLalchemy y marshmallow .

Versión de `Python 3.8.2`

### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Marshalling: [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) 


## Instalación

Creación de virtual environment. Dentro de la carpeta web/:

```
$ python -m venv env
```

Activación de virtual environment:

```
$ ./env/Scripts/activate
```

Instalación con pip:

```
$ pip install -r requirements.txt
```

## Configuración Flask

#### Seteo en desarrollo

```
$ set FLASK_APP=infrastructure/app.py
$ set FLASK_ENV=development
```

## Run Flask
### Iniciar la aplicación
```
$ flask run
```
En Flask, El puerto Default es `5000`

Documento Swagger:  `http://127.0.0.1:5000/`

## Estructura de Aplicación Flask
```
.
|──────web/
| |────__init__.py
| |────domain/
| | |────__init__.py
| | |────models/
| | |────use_cases/
| | |────tests/
| |────infrastructure/
| | |────__init__.py
| | |────views/

```



## Pytest
```
$ pytest
```


## Referencias

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
