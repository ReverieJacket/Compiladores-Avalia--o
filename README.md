# Analisador Léxico e Sintático
Inicialmente foi utilizado java puro, nem mesmo o regex, para implementação. No entanto, como foi dado um segundo prazo para entrega, uma abordagem mais simples foi escolhida através do PLY (Python Lex-Yacc); ferramenta para gerar analisadores léxicos e sintáticos, sendo uma alternativa para Lex e Yacc tradicionais.
* lex.py foi retirado do repositório https://github.com/dabeaz/ply 

## Implementação
- O léxico está no arquivo lexer.py
- O sintático está no lexer-parser.py

## Exemplo de uso
- Abra o repositório no gitpod.io
- Para obter o pacote, execute o comando 'pip install ply' 
- Execute o comando 'python lexer.py' para testar o léxico
- Execute o comando 'python lexer-parser.py' para testar o sintático


