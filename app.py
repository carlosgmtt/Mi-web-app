#importamos la clase Flask
from flask import Flask

#importamos la clase API y RESOURSE desde flask_restful
from flask_restful import Api, Resource
from rutas import crear_rutas #aqui estoy importando mi función crear rutas del archivo rutas.py

#Vamos a ccrear un objeto de tipo Flask
app=Flask(__name__)

#creamos un objeto de tipo API y como argumento le pasamos el objeto app, ese objeto app es el objeto de Flask
#La API será el programa que se communique con  el dispositivo físico
api=Api(app)

crear_rutas(api)

app.run(port=8080, debug=True) #Del objeto app ejecutamos el metodo RUN, eso hace que mi compu sea como un servidor esto siempre debe ir al final para que funcione