#aqui estan las rutas de acceso a cada recurso
from recursos import *

#Aqui necesitamos también el objeto api, pero ese mismo objeto también debe existir en mi archivo app.py, para que el
#mismo objeto viva en 2 lugares a la  vez puedo definir una funcion en donde el argumento  que reciba será
#precisamente api, ojo para que funcione debo immportar los recursos que tengo en mi archvo de recursos.py, por eso hasta arriba le puse import from recursos * (también puedo declararlos uno a uno si no quiero poner el asterisco)
def crear_rutas(api):
    # Ahora le  dire a la API que puede acceder a este recurso por medio de tal ruta
    # si quiero llegar a un  recurso en especifico debo indicarle la ruta y esto lo hago con api.add_resource() en donde
    # el 1er argumento es el recurso que va a invocar y el 2do es la direccion de ese recurso.
    api.add_resource(HolaMundo,'/hola')  # HolaMundo es el recurso  y 'hola' es la direcciòn, en este caso es la parte del diccionario que retorne anteriormente cuando cree el recurso HolaMundo
    # al correr el código en la consola me saldrá una url, si le doy click me dara un not found pero, en el navegador al final de la url le pongo /hola y me saldrá el diccionario que configuré
    api.add_resource(PantallaInicio, '/')  # aqui la ruta solo será un slash porque digamos que es la ruta de inicio



