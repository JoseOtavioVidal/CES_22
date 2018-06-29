class AbstractInterface:

    """ Target interface.
 
    This is the target interface, that clients use.
    """
    def contagem(self, n):
        raise NotImplemented()

class Bridge(AbstractInterface):
    """ Bridge class.
     
    This class forms a bridge between the target
    interface and background implementation.
    """
    def __init__(self):
        self.__implementation = None

class Decimal(Bridge):
    """ Variant of the target interface.
 
    This is a variant of the target Abstract interface.
    It can do something little differently and it can
    also use various background implementations through
    the bridge.
    """
    def __init__(self, implementation):
        self.__implementation = implementation

    def contagem(self, n):
        modo = 'dec'
        print("Contagem em numeros decimais: ")
        self.__implementation.contar(n ,modo)

class Hexadecimal(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def contagem(self, n):
        modo = 'hex'
        print("Contagem em numeros  hexadecimais: ")
        self.__implementation.contar(n, modo)

class ImplementationInterface:
    """ Interface for the background implementation.
 
    This class defines how the Bridge communicates
    with various background implementations.
    """
    def contar(self, n, modo):
        raise NotImplemented

class Crescente(ImplementationInterface):

    """ Concrete background implementation.
 
    A variant of background implementation, in this
    case for Linux!
    """
    def contar(self, n, modo):
        for i in range(n):
            if modo == 'dec':
                print("{0} ".format(i))
            else:
                print("{0} ".format(hex(i)))

class Descrecente(ImplementationInterface):
    def contar(self, n, modo):
        for i in range(n, 0, -1):
            if modo == 'dec':
                print("{0} ".format(i))
            else:
                print("{0} ".format(hex(i)))

if __name__ == "__main__":
    n = 10
    descrecente = Descrecente()

    crescente = Crescente()
    # Couple of variants under a couple
    # of operating systems.
    decimal = Decimal(crescente)
    decimal.contagem(n)
    decimal = Decimal(descrecente)
    decimal.contagem(n)
    print("\nMudando a interface agora\n")
    hexa = Hexadecimal(crescente)
    hexa.contagem(n)
    hexa = Hexadecimal(descrecente)
    hexa.contagem(n)
