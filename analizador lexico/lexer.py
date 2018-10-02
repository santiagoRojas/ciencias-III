import ply.lex as lex

tokens = [ 'VARIABLE','NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION', 'ASIGNACION','SALTOLINEA' ]

t_ignore = ' \t'
t_SUMA = r'\+'
t_RESTA= r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SALTOLINEA = r'\n'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer



lectura = open("expresiones.in","r")
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
