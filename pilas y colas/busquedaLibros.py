# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se r{epresenta con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
class Libro:
    def __init__(self,nombre,categoria,autor):
        self.nombre = nombre
        self.categoria = categoria
        self.autor = autor
    def getNombre(self):
        return self.nombre

archivo = open("libros.csv","r")
lista = [(x.split(";")[0],x.split(";")[1],x.split(";")[2]) for x in archivo.readlines()]

pila = Pila()
for x in lista:
    libro = Libro(x[0],x[1],x[2].strip("\n").strip("\r").strip(" "))
    pila.apilar(libro)

opcion = int(input("digite la opcion que desea realizar \n 1 si desea buscar por nombre del libro \n 2 si desea buscar por categoria del libro\n 3 si desea buscar por autor del libro\n"))
if(opcion == 1 or opcion == 2 or opcion == 3):
    busqueda = raw_input("digite para empezar la busqueda\n")
    if opcion == 3:
        busqueda = busqueda +" \r\n"
    validacion = False
    while validacion == False:
        try:
            ultimoLibro = pila.desapilar()
            if(opcion == 1):
                if(ultimoLibro.nombre == busqueda):
                    validacion = True
            elif (opcion == 2):
                if(ultimoLibro.categoria == busqueda):
                    validacion = True
            elif (opcion == 3):
                if(ultimoLibro.autor == busqueda+"\n"):
                    print "ENTRO"
                    validacion = True
            if(validacion == True):
                print "Primer libro encontrado con la especificacion es \n nombre del libro:", ultimoLibro.nombre," \n categoria: ",ultimoLibro.categoria ,"\n autor:", ultimoLibro.autor
        except IndexError:
            print "La pila está vacía, no se encontro un libro con estas especificaciones"
            validacion = True

else:
    print "opcion invalida"

