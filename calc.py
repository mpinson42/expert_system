import inspect

def verbose(text):
    if verboseEnabled:
        print text

def is_number(str):
    if str.find('+') != -1:
        verbose("token {0} is a operator".format(str))
        return False
    if str.find('|') != -1:
        verbose("token {0} is a operator".format(str))
        return False
    if str.find('!') != -1:
        verbose("token {0} is a operator".format(str))
        return False
    if str.find('>') != -1:
        verbose("token {0} is a operator".format(str))
        return False
    if str.find('(') != -1:
        verbose("token {0} is a operator".format(str))
        return False
    if str.find(')') != -1:
        verbose("token {0} is a operator".format(str))
        return False    
    verbose("token {0} is a parameter".format(str))
    return True
 
def peek(stack):
    return stack[-1] if stack else None
 
def apply_operator(operators, values):
    verbose(values)
    verbose(operators)
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
    verbose(tokens)
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
    verbose("value:\t\t{0}".format(values))
    verbose("operators:\t{0}".format(operators))
    verbose("tokens:\t\t{0}".format(tokens))
 
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
        return error_found("Symbol {0} doesn't exits".format(symbol))
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
        verbose("Symbol: {0} has been added and is stated as true.".format(symbol))
    else:
        values["state_true"].append(False)
        values["state_false"].append(False)
        verbose("Symbol: {0} has been added and is NOT stated as true.".format(symbol))

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
        return error_found("Symbol {0} doesn't exits".format(symbol))
    index = values["name"].index(symbol)
    if values["state_true"][index] and values["state_false"][index]:
        error_found("Paradox found")
        return False
    if values["state_true"][index]:
        return True
    if not values["state_true"][index]:
        return False

def getIsTrueStateFromDictionary(symbol):
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
        return error_found("Symbol {0} doesn't exits".format(symbol))
    index = values["name"].index(symbol)
    return values["state_true"][index]

def getIsFalseStateFromDictionary(symbol):
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
        return error_found("Symbol {0} doesn't exits".format(symbol))
    index = values["name"].index(symbol)
    return values["state_false"][index]

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
        return error_found("Symbol {0} doesn't exits".format(symbol))
    index = values["name"].index(symbol)
    if values["state_true"][index] or values["state_false"][index]:
        return True

def andOperation(lhs, rhs):
    return (getLogicalStateFromDictionary(lhs) and getLogicalStateFromDictionary(rhs))

def orOperation(lhs, rhs):
    return (getLogicalStateFromDictionary(lhs) or getLogicalStateFromDictionary(rhs))

def notOperation(rhs):
    verbose("Do operation:\n\toperator: !, rhs: {0}".format(rhs))
    if getLogicalStateFromDictionary(rhs):
        verbose("\tResult = false")
        return "false"
    else:
        verbose("\tResult = true")
        return "true"

def doOperation(operator, lhs, rhs):
    verbose("Do operation:\n\toperator: {0}, lhs: {1}, rhs: {2}".format(operator, lhs, rhs))
    if (operator == '+'):
        if (andOperation(lhs,rhs)):
            verbose("\tResult = true")
            return ("true")
        else:
            verbose("\tResult = false")
            return ("false")
    if (operator == '|'):
        if (orOperation(lhs,rhs)):
            verbose("\tResult = true")
            return ("true")
        else:
            verbose("\tResult = false")
            return ("false")

def addListToDictionaryAsTrue(symbols):
    for symbol in symbols:
        addToDictionary(symbol, True)

def addListToDictionary(symbols):
    for symbol in symbols:
        addToDictionary(symbol, False)

def orOperationSymplification(lhs, rhs):
    verbose("Syplification of:\n\toperator: |, lhs: {0}, rhs: {1}".format(lhs, rhs))
    if (lhs == 'true' or rhs == 'true'):
        verbose("\tSymplified statement: true")
        return 'true'
    if (lhs == 'false' and rhs == 'false'):
        verbose("\tSymplified statement: false")
        return 'false'
    if (lhs == 'false'):
        verbose("\tSymplified statement: {0}".format(rhs))
        return rhs
    if (rhs == 'false'):
        verbose("\tSymplified statement: {0}".format(lhs))
        return lhs
    verbose("\tUnsimplifiable")
    return (lhs + " | " + rhs)

