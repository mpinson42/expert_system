def is_number(str):
    if str.find('+') != -1:
        return False
    if str.find('|') != -1:
        return False
    if str.find('>') != -1:
        return False
    if str.find('(') != -1: 
        return False
    if str.find(')') != -1:
        return False    
    print ("token {0} is a parameter".format(str))
    return True
#    try:    
#        return True
#    except ValueError:
#        return False
 
def peek(stack):
    return stack[-1] if stack else None
 
def apply_operator(operators, values):
    operator = operators.pop()
    values += operator
#    right = values.pop()
#    left = values.pop()
#    values.append(eval("{0}{1}{2}".format(left, operator, right)))
 
def greater_precedence(op1, op2):
    precedences = {'+' : 1, '|' : 2, '>' : 0}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    tokens = expression.split(" ")
    print tokens
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop()
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    print ("value:\t\t{0}".format(values))
    print ("operators:\t{0}".format(operators))
    print ("tokens:\t\t{0}".format(tokens))
    while peek(operators) is not None:
        apply_operator(operators, values)
 
    return values[0]

def main():
    expression = 'Z | ( A + B ) > E'
    evaluate(expression)
    #print("Shunting Yard Algorithm: {0}".format(evaluate(expression)))
    #print("Python: {0}".format(eval(expression)))
 
if __name__ == '__main__':
    main()