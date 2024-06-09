import ply.lex as lex

# resultado del analisis
resultado_lexema = []
resultado_tabla = []
conteo_tokens = {}

categorias = {
    'INCLUDE': 'Reservada',
    'USING': 'Reservada',
    'NAMESPACE': 'Reservada',
    'STD': 'Reservada',
    'COUT': 'Reservada',
    'CIN': 'Reservada',
    'GET': 'Reservada',
    'RETURN': 'Reservada',
    'VOID': 'Reservada',
    'INT': 'Reservada',
    'ENDL': 'Reservada',
    'SI': 'Reservada',
    'SINO': 'Reservada',
    'MIENTRAS': 'Reservada',
    'PARA': 'Reservada',
}

reservada = tuple(categorias.keys())

tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'NUMERO',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'CADENA',
    'MAYORDER',
    'MAYORIZQ',
)

# Reglas de expresiones regulares para tokens de contexto simple
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2}|\^)'
t_ASIGNAR = r'='
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
t_PUNTO = r'\.'

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Definición de palabras reservadas y otros tokens complejos
def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_VOID(t):
    r'void'
    return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reservada:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = ' \t'

def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Nueva prueba para tabla de resultados
def prueba2(data):
    global resultado_tabla

    analizador = lex.lex()
    analizador.input(data)

    resultado_tabla.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        categoria = categorias.get(tok.type, '')
        resultado = {
            "Identificador": tok.value,
            "Simbolo": categoria,
            "Token": tok.type,
            "Número de línea": tok.lineno,
            "Palabra reservada": 'X' if tok.type in categorias and categorias[tok.type] == 'Reservada' else '',
            "Número": 'X' if tok.type == 'ENTERO' else '',
            "Llave izquierda": 'X' if tok.type == 'LLAIZQ' else '',
            "Llave derecha": 'X' if tok.type == 'LLADER' else '',
            "Paréntesis izquierdo": 'X' if tok.type == 'PARIZQ' else '',
            "Paréntesis derecho": 'X' if tok.type == 'PARDER' else '',
            "Punto y coma": 'X' if tok.type == 'PUNTOCOMA' else '',
        }
        resultado_tabla.append(resultado)
    return resultado_tabla

# Nueva prueba para conteo de tokens
def contar_tokens(data):
    global conteo_tokens

    analizador = lex.lex()
    analizador.input(data)

    conteo_tokens.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        tipo = tok.type
        if tipo in conteo_tokens:
            conteo_tokens[tipo] += 1
        else:
            conteo_tokens[tipo] = 1
    return conteo_tokens

# Instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        print("Prueba:")
        print(prueba(data))
        print("Prueba 2:")
        print(prueba2(data))
        print("Conteo de Tokens:")
        print(contar_tokens(data))
