class Shape:
    geometric_type = "Generic Shape"

    def area(self):
        raise NotImplementedError


    def gte_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        print("Plotting at {}, ratio {}". format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = "Polygon"

    isConvex = False


class RegularPolygon(Polygon):
    geometric_type = "Regular Polygon"
    isConvex = True

    def __init__(self, side):
        self.side = side

class IrregularPolygon(Polygon):
    geometric_type = "Irregular Polygon"
    isConvex = False


class AnusualHexagon(IrregularPolygon, RegularPolygon):
    geometric_type = "Anusual Hexagon"

    def area(self):
        return "It is not exist"


class OtherAnusualHexagon(RegularPolygon, IrregularPolygon):
    geometric_type = "Anusual Hexagon type 2"

    def area(self):
        return 1.5*(3**.5*self.side**2)

class RegularHexagon(RegularPolygon):
    geometric_type = "Regular Hexagon"

    def area(self):
        return 1.5*(3**.5*self.side**2)


class Square(RegularPolygon):
    geometric_type = "Square"

    def area(self):
        return self.side**2


hexagon = RegularHexagon(5)
print(hexagon.__class__.__mro__)
print(hexagon.geometric_type)
print(hexagon.area())

anusualHexagon = AnusualHexagon(5)
print(anusualHexagon.__class__.__mro__)
print(anusualHexagon.geometric_type)
print(anusualHexagon.area())

otherAnusualHexagon = OtherAnusualHexagon(5)
print(otherAnusualHexagon.__class__.__mro__)
print(otherAnusualHexagon.geometric_type)
print(otherAnusualHexagon.area())
