import lex  # Importa o módulo lex para construir o analisador léxico

# Dicionário de palavras reservadas e seus tipos
reserved = {
   'int' : 'RESERVED_WORD_INT',
   'float' : 'RESERVED_WORD_FLOAT',
   'char' : 'RESERVED_WORD_CHAR',
   'boolean' : 'RESERVED_WORD_BOOLEAN',
   'void' : 'RESERVED_WORD_VOID',
   'if' : 'RESERVED_WORD_IF',
   'else' : 'RESERVED_WORD_ELSE',
   'while' : 'RESERVED_WORD_WHILE',
   'scanf' : 'RESERVED_WORD_SCANF',
   'println' : 'RESERVED_WORD_PRINTLN',
   'main' : 'RESERVED_WORD_MAIN',
   'return' : 'RESERVED_WORD_RETURN',
   'struct' : 'RESERVED_WORD_STRUCT'
}

# Lista de tipos de tokens, incluindo palavras reservadas
tokens = [
    'ID',
    'NUM_INT',
    'OPERADOR',
    'TEXTO',
    'SPECIAL',
    'NUM_DEC'
 ] + list(reserved.values())

# Define os caracteres a serem ignorados (espaço e tabulação)
t_ignore  = ' \t'

# Define a regra para ignorar comentários no formato // até o final da linha
t_ignore_COMMENT = '//.*'

# Função para reconhecer identificadores (IDs)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Verifica se a palavra é reservada
    return t

# Expressões regulares para tokens
t_NUM_INT = r'\d+'
t_NUM_DEC = r'\d+\.\d+'
t_OPERADOR = r'\=|\+|\-|\*|\/(?!\/)|\%|\&\&|\=|\|\||\!|\>|\>\=|\<|\<\=|\!\=|\=\='
t_SPECIAL = r'\(|\)|\{|\}|\;|\,|\.|\[|\]'
t_TEXTO = r'".*"'

# Define uma regra para contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Cria o analisador léxico
lexer = lex.lex()

# Exemplo de uso
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

# Alimenta o analisador léxico com o trecho de código
lexer.input(code_snippet)

# Imprime os tokens gerados pelo analisador léxico
for token in lexer:
    print(token)
