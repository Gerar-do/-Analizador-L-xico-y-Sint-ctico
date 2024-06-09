import ply.yacc as yacc
from analizador_lexico import tokens

resultado_sintactico = []

def p_program(p):
    '''program : declaraciones'''
    p[0] = p[1]

def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaracion(p):
    '''declaracion : tipo IDENTIFICADOR PARIZQ PARDER bloque'''
    p[0] = ('declaracion', p[1], p[2], p[3], p[4], p[5])

def p_tipo(p):
    '''tipo : VOID'''
    p[0] = p[1]

def p_bloque(p):
    '''bloque : LLAIZQ instrucciones LLADER'''
    p[0] = ('bloque', p[2])

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_instruccion(p):
    '''instruccion : expresion PUNTOCOMA'''
    p[0] = p[1]

def p_expresion(p):
    '''expresion : IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ argumentos PARDER
                 | IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ PARDER'''
    if len(p) == 7:
        p[0] = ('metodo', p[1], p[2], p[3], p[4], p[5], p[6])
    else:
        p[0] = ('metodo', p[1], p[2], p[3], p[4], None, p[5])

def p_argumentos(p):
    '''argumentos : argumentos COMA argumento
                  | argumento'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_argumento(p):
    '''argumento : ENTERO
                 | NUMERO
                 | CADENA
                 | IDENTIFICADOR'''
    p[0] = p[1]

def p_error(p):
    global resultado_sintactico
    if p:
        error_msg = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
    else:
        error_msg = "Error de sintaxis en entrada vacía"
    resultado_sintactico.append(error_msg)

parser = yacc.yacc()

def prueba_sintactico(codigo):
    global resultado_sintactico
    resultado_sintactico = []
    parser.parse(codigo)
    if not resultado_sintactico:
        resultado_sintactico.append("Sintaxis correcta")
    return resultado_sintactico