def andOperationSymplification(lhs, rhs):
    verbose("\tSyplification of:\n\toperator: +, lhs: {0}, rhs: {1}".format(lhs, rhs))
    if (lhs == 'true' and rhs == 'true'):
        verbose("\tSymplified statement: true")
        return 'true'
    if (lhs == 'false' or rhs == 'false'):
        verbose("\tSymplified statement: false")
        return 'false'
    if (lhs == 'true'):
        verbose("\tSymplified statement: {0}".format(rhs))
        return rhs
    if (rhs == 'true'):
        verbose("\tSymplified statement: {0}".format(lhs))
        return lhs
    verbose("\tUnsimplifiable")
    return (lhs + " + " + rhs)

def notOperationSymplification(rhs):
    verbose("Syplification of:\n\toperator: !, rhs: {0}".format(rhs))
    if (rhs == 'true'):
        verbose("Symplified statement: false")
        return 'false'
    if (rhs == 'false'):
        verbose("Symplified statement: true")
        return 'true'
    verbose("Unsimplifiable")
    return ('! ' + rhs)


def doOperationSymplification(operator, lhs, rhs):
    verbose("operator symplification: {0}, lhs: {1}, rhs: {2}".format(operator, lhs, rhs))
    if (operator == '+'):
        return (andOperationSymplification(lhs,rhs))
    if (operator == '|'):
        return (orOperationSymplification(lhs,rhs))

def apply_operation_simplification(operators, values):
    verbose(values)
    verbose(operators)
    operator = operators.pop()

    right = values.pop()
    if operator != '!':
        left = values.pop()
        values.append(doOperationSymplification(operator, left, right))
    else:
        values.append(notOperationSymplification(right))

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
    verbose("simplifiedExpression is: {0}".format(expression_cpy))
    values = []
    operators = []
    for token in expression_cpy:
        if is_number(token):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operation_simplification(operators, values)
                top = peek(operators)
            operators.pop()
        else:
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operation_simplification(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operation_simplification(operators, values)
    finalValue = []
    for value in values:
        for token in value.split(" "):
            finalValue.append(token)
    verbose("value:\t\t{0}".format(finalValue))
    verbose("operators:\t{0}".format(operators))
    verbose("tokens:\t\t{0}".format(tokens))
 
    return finalValue

def applyInferences(symplifiedExpression):
    symbol = symplifiedExpression.pop()
    if (is_number(symbol)):
        verbose("\t{0} is true".format(symbol))
        editDictionary(symbol, True, getIsFalseStateFromDictionary(symbol))
    if (symbol == '!'):
        nextSymbol = symplifiedExpression.pop()
        if (is_number(nextSymbol)):
            editDictionary(nextSymbol, getIsTrueStateFromDictionary(nextSymbol), True)
            verbose("\t{0} is false".format(nextSymbol))

def infer(evaluatedExpression, symplifiedExpression):
    verbose(evaluatedExpression)
    verbose(symplifiedExpression)
    if (evaluatedExpression != 'true'):
        verbose("Nothing to infer")
        return
    verbose("inference Possible")
    if ('|' in symplifiedExpression):
        verbose("No conclusion can be made")
        return
    symplifiedExpression.reverse()
    verbose(symplifiedExpression)
    while peek(symplifiedExpression) is not None:
        applyInferences(symplifiedExpression)

def printDictionary(asVerbose):
    i = 0
    for name in values["name"]:
        chain = None
        if (values["state_true"][i] and values["state_false"][i]):
            chain = "Paradox"
        elif (not values["state_true"][i] and not values["state_false"][i]):
            chain = "False (unexplicitly)"
        elif (values["state_true"][i]):
            chain = "True"
        else:
            chain = "False"
        if asVerbose:
            verbose("{0} is {1}".format(name, chain))
        else:
            print("{0} is {1}".format(name, chain))
        i += 1

def main():
    addToDictionary('A', True)
    addToDictionary('B', False)
    addToDictionary('E', False)
    addToDictionary('G', False)
    expression = "A | ! B > E + G"
    print expression
    expressionsides = expression.split(" > ")
    verbose(expressionsides)
    expressionLeftSide = expressionsides[0]
    expressionRightSide = expressionsides[1]
    verbose("Evaluating")
    evaluatedExpressionResult = evaluate(expressionLeftSide)
    symplifiedExpression = simplifyExpression(expressionRightSide)
    verbose(symplifiedExpression)
    infer(evaluatedExpressionResult, symplifiedExpression)
    printDictionary(False)

values = {"name":[], "state_true": [], "state_false": []}
verboseEnabled = True

if __name__ == '__main__':
    main()