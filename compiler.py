import sys
import pprint
import ply.lex as lex
import ply.yacc as yacc


# Lista de tokens
tokens = (
    'ID',
    'INT_TYPE',
    'FLOAT_TYPE',
    'BOOL_TYPE',
    'INT',
    'FLOAT',
    'BOOL',
    'COLON',
    'EQUALS',
    'ARROW',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'DEF',
    'RETURN',
    'IF',
    'ELSE',
    'READ',
    'WRITE',
    'MAIN',  # Adicionei MAIN como um token
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQ',
    'NEQ',
    'LT',
    'LE',
    'GT',
    'GE',
)

# Expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_COLON = r':'
t_EQUALS = r'='
t_ARROW = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

# Tokens com ações associadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratamento de palavras-chave
reserved = {
    'int': 'INT_TYPE',
    'float16': 'FLOAT_TYPE',
    'bool': 'BOOL_TYPE',
    'def': 'DEF',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'read': 'READ',
    'write': 'WRITE',
    'true': 'BOOL',
    'false': 'BOOL',
    'MAIN': 'MAIN',  # Adicionei MAIN como palavra-chave
}

# Ignorar espaços em branco e comentários
t_ignore = ' \t'

# Tratamento de comentários // (adicionado)
def t_comment(t):
    r'//.*'
    pass  # Ignora comentários

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Análise sintática
def p_program(p):
    """program : declarations functions main"""
    p[0] = ('program', p[1], p[2], p[3])

def p_declarations(p):
    """declarations : declarations declaration
                   | """
    if len(p) > 1:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_declaration(p):
    """declaration : ID COLON type EQUALS expression SEMICOLON"""
    p[0] = ('declaration', p[1], p[3], p[5])

def p_type(p):
    """type : INT_TYPE
            | FLOAT_TYPE
            | BOOL_TYPE"""
    p[0] = p[1]

# Outras regras de produção (funções, expressões, etc.) devem ser definidas aqui
def p_functions(p):
    """functions : functions function
                 | function"""
    if len(p) > 2:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_function(p):
    """function : DEF ID LPAREN parameters RPAREN ARROW type block"""
    p[0] = ('function', p[2], p[4], p[7])

def p_parameters(p):
    """parameters : parameters COMMA parameter
                  | parameter
                  | """
    if len(p) > 1:
        if len(p) > 2:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[1]]
    else:
        p[0] = []

def p_parameter(p):
    """parameter : ID COLON type"""
    p[0] = ('parameter', p[1], p[3])

def p_block(p):
    """block : LBRACE declarations statements RBRACE"""
    p[0] = ('block', p[2], p[3])

def p_error(p):
    pass

# Definição de regra de produção para 'main'
def p_main(p):
    """main : DEF MAIN LPAREN RPAREN ARROW INT_TYPE block"""
    p[0] = ('main', p[7])

def p_statements(p):
    """statements : statements statement
                  | statement
                  | """
    if len(p) > 1:
        if len(p) > 2:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]
    else:
        p[0] = []

def p_statement(p):
    """statement : expression SEMICOLON"""
    p[0] = ('statement', p[1])

def p_expression(p):
    """expression : ID
                  | INT
                  | FLOAT
                  | BOOL"""
    p[0] = ('expression', p[1])

def p_expression_arithmetic(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    p[0] = ('binary_operation', p[2], p[1], p[3])

def p_expression_comparison(p):
    """expression : expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression"""
    p[0] = ('comparison', p[2], p[1], p[3])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"USO: python3 {sys.argv[0]} arquivo_de_codigo.cpy")
    else:
        cod = sys.argv[1]
        # Leitura do código a partir de um arquivo
        with open(cod, "r") as file:
            code = file.read()

        # Construção do parser
        parser = yacc.yacc()

        # Análise do código
        result = parser.parse(code)

        # Impressão da árvore de análise
        pprint.pprint(result)
