import abc

class Car(object):

    __metaclass__ = abc.ABCMeta

    principalElements = ["Rodas", "Volante", "Bancos", "Estrutura mecanica"]

    @abc.abstractmethod
    def get_Type(self):
        """Return the type of the car"""

    @classmethod
    @abc.abstractmethod
    def get_Elements(cls):
        """Return the elements of the car"""
        return cls.principalElements


class Chevrolet(Car):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.uniqueElements = []

    def addElements(self, element):
        self.uniqueElements.append(element)

    def get_Elements(self):
        return self.uniqueElements + super(Chevrolet, self).get_Elements()

    def get_Original_Elements(self):
        return self.uniqueElements

    def get_Type(self):
        return self.type

    @staticmethod
    def get_Name(name):
        return "O nome do carro eh " + str (name)


a = Chevrolet("Tel", "Onix")
a.addElements("direcao hidraulica")
a.addElements("ar-condicionado")
a.addElements("vidros eletricos")

print(a.get_Name("Alexandra"))

print(a.get_Original_Elements())

print(a.get_Type())

print(a.get_Elements())

print(Chevrolet.get_Type())