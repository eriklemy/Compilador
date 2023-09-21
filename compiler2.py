import sys
import ply.lex as lex
import ply.yacc as yacc

# ANALISADOR LEXICO E SINTATICO - FASE 2

# Defina os tokens
tokens = (
    'ID',
    'FLOAT16',
    'INT',
    'BOOL',
    'IF',
    'ELSE',
    'RETURN',
    'DEF',
    'ARROW',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'PLUS',    # Adicione o token PLUS
    'MINUS',   # Adicione o token MINUS
)

# Regras para tokens simples
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_ARROW = r'\->'
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'


# Regra para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'true' or t.value == 'false':
        t.type = 'BOOL'
    elif t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    elif t.value == 'return':
        t.type = 'RETURN'
    elif t.value == 'def':
        t.type = 'DEF'
    elif t.value == 'print':
        t.type = 'PRINT'
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t

# Regra para números em ponto flutuante
def t_FLOAT16(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Regra para números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para comentários
def t_COMMENT(t):
    r'\/\/.*'
    pass

# Ignorar espaços em branco
t_ignore = ' \t\r\n'

# Função para capturar erros de token
def t_error(t):
    print(f"Token não reconhecido: '{t.value[0]}'")
    t.lexer.skip(1)

# Defina a gramática
def p_code(p):
    '''
    code : declarations functions
    '''

def p_declarations(p):
    '''
    declarations : declarations declaration
                | empty
    '''

def p_declaration(p):
    '''
    declaration : ID COLON ID ASSIGN expression SEMICOLON
    '''
    
precedence = (
    ('left', 'PLUS', 'MINUS'),
)

def p_expression(p):
    '''
    expression : ID
               | literal
               | expression PLUS expression
               | expression MINUS expression
               | LPAREN expression RPAREN
    '''

def p_literal(p):
    '''
    literal : FLOAT16
            | INT
            | BOOL
    '''

def p_functions(p):
    '''
    functions : functions function
              | empty
    '''

def p_function(p):
    '''
    function : DEF ID LPAREN args RPAREN ARROW ID COLON LBRACE statements RBRACE
    '''

def p_args(p):
    '''
    args : args_list
         | empty
    '''

def p_args_list(p):
    '''
    args_list : args_list COMMA arg
              | arg
    '''

def p_arg(p):
    '''
    arg : ID COLON ID
    '''

def p_statements(p):
    '''
    statements : statements statement
               | empty
    '''

def p_statement(p):
    '''
    statement : IF LPAREN expression RPAREN COLON LBRACE statements RBRACE ELSE COLON LBRACE statements RBRACE
              | RETURN expression SEMICOLON
    '''

def p_empty(p):
    '''
    empty :
    '''

# Função para capturar erros de sintaxe
def p_error(p):
    print(f"Erro de sintaxe na linha {p.lineno}: token '{p.value}'")


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print(f"USO: python3 {sys.argv[0]} arquivo_de_codigo.cpy")
    # else:
    #     cod = sys.argv[1]
    #     # Leitura do código a partir de um arquivo
    #     with open(cod, "r") as file:
    #         code = file.read()

        # Crie um analisador léxico e um analisador sintático
        lexer = lex.lex()
        parser = yacc.yacc()
        
        # Código de teste
        code = '''
        // Declara uma variável booleana
        ligado: bool = true;

        // Declara uma variável real
        num: int = 69;
        PI: float16 = 3.14159;

        def main() -> int: {
            if (ligado) : {
                return 1;
            } else: {
                return 0;
            }
            return 0;
        }

        def soma(a: float16, b: float16) -> float16: {
            return a + b;
        }
        '''
        # Análise do código
        result = parser.parse(code)
        print("Analisado com sucesso!")

