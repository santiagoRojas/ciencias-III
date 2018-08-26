# -*- coding: utf-8 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

class Estudiante:
    def __init__(self,nombre,codigo,placa):
        self.nombre = nombre
        self.codigo = codigo
        self.placa = placa

validacion = True
cola = Cola()
while validacion ==True:

    print "bienvenidos al sistema de asignacion de cupos de parqueadero de la universidad distrital \n recuerde que los cupos son limitados\n"

    nombre = raw_input("digite su nombre completo \n")
    codigo = int(raw_input("digite su codigo de estudiante \n"))
    placa = raw_input("digite la placa del vehiculo\n")

    estudiante = Estudiante(nombre,codigo,placa)
    cola.encolar(estudiante)

    opcion = raw_input("si desea seguir ingresando estudiantes escriba cualquier tecla, de lo contrario escriba 1 para proceguir con la asignacion de cupos")
    if opcion == '1':
        validacion = False
cupos = int(input("cuantos cupos desea habilitar"))
print "los siguientes estudiantes obtendran un cupo"
for i in range(0,cupos):
    try:
        estudianteActual = cola.desencolar()
        print "estudiante numero ",i+1,"\n nombre: ",estudianteActual.nombre,"\n codigo: ",estudianteActual.codigo,"\n placa del vehiculo: ",estudianteActual.placa
    except IndexError:
        print "demasiados cupos, cola vacia"
