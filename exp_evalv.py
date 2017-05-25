from plotter import drawfunction, Plot
import turtle

# Null object
class null:
    def __repr__(self):
        return 'nil'

    def __str__(self):
        return 'nil'

# Makes sure there is only one instance of null
nil = null()

# Uses a tree to store operators, numbers, and maintain order of operation
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

# All available operators in reverse PEMDAS order
symbols = ["-", "+", "/", "*", "^"]

# Returns whether a symbol is an operator
def isoperator(symbol):
    if symbol in symbols:
        return True
    return False

# The operator class that makes the calculations
class operator:

    def __init__(self, symbol):
        assert isoperator(symbol)
        self.symbol = symbol

    def __repr__(self):
        return self.symbol

    def apply(self, left, right):
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
            raise SyntaxError(self.symbol, " is not an operator")

# The expression class. Midpoint between converting a string to a tree
class expression:

    def __init__(self, exp):
        if exp == "":
            self.first = nil
            self.rest = nil
        else:
            expression = self.remove_space(exp)
            self.first = expression[0]
            self.rest = nil
            self.exp = expression
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

    def isfunction(self):
        if self.exp[0:5] == "f(x)=":
            return True
        else:
            return False

#Converts a string to a tree for calculation
def string_to_tree(sequence):
    assert len(sequence) > 0
    sequence = check_variable(sequence)
    exp = expression(sequence)
    k = 0

    # Looks for in order of reverse PEMDAS
    while k < len(symbols):
        result = keyfinder(exp, symbols[k])
        if isinstance(result, Tree):
            return result
        else:
            k += 1

    # Returns the sequence, which should be a number, in a tree if not an operator
    return Tree(sequence)

#Checks for an operator in a sequence
def keyfinder(sequence, key, left=""):

    # Base case if the operator is not in the sequence
    if isinstance(sequence, null):
        return left
    sequence = expression(sequence)

    # Special case for parentheses
    if sequence.first == "(":
        # Evaluates inside of parentheses
        middle, sequence.rest = parentheses(sequence.rest)

        # Special case for empty rest
        if sequence.rest == nil:
            sequence.rest = ""

        # Implements implicit multiplication
        elif not isoperator(expression(sequence.rest).first):
            sequence.rest = "*" + sequence.rest
        if left != "" and left !="#":
            if not isoperator(left[-1]):
                left = left + "*"

        # Special case for negatives inside parentheses
        if middle < 0:
            middle = "#" + str(middle)[1:]

        return string_to_tree(left + str(middle) + sequence.rest)

    # If the function finds the key in the sequence
    elif sequence.first == key:
        if sequence.first == "-" and left == "":
            #Special case for negative numbers
            return string_to_tree("#" + sequence.rest)
        # Returns Tree object with operator as the root
        return Tree(operator(sequence.first), string_to_tree(left), string_to_tree(sequence.rest))
    else:
        #Iterates through the whole sequence
        left = left + sequence.first
        return keyfinder(sequence.rest, key, left)

# Evaluates the string inside a parentheses
def parentheses(sequence, left="", innercount=0):
    sequence = expression(sequence)

    # Special case for nested parentheses
    if sequence.first == "(":
        innercount += 1

    # Closing the parentheses while accounting for nested ones
    elif sequence.first == ")":
        if innercount == 0:
            return evalv_exp(left), sequence.rest
        else:
            innercount -= 1
    left = left + sequence.first

    # Recursion to iterate through the string
    return parentheses(sequence.rest, left, innercount)

# Evaluates a tree and returns a number
def evalv_tree(tree):
    # Accounts for some negative numbers, denoted with a #
    if str(tree.root)[0] == "#":
        tree.root = "-" + tree.root[1:]

    # Applies the operator to the left and right branches
    if isinstance(tree.root, operator):
        return tree.root.apply(evalv_tree(tree.left), evalv_tree(tree.right))
    else:
        # Returns the root number if not an operators
        try:
            # If double negative
            if tree.root[0:2] == "-#" or tree.root[0:2] == "##" or tree.root[0:2] == "--":
                return float(tree.root[2:])
            return float(tree.root)

        # Handles an exception of unsupported symbols
        except Exception as e:
            raise SyntaxError("'" + tree.root + "' is not a number or recognized symbol")

# Replaces supported symbols with their number forms
def check_variable(seq):
    assert isinstance(seq, str)
    if "e" in seq:
        seq = seq.replace("e", "2.718281828459045235360287471352662497757247093699959574966")
    elif "pi" in seq:
        seq = seq.replace("pi", "3.141592653589793238462643383279502884197169399375105820974")
    return seq

# Point class to not break abstraction barriers
class Point:

    def __init__(self, xvalue, yvalue):
        self.xvalue = xvalue
        self.yvalue = yvalue

    def __repr__(self):
        return "Point({0}, {1})".format(self.xvalue, self.yvalue)

# Table class to not break abstraction barriers
class Table:

    def __init__(self):
        self.instances = []

    def addinst(self, point):
        self.instances.append(point)

    def evalvself(self):
        self.first = self.instances[0].xvalue
        self.last = self.instances[-1].xvalue

    def __repr__(self):
        return str(self.instances)

    def __len__(self):
        return len(self.instances)

    def __iter__(self):
        assert len(self.instances) > 0
        self.now = 0
        self.next = 1
        return self

    def __next__(self):
        if self.now == len(self.instances):
            return None
        point = self.instances[self.now]
        self.now, self.next = self.next, self.next + 1
        return point

# Evaluates a function with respect to x, returns a table
def function_evalv(sequence, plot):
    k = plot.accuracy
    xnow = plot.xmin
    table = Table()

    # Recalculates the function after subbing in a value for x, adds point to table
    while k >= 0:
        instance = sequence
        if "x" in instance:
            instance = instance.replace("x", "(" + "{0:.5f}".format(xnow) +")")
            k -= 1
            ypoint = evalv_exp(instance)
            if isinstance(ypoint, complex):
                table.addinst(Point(float("{0:.5f}".format(xnow)), None))
            else:
                table.addinst(Point(float("{0:.5f}".format(xnow)), float("{0:.5f}".format(ypoint))))
            xnow += plot.xint
            if k == 0.5 * plot.accuracy:
                xnow = 0
        else:
            # Raises exception where 'x' in not in the function
            raise SyntaxError("Function must have a 'x' value")
    return table

# General plot for now
plot = Plot(-10, 10)

# Decides if a string is an expression or function, then evaluates either
def evalv_exp(string):
    exp = expression.remove_space(expression(string), string)
    if exp[0:5] == "f(x)=":
        Plot(-150, 150).setup(10)
        drawfunction(function_evalv(exp[5:], plot))
        return "See Graph"
    elif exp[0:6] == "clear":
        turtle.clear()
        Plot(-150, 150).setup(10)
        return "Graph Cleared"
    else:
        return evalv_tree(string_to_tree(string))
