#--------------
#lexer.py
#
#lexer for math expressions
#
#--------------
import ply.lex as lex

tokens = (
    'NUMBER',
    'ADDITION',
    'SUBTRACTION',
    'MULTIPLICATION',
    'DIVISION',
    'POWER',
    'SQRT',
    'VARIABLE',
    'LPAREN',
    'RPAREN'
)


t_NUMBER = r'\d+(\.\d+)?'
t_ADDITION = r'\+'
t_SUBTRACTION = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_POWER = r'\^'
t_SQRT = r'sqrt'
t_VARIABLE = r'(?!sqrt)[a-zA-Z]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n\r\f\v'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def make_tokens(lexer, text):
    tokensList = []
    lexer.input(text)
    while True:
        token = lexer.token()
        if not token:
            break
        tokensList.append(token)
    return tokensList

if __name__ == "__main__":
    text = raw_input()
    tokensList = make_tokens(lexer, text)
    print(tokensList)
