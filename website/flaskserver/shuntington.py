import re

def is_number(str):
    operators=['+', '-', '*', '/', '(', ')']
    return str not in operators
    '''
    try:
        int(str)
        return True
    except ValueError:
        return False
    '''
 
def is_name(str):
    return re.match("\w+", str)
 
def peek(stack):
    return stack[-1] if stack else None
 
def apply_operator(operators, values):
    print(operators)
    print(values)
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator=='/':
        values.append("\\frac{"+str(left)+"}{"+str(right)+"}")
    else:
        values.append("{0}{1}{2}".format(left, operator, right))
 
def greater_precedence(op1, op2):
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]
 
def evaluate(expression):
    tokens = re.findall("[+/*()-]|\w+", expression)
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
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)

    print(values)
    return values[0]
