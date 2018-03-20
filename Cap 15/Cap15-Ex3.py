class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        """Calculates the slope from the origin"""
        if self.x == 0:
            return None
        else:
            return self.y/self.x


q = Point(4, 10)
error = Point(0, 5)

print(q.slope_from_origin(), error.slope_from_origin())