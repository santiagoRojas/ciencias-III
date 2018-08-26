from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":

            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

a = None
b = None
c = None
i = 0

def evaluar(arbol):
    if arbol.valor in "abc":
        if arbol.valor == "a":
            return a
        if arbol.valor == "b":
            return b
        if arbol.valor == "c":
            return c
    if arbol.valor == "=":
        if (arbol.der).valor == "a":
            global a
            a = int(evaluar(arbol.izq))
            return a
        if (arbol.der).valor == "b":
            global b
            b = int(evaluar(arbol.izq))
            return b
        if (arbol.der).valor == "c":
            global c
            c = int(evaluar(arbol.izq))
            return c

    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

pila = Pila()

lectura = open("expresiones_2.in","r")
escritura = open("expresiones_2.out","w")

for i in lectura.readlines():
    convertir(i.strip("\n").split(" "),pila)
    resultado = evaluar(pila.desapilar())
    escritura.write(str(resultado)+"\n")

lectura.close()
escritura.close()
