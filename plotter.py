import turtle

# Plot class to define bounds of function and interval
class Plot:
    accuracy = 500

    def __init__(self, xmin, xmax, ymin=None, ymax=None):
        self.xmin = xmin
        self.xmax = xmax
        if ymin == None:
            self.ymin = xmin
        else:
            self.ymin = ymin
        if ymax == None:
            self.ymax = xmax
        else:
            self.ymax = ymax
        self.xint = (xmax - xmin) / self.accuracy

    def setup(self, interval):
        turtle.setup(1.25*(abs(self.xmin) + abs(self.xmax)), 1.25*(abs(self.ymin) + abs(self.ymax)))
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(self.xmin, self.ymin)
        turtle.pendown()
        turtle.goto(self.xmin, self.ymax)
        turtle.goto(self.xmax, self.ymax)
        turtle.goto(self.xmax, self.ymin)
        turtle.goto(self.xmin, self.ymin)
        turtle.penup()
        turtle.goto(self.xmin, 0)
        turtle.pendown()
        turtle.goto(self.xmax, 0)
        turtle.penup()
        turtle.goto(0, self.ymin)
        turtle.pendown()
        turtle.goto(0, self.ymax)
        size = 200
        xnow = size
        while xnow > -size:
            turtle.penup()
            turtle.goto(xnow, 0)
            turtle.pendown()
            turtle.goto(xnow, size/50)
            turtle.goto(xnow, -size / 50)
            turtle.penup()
            xnow -= size / interval
        ynow = size
        while ynow > -size:
            turtle.penup()
            turtle.goto(0, ynow)
            turtle.pendown()
            turtle.goto(size/50, ynow)
            turtle.goto(-size / 50, ynow)
            turtle.penup()
            ynow -= size / interval

def drawfunction(table):
    size = 200
    table = rescale(table, size).__iter__()
    point = table.__next__()
    turtle.penup()
    if point.yvalue != None:
        turtle.goto(point.xvalue, point.yvalue)
    while point != None:
        if point.yvalue == None or abs(point.yvalue) > size:
            point = table.__next__()
            continue
        turtle.goto(point.xvalue, point.yvalue)
        turtle.pendown()
        point = table.__next__()

def rescale(table, size):
    table.evalvself()
    difference = abs(table.first - table.last)
    scale = 2 * size / difference
    lst = table.instances
    for i in lst:
        i.xvalue *= scale
        if i.yvalue != None:
            i.yvalue *= scale
    table.instances = lst
    return table
