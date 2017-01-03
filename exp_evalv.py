class null:
    # The empty object
    def __repr__(self):
        return 'nil'

    def __str__(self):
        return 'nil'

nil = null()

class Tree:
    def __init__(self, root, left=nil, right=nil):
        self.root = root
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is not nil and self.right is not nil:
            return "Tree(" + str(self.root) + ", ["  + str(self.left) + ", " + str(self.right) + "])"
        else:
            return "Tree(" + str(self.root) + ")"


symbols = ["-", "+", "/", "*", "^"]

def isoperator(symbol):
    if symbol in symbols:
        return True
    return False

class operator:

    def __init__(self, symbol):
        assert isoperator(symbol)
        self.symbol = symbol

    def __repr__(self):
        return self.symbol

    def apply(self, left, right):
        assert isinstance(left, float)
        assert isinstance(right, float)
        if self.symbol == "+":
            return left + right
        elif self.symbol == "-":
            return left - right
        elif self.symbol == "*":
            return left * right
        elif self.symbol == "/":
            return left / right
        elif self.symbol == "^":
            return left ** right
        else:
            raise TypeError(self.symbol, " is not an operator")

class expression:

    def __init__(self, exp):
        if exp == "":
            self.first = nil
            self.rest = nil
        else:
            expression = self.remove_space(exp)
            self.first = expression[0]
            self.rest = nil
            if len(expression) > 1:
                self.rest = expression[1:]

    def remove_space(self, exp):
        no_space = ""
        for i in str(exp):
            if i != " ":
                no_space += i
        return no_space

    def __repr__(self):
        if self.rest is nil:
            return "nil"
        else:
            return self.first + self.rest

def string_to_tree(sequence):
    assert len(sequence) > 0
    sequence = check_variable(sequence)
    exp = expression(sequence)
    k = 0
    while k < len(symbols):
        result = keyfinder(exp, symbols[k])
        if isinstance(result, Tree):
            return result
        else:
            k += 1
    return Tree(sequence)

def keyfinder(sequence, key, left=""):
    if isinstance(sequence, null):
        return left
    sequence = expression(sequence)
    if sequence.first == "(":
        middle, sequence.rest = parantheses(sequence.rest)
        if sequence.rest == nil:
            sequence.rest = ""
        elif not isoperator(expression(sequence.rest).first):
            sequence.rest = "*" + sequence.rest
        if left != "":
            if not isoperator(left[-1]):
                left = left + "*"
        return string_to_tree(left + str(middle) + sequence.rest)
    elif sequence.first == key:
        return Tree(operator(sequence.first), string_to_tree(left), string_to_tree(sequence.rest))
    else:
        left = left + sequence.first
        return keyfinder(sequence.rest, key, left)

def parantheses(sequence, left="", innercount=0):
    sequence = expression(sequence)
    if sequence.first == "(":
        innercount += 1
    elif sequence.first == ")":
        if innercount == 0:
            return evalv_exp(left), sequence.rest
        else:
            innercount -= 1
    left = left + sequence.first
    return parantheses(sequence.rest, left, innercount)

def evalv_tree(tree):
    if isinstance(tree.root, operator):
        return tree.root.apply(evalv_tree(tree.left), evalv_tree(tree.right))
    else:
        return float(tree.root)

def check_variable(seq):
    assert isinstance(seq, str)
    if "e" in seq:
        seq = seq.replace("e", "2.718281828459045235360287471352662497757247093699959574966")
    elif "pi" in seq:
        seq = seq.replace("pi", "3.141592653589793238462643383279502884197169399375105820974")
    return seq

def evalv_exp(expression):
    return evalv_tree(string_to_tree(expression))