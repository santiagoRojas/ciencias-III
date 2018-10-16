import ply.lex as lex
palabrasReservadas = {
    'apagate' : 'EXPRESION',
    'gira-izquierda' : 'EXPRESION',
    'avanza' : 'EXPRESION',
    'coge-zumbador' : 'EXPRESION',
    'deja-zumbador' : 'EXPRESION',
    'sal-de-instruccion' : 'EXPRESION',
    'inicio' : 'EXPRESION',
    'fin' : 'EXPRESION',
    'iniciar-programa' : 'DECLARACION_DEL_PROGRAMA',
    'inicia-ejecucion' : 'DECLARACION_DEL_PROGRAMA',
    'termina-ejecucion' : 'DECLARACION_DEL_PROGRAMA',
    'finalizar-programa' : 'DECLARACION_DEL_PROGRAMA',
    'define-nueva-instruccion': 'DECLARACION_DEL_PROCEDIMIENTO',
    'como': 'DECLARACION_DEL_PROCEDIMIENTO',
    'frente-libre': 'FUNCION_BOOLEANA',
    'frente-bloqueado': 'FUNCION_BOOLEANA',
    'izquierda-libre': 'FUNCION_BOOLEANA',
    'izquierda-bloqueada': 'FUNCION_BOOLEANA',
    'derecha-libre': 'FUNCION_BOOLEANA',
    'derecha-bloqueada': 'FUNCION_BOOLEANA',
    'junto-a-zumbador': 'FUNCION_BOOLEANA',
    'no-junto-a-zumbador': 'FUNCION_BOOLEANA',
    'algun-zumbador-en-la-mochila': 'FUNCION_BOOLEANA',
    'ningun-zumbador-en-la-mochila': 'FUNCION_BOOLEANA',
    'orientado-al-norte': 'FUNCION_BOOLEANA',
    'orientado-al-sur': 'FUNCION_BOOLEANA',
    'orientado-al-este': 'FUNCION_BOOLEANA',
    'orientado-al-oeste': 'FUNCION_BOOLEANA',
    'no-orientado-al-norte': 'FUNCION_BOOLEANA',
    'no-orientado-al-sur': 'FUNCION_BOOLEANA',
    'no-orientado-al-este': 'FUNCION_BOOLEANA',
    'si': 'EXPRESION_SI',
    'entonces': 'EXPRESION_SI',
    'sino': 'EXPRESION_SI',
    'mientras': 'EXPRESIONES_MIENTRAS',
    'hacer': 'EXPRESIONES_MIENTRAS',
    'repetir': 'EXPRESIONES_PARA',
    'veces': 'EXPRESIONES_PARA',
    'no': 'CLAUSULA_NO',

}

tokens = [ 'NUMERO','SALTOLINEA','EXPRESIONCIERRE' ]+ list(palabrasReservadas.values())


t_SALTOLINEA = r'\n+'
t_ignore = r' \t'
t_EXPRESIONCIERRE= r';'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CARACTER_ILEGAL(t):
    r'[a-zA-Z_][-_a-zA-Z_0-9]*'
    t.type = palabrasReservadas.get(t.value,'CARACTER_ILEGAL')
    if t.type != 'CARACTER_ILEGAL' :
        return t
    else:
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(1)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex() # Build the lexer



lectura = open("Codigokarel.in","r")
for i in lectura.readlines():
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
lectura.close()
