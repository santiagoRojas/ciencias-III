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

i = 0
diccionario = dict()

def evaluar(arbol):
    if arbol.valor in "abcdefghijklmnopqrstuvwxyz":
        return diccionario[arbol.valor]
    if arbol.valor == "=":
        diccionario[arbol.der] = evaluar(arbol.izq)
            return str(arbol.der)+"="+str(diccionario[arbol.der])
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
