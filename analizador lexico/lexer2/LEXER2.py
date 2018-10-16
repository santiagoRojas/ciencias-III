import ply.lex as lex
palabrasReservadas = {
       'if' : 'IF',
       'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'SUM' : 'SUMA',
   'RES' : 'RESTA',
   'DIV' : 'DIVISION',
   'MULT' : 'MULTIPLICACION',
   'IGU' : 'ASIGNACION',
   'and' : 'y',
   'or' : 'o',
}

tokens = [ 'NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION', 'ASIGNACION','SALTOLINEA','VARIABLE','MAYOR','MENOR','IGUALDAD','FINPREGUNTA' ]+ list(palabrasReservadas.values())

t_IGUALDAD = r'=='
t_MENOR = r'<'
t_MAYOR = r'>'
t_SUMA = r'\+'
t_RESTA= r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_SALTOLINEA = r'\n'
t_ignore = r' \t'
t_FINPREGUNTA = r':'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasReservadas.get(t.value,'VARIABLE')
    return t
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex() # Build the lexer



lectura = open("expresiones2.in","r")
a= 0
for i in lectura.readlines():
    a= a+1
    print "\n expresion ",(a)
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
lectura.close()
