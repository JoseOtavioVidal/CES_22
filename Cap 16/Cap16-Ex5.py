class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def colision(self, ret):
        """Analyses if ther is a collision with other rectangle"""
        if self.corner.x <= ret.corner.x and self.corner.y <= ret.corner.y:
            if self.corner.x + self.width >= ret.corner.x and self.corner.y + self.height >= ret.corner.y:
                return True
            else:
                return False
        elif self.corner.x <= ret.corner.x and self.corner.y > ret.corner.y:
            return False
        elif self.corner.x > ret.corner.x and self.corner.y <= ret.corner.y:
            return False
        else:
            if self.corner.x < ret.corner.x + ret.width and self.corner.y <= ret.corner.y + ret.height:
                return True
            else:
                return False

a = Rectangle(Point(-3,5), 50, 50)
b = Rectangle(Point(0, 0), 2, 2)

print(a.colision(b))