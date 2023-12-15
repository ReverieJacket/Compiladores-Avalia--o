import lex
from yacc import yacc

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'char' : 'CHAR',
   'boolean' : 'BOOLEAN',
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'return' : 'RETURN',
   'for' : 'FOR',
   'switch' : 'SWITCH',
   'case' : 'CASE',
   'default' : 'DEFAULT',
   'break' : 'BREAK',
   'continue' : 'CONTINUE',
   'struct' : 'STRUCT',
   'double' : 'DOUBLE' 
}

tokens = [
    'ID',
    'NUM_INT',
    'TEXTO',
    'NUM_DEC',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ATRIB',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'PERCENT',
    'AND',
    'OR',
    'COLON',
    'NOT',
    'GREATER',
    'LESS',
    'DOUBLE',
    'EQUAL',
    'GREATEREQUAL',
    'LESSEQUAL',
    'NOTEQUAL',
    'PLUSPLUS',
    'MINUSMINUS',
    'ARROW',
    'DOTDOTDOT'
    
 ] + list(reserved.values())

t_ignore  = ' \t'
t_ignore_COMMENT = '//.*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Regular expressions for tokens
t_NUM_INT = r'\d+'
t_NUM_DEC = r'\d+\.\d+'
t_PERCENT = r'\%'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_COLON = r'\:'
t_NOT = r'\!'
t_GREATER = r'\>'
t_LESS = r'\<'

t_TEXTO = r'".*"' 
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/(?!\/)'
t_ATRIB = r'\='
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_DOT = r'\.'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

import yacc
# 1. Declaração
def p_declaracao(p):
    '''declaracao : declaracao_variavel
                  | declaracao_funcao
                  | declaracao_estrutura'''

# 2. Declaração Variável
def p_declaracao_variavel(p):
    '''declaracao_variavel : tipo ID SEMICOLON
                           | tipo ID ATRIB expressao SEMICOLON'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | DOUBLE
            | CHAR
            | BOOLEAN'''

# 3. Declaração Função
def p_declaracao_funcao(p):
    'declaracao_funcao : tipo ID LPAREN parametros RPAREN bloco'

# 4. Parâmetros
def p_parametros(p):
    '''parametros : parametro
                  | parametro COMMA parametros'''

def p_parametro(p):
    '''parametro : tipo ID
                 | tipo ID LBRACKET RBRACKET
                 | tipo DOTDOTDOT ID'''

# 5. Bloco
def p_bloco(p):
    'bloco : LBRACE declaracoes RBRACE'

def p_declaracoes(p):
    '''declaracoes : declaracao
                   | declaracao declaracoes'''


# Estrutura de Controle
def p_estrutura_controle(p):
    '''estrutura_controle : IF LPAREN expressao RPAREN bloco
                          | IF LPAREN expressao RPAREN bloco ELSE bloco
                          | WHILE LPAREN expressao RPAREN bloco
                          | FOR LPAREN expressao SEMICOLON expressao SEMICOLON expressao RPAREN bloco
                          | SWITCH LPAREN expressao RPAREN case_lista
                          | BREAK SEMICOLON
                          | CONTINUE SEMICOLON
                          | RETURN expressao SEMICOLON'''

# Case Lista
def p_case_lista(p):
    '''case_lista : case_decl
                  | case_decl case_lista'''

# Case Declaração
def p_case_decl(p):
    '''case_decl : CASE expressao COLON bloco
                 | DEFAULT COLON bloco'''

# Declaração de Estrutura
def p_declaracao_estrutura(p):
    'declaracao_estrutura : STRUCT ID LBRACE declaracao_variavel RBRACE SEMICOLON'

# Array
def p_array(p):
    '''array : ID LBRACKET expressao RBRACKET
             | ID LBRACKET RBRACKET'''

# Inicialização de Array
def p_array_inicializacao(p):
    'array_inicializacao : LBRACE expressao_lista RBRACE'


# Expressão
def p_expressao(p):
    '''expressao : atribuicao
                 | expressao_logica'''

# Atribuição
def p_atribuicao(p):
    '''atribuicao : ID ATRIB expressao
                  | ID PLUS ATRIB expressao
                  | ID MINUS ATRIB expressao
                  | ID TIMES ATRIB expressao
                  | ID DIVIDE ATRIB expressao
                  | ID PERCENT ATRIB expressao
                  | ID AND ATRIB expressao
                  | ID OR ATRIB expressao'''

# Expressão Lógica
def p_expressao_logica(p):
    '''expressao_logica : expressao_relacional
                        | expressao_logica AND expressao_relacional
                        | expressao_logica OR expressao_relacional
                        | NOT expressao_relacional'''

# Expressão Relacional
def p_expressao_relacional(p):
    '''expressao_relacional : expressao_aritmetica
                            | expressao_aritmetica GREATER expressao_aritmetica
                            | expressao_aritmetica GREATEREQUAL expressao_aritmetica
                            | expressao_aritmetica LESS expressao_aritmetica
                            | expressao_aritmetica LESSEQUAL expressao_aritmetica
                            | expressao_aritmetica NOTEQUAL expressao_aritmetica
                            | expressao_aritmetica EQUAL expressao_aritmetica'''

# Expressão Aritmética
def p_expressao_aritmetica(p):
    '''expressao_aritmetica : expressao_multiplicativa
                            | expressao_aritmetica PLUS expressao_multiplicativa
                            | expressao_aritmetica MINUS expressao_multiplicativa'''

# Expressão Multiplicativa
def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                | expressao_multiplicativa TIMES expressao_unaria
                                | expressao_multiplicativa DIVIDE expressao_unaria
                                | expressao_multiplicativa PERCENT expressao_unaria'''

# Expressão Unária
def p_expressao_unaria(p):
    '''expressao_unaria : expressao_postfix
                        | MINUS expressao_unaria
                        | PLUSPLUS expressao_postfix
                        | MINUSMINUS expressao_postfix'''

# Expressão Postfix
def p_expressao_postfix(p):
    '''expressao_postfix : primaria
                         | primaria LBRACKET expressao RBRACKET
                         | primaria LPAREN argumentos RPAREN
                         | primaria DOT ID
                         | primaria ARROW ID'''

# Argumentos
def p_argumentos(p):
    '''argumentos : expressao_lista
                  | empty'''

# Primária
def p_primaria(p):
    '''primaria : ID
                | NUM_INT
                | NUM_DEC
                | TEXTO
                | LPAREN expressao RPAREN'''

# Expressão Lista
def p_expressao_lista(p):
    '''expressao_lista : expressao
                       | expressao_lista COMMA expressao'''

# Vazio
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type}), line {p.lineno}, column {find_column(p)}")
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

# Função auxiliar para encontrar a coluna do token na entrada
def find_column(token):
    last_cr = lexer.lexdata.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Example usage
code_snippet = '''
// Declaração de variável
int contador;
// Declaração de função com parâmetros e bloco
double calcularMedia(int numero1, float numero2){
	// Bloco com declarações e expressões
	double media;
	media = (numero1 + numero2) / 2;
	return media;
}
//Estrutura de controle com expressão lógica
if (contador > 10){
	contador = 0;
} else {
	contador += 1;
}
// Uso de expressão aritmética
int resultado;
resultado = 5 * (3 + 2);
//Declaração de uma estrutura
struct Ponto {
	int x;
	int y;
};
// Comentário de uma linha
// Inicialização de uma estrutura
struct Ponto ponto1 = {10,20};
'''

# Build the lexer
lexer = lex.lex()
# Example usage

lexer.input(code_snippet)

for token in lexer:
    print(token)

# Build the parser
parser = yacc.yacc()

result = parser.parse(code_snippet)


print(result)
