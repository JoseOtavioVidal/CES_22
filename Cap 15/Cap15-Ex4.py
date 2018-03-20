class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


    def get_line_to(self, q):
        if self.x != q.x:
            a = (self.y - q.y)/(self.x - q.x)
            b = self.y - a*self.x
            return (a, b)
        else:
            return None


p = Point(4, 11)

print(p.get_line_to(Point(6, 15)))