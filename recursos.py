#aqui pongo los recursos que mi servidor  tendrá disponibles
#vamos a crear recursos: para esto lo haremos a través de clases y objetos, los  RECURSOS son  la información
#que tendrá disponible el servidor para cuando  le preguntemos algo.
from flask_restful import Resource
from flask import make_response, render_template #estos 2 que estoy importando son metodos es decir, son funciones

class  HolaMundo(Resource): #El argumento resource es para indicar que es un recurso y no una clase de POO.
    def get(self):#Aqui ya  no es necesario que meta un método constructor pues ya se está siendo heredado  del Resource
        return {'hola':'Mundo'} #aqui  estoy retornando un diccionario

class PantallaInicio(Resource):
    def get(self):
        contenido = render_template('index.html') #aqui cree la variable contenido y le estoy pidiendo que, a través de la función
        # renderice lo que encuentre en  el archivo index, renderizar quiere decir preparar una serie de información para que se
        #pueda ver correctamente en otro dispositivo
        return make_response(contenido) #aqui retornamos el contenido renderizado en una respuesta