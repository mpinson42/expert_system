priorityParenthesisOpenining = 1
priorityParenthesisClosing = 2
priorityLevelNot = 3
priorityLevelAnd = 4
priorityLevelOr = 5
priorityLevelXor = 6
priorityLevelImplication = -1

def checkForContradiction(stated_true_value_table, stated_false_value_table):
    paradoxDetected = False
    for stated_as_false in stated_false_value_table:
        for stated_as_true in stated_true_value_table:
            if (stated_as_true == stated_as_false):
                print(stated_as_false + " is a paradox")
                paradoxDetected = True
    return paradoxDetected

def isOperator(symbol):
    if '+' in symbol:
        print "and found"
        return priorityLevelAnd
    if '|' in symbol:
        print "or found"
        return priorityLevelOr
    if '^' in symbol:
        print "xor found"
        return priorityLevelXor
    if "=>" in symbol:
        print "implication found"
        return priorityLevelImplication
    if ">" in symbol:
        print "implication found"
        return priorityLevelImplication
    if "=" in symbol:
        print "implication found"
        return priorityLevelImplication
    if "!" in symbol:
        print "! found"
        return priorityLevelNot
    if "(" in symbol:
        print "( found"
        return priorityParenthesisOpenining
    if ")" in symbol:
        print ") found"
        return priorityParenthesisClosing
    return 0

###need to implement () management
def reversePolishNotation(premice):
    symbolsSplitedPremice = premice.split(" ")
    print symbolsSplitedPremice
    operatorStack = list()
    postfixList = list()
    for symbol in symbolsSplitedPremice:
        print "current symbol = " + symbol
        if (isOperator(symbol) == priorityLevelImplication):
            break
        currentSymbolValue = isOperator(symbol)
        if currentSymbolValue != 0:
            if (isOperator(currentSymbolValue) == priorityParenthesisOpenining):
                operatorStack+=symbol
            elif (isOperator(currentSymbolValue) == priorityParenthesisClosing):
                for symbolInOpStack in operatorStack:
                    print ""
            else:
                for symbolInOpStack in operatorStack:
                    print "symbolInOpStack val ="
                    print isOperator(symbolInOpStack)
                    print "symbol"
                    print isOperator(symbol)
                    if (isOperator(symbolInOpStack) < isOperator(symbol)):
                        postfixList += symbolInOpStack
                        operatorStack.remove(symbolInOpStack)
                operatorStack += symbol
                print postfixList
                continue
        postfixList += symbol
    for symbolInOpStack in operatorStack:
        postfixList += symbolInOpStack
    for symbolInOpStack in operatorStack:
        operatorStack.remove(symbolInOpStack)
    for symbolSelected in postfixList:
       symbolsSplitedPremice.remove(symbolSelected)
    print "\t" + symbol
    print "postfixList contains:"
    print postfixList
    print "operation stack contains:"
    print operatorStack
    print symbolsSplitedPremice
    return postfixList



def solveReversePolishNotation(revPolishPremice):
    print "solve expression"

def applyImplication(premice, stated_true_value_table, stated_false_value_table, searched_value_table):
    print "applying implication to " + premice
    revPolishPremice = reversePolishNotation(premice)


def solve(premice_table, stated_true_value_table, stated_false_value_table, searched_value_table):
#    checkForContradiction(stated_true_value_table, stated_false_value_table)

#   for premice in premice_table:
#        applyImplication(premice, stated_true_value_table, stated_false_value_table, searched_value_table)
    print "Solved"