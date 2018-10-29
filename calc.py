import inspect

def is_number(str):
    if str.find('+') != -1:
        return False
    if str.find('|') != -1:
        return False
    if str.find('!') != -1:
        return False
    if str.find('>') != -1:
        return False
    if str.find('(') != -1: 
        return False
    if str.find(')') != -1:
        return False    
    print ("token {0} is a parameter".format(str))
    return True
 
def peek(stack):
    return stack[-1] if stack else None
 
def apply_operator(operators, values):
    print values
    print operators
    operator = operators.pop()

    right = values.pop()
    if operator != '!':
        left = values.pop()
        values.append(doOperation(operator, left, right))
    else:
        values.append(notOperation(right))
 
def greater_precedence(op1, op2):
    precedences = {'!': 3, '+' : 2, '|' : 1, '>' : 0}
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
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)
    print ("value:\t\t{0}".format(values))
    print ("operators:\t{0}".format(operators))
    print ("tokens:\t\t{0}".format(tokens))
 
    return values[0]

def error_found():
    print ("error :" + inspect.stack()[1][3])

def error_found(error_complement):
    print ("error in " + inspect.stack()[1][3] + ": " + error_complement)

def editDictionary(symbol, isTrue, isFalse):
    symbolFound = False
    for name in values["name"]:
        if (name == symbol):
            symbolFound = True
            break
    if not symbolFound:
        return error_found("Symbol doesn't exits")
    index = values["name"].index(symbol)
    if isTrue:
        values["state_true"][index] = True
    if isFalse:
        values["state_false"][index] = True

def addToDictionary(symbol, isTrue):
    symbolFound = False
    for name in values["name"]:
        if (name == symbol):
            symbolFound = True
            break
    if symbolFound:
        return error_found("symbol already exist")
    values["name"].append(symbol)
    if isTrue:
        values["state_true"].append(True)
        values["state_false"].append(False)
        print "Symbol: {0} has been added and is stated as true.".format(symbol)
    else:
        values["state_true"].append(False)
        values["state_false"].append(False)
        print "Symbol: {0} has been added and is NOT stated as true.".format(symbol)

def getLogicalStateFromDictionary(symbol):
    if (symbol == 'true'):
        return True
    elif (symbol == 'false'):
        return False
    symbolFound = False
    for name in values["name"]:
        if (name == symbol):
            symbolFound = True
            break
    if not symbolFound:
        return error_found("Symbol doesn't exits")
    index = values["name"].index(symbol)
    if values["state_true"][index] and values["state_false"][index]:
        error_found("Paradox found")
        return False
    if values["state_true"][index]:
        return True
    if not values["state_true"][index]:
        return False

def isLogicalStateFromDictionaryStated(symbol):
    if (symbol == 'true'):
        return True
    elif (symbol == 'false'):
        return False
    symbolFound = False
    for name in values["name"]:
        if (name == symbol):
            symbolFound = True
            break
    if not symbolFound:
        return error_found("Symbol doesn't exits")
    index = values["name"].index(symbol)
    if values["state_true"][index] or values["state_false"][index]:
        return True

def andOperation(lhs, rhs):
    return (getLogicalStateFromDictionary(lhs) and getLogicalStateFromDictionary(rhs))

def orOperation(lhs, rhs):
    return (getLogicalStateFromDictionary(lhs) or getLogicalStateFromDictionary(rhs))

def notOperation(rhs):
    if getLogicalStateFromDictionary(rhs):
        return "false"
    else:
        return "true"

def doOperation(operator, lhs, rhs):
    print "operator: {0}, lhs: {1}, rhs: {2}".format(operator, lhs, rhs)
    if (operator == '+'):
        if (andOperation(lhs,rhs)):
            return ("true")
        else:
            return ("false")
    if (operator == '|'):
        if (orOperation(lhs,rhs)):
            return ("true")
        else:
            return ("false")

def addListToDictionaryAsTrue(symbols):
    for symbol in symbols:
        addToDictionary(symbol, True)

def addListToDictionary(symbols):
    for symbol in symbols:
        addToDictionary(symbol, False)

def simplifyExpression (expression):
    tokens = expression.split(" ")
    expression_cpy = list()
    for symbol in tokens:
        if (is_number(symbol)):
            if (isLogicalStateFromDictionaryStated(symbol) == True):
                if getLogicalStateFromDictionary(symbol):
                    expression_cpy.append("true")
                else:
                    expression_cpy.append("false")
            else:
                expression_cpy.append(symbol)
        else:
            expression_cpy.append(symbol)
    print "simplifiedExpression is: {0}".format(expression_cpy)


def main():
    addToDictionary('Z', False)
    addToDictionary('A', True)
    addToDictionary('B', False)
    addToDictionary('E', False)
    addToDictionary('F', True)
    addToDictionary('G', False)
    editDictionary('E', False, True)
    expression = "( ! Z + A | B ) > E" # + F | G"
    expressionsides = expression.split(" > ")
    print expressionsides
    expressionLeftSide = expressionsides[0]
    expressionRightSide = expressionsides[1]
    print "Evaluating"
    evaluate(expressionLeftSide)
    simplifyExpression(expressionRightSide)
    print values

values = {"name":[], "state_true": [], "state_false": []}

if __name__ == '__main__':
    main()