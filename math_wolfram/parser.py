#-----------------------------------
#parser.py
#
#Create tree from tokens
#
#-----------------------------------
import ply.yacc as yacc
from lexer import tokens
from node import Node

def p_expression_subtraction(p):
    'expression : expression SUBTRACTION term'
    p[0] = Node(p[2], [p[1], p[3]])

def p_expression_addition(p):
    'expression : expression ADDITION term'
    p[0] = Node(p[2], [p[1], p[3]])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_division(p):
    'term : term DIVISION pow'
    p[0] = Node(p[2], [p[1], p[3]])

def p_term_multiplication(p):
    'term : term MULTIPLICATION pow'
    p[0] = Node(p[2], [p[1], p[3]])

def p_term_pow(p):
    'term : pow'
    p[0] = p[1]

def p_pow_power(p):
    'pow : pow POWER operator'
    p[0] = Node(p[2], [p[1], p[3]])

def p_pow_operator(p):
    'pow : operator'
    p[0] = p[1]

def p_operator_minus(p):
    'operator : SUBTRACTION num'
    p[0] = Node(p[1], [p[2]])

def p_operator_sqrt(p):
    'operator : SQRT num'
    p[0] = Node(p[1], [p[2]])

def p_operator_num(p):
    'operator : num'
    p[0] = p[1]

def p_num_number(p):
    'num : NUMBER'
    p[0] = p[1]

def p_num_variable(p):
    'num : VARIABLE'
    p[0] = p[1]

def p_num_expr(p):
    'num : LPAREN expression RPAREN'
    p[0] = Node(p[1], [p[2]])

parser = yacc.yacc()

def build_tree(expression):
    return parser.parse(expression)