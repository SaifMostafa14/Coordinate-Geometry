class coordinate(object):
    def __init__(self, x, y):  # the special method (__init__) is often used with-
        self.x = x  # classes and it takes 3 parameters (self, x, y)
        self.y = y  # the x and y are the two coordinate values for example
        # the self represents a particular instance of the class

    def distance(self, other):
        diff_X_sq = (self.x - other.x) ** 2
        diff_Y_sq = (self.y - other.y) ** 2
        return (diff_X_sq + diff_Y_sq) ** 0.5

    def slope(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        return (diff_y / diff_x)

    def y_intercept(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        m = (diff_y / diff_x)
        return (self.y - (m*self.x))
    
    def midpoint (self, other):
        mid_x = int((self.x + other.x)/2)
        mid_y = int((self.y + other.y)/2)

        return ("("+str(mid_x)+","+str(mid_y)+")")

    def equation (self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        m = float((diff_y / diff_x))
        b = float(self.y - (m*self.x))
        if m == 1:
            if b == 0:
                return ("y = "+ "x")
            else:
                return ("y = "+ "x + " + str(b))
        elif b == 0:
            return ("y = "+ str(m) + "x ")
        else:
            return ("y = "+ str(m) + "x + " + str(b))
        
    def __str__(self):  # define what to do when you print the object you created
        return "<" + str(self.x) + "," + str(self.y) + ">"  # always return a string

# distance .... slope .... y-intercept .... midpoint .... equation ....





