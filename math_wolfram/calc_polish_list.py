import math


def vars_to_nums(polish_list, var_dict):
    newPolishList = []
    for i, val in enumerate(polish_list):
        if(var_dict.get(val[0]) == None):
            newPolishList.append(polish_list[i])
            continue
        newPolishList.append((var_dict.get(val[0]), val[1]))

    return newPolishList

def calc_polish_list(polish_list):
    stack = []
    for i, val in enumerate(polish_list):
        value, count = val
        if(count == 0):
            stack.append(float(value))
            continue
        if val == ('+', 2):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2+op1)
            continue
        if val == ('-', 2):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2-op1)
            continue
        if val == ('*', 2):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2*op1)
            continue
        if val == ('/', 2):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2/op1)
            continue
        if val == ('^', 2):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(math.pow(op2,op1))
            continue
        if val == ('-', 1):
            op1 = stack.pop()
            stack.append(-1*op1)
            continue
        if val == ('sqrt', 1):
            op1 = stack.pop()
            stack.append(math.sqrt(op1))
            continue

    return stack.pop()
