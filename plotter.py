class Plot:
    accuracy = 500

    def __init__(self):
        self.xmin = input("xmin: ")
        self.xmax = input("xmax: ")

    def __repr__(self):
        return str(self.xmin) + str(self.xmax)

