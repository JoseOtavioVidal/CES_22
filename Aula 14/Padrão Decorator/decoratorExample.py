class hexaComponent:
    def getDescription(self):
        if(self.__class__.__name__ == 'Team'):
            return ''
        else:
            return self.__class__.__name__

    def getPossibilityToHexa(self):
        return self.__class__.possibility

class Team(hexaComponent):
    possibility = 0.3

class Decorator(hexaComponent):
    def __init__(self, hexacomponent):
        self.component = hexacomponent

    def getPossibilityToHexa(self):
        return self.component.getPossibilityToHexa() + hexaComponent.getPossibilityToHexa(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + hexaComponent.getDescription(self)

class Neymar(Decorator):
    possibility = 0.15
    def __init__(self, hexacomponent):
        Decorator.__init__(self, hexacomponent)

class Coutinho(Decorator):
    possibility = 0.4
    def __init__(self, hexacomponent):
        Decorator.__init__(self, hexacomponent)

class Thiago_Silva(Decorator):
    possibility = 0.065
    def __init__(self, hexacomponent):
        Decorator.__init__(self, hexacomponent)

class Paulinho(Decorator):
    possibility = 0.045
    def __init__(self, hexacomponent):
        Decorator.__init__(self, hexacomponent)

class Taison(Decorator):
    possibility = 0.045
    def __init__(self, hexacomponent):
        Decorator.__init__(self, hexacomponent)

if __name__ == "__main__":
    possibility1 = Neymar(Coutinho(Team()))
    print("A chance do Brazil ganhar o hexa com esses jogadores {0} eh: {1}".format(possibility1.getDescription(),
                                                                                    possibility1.getPossibilityToHexa()))

    possibility2 = Thiago_Silva(Neymar(Coutinho(Paulinho(Team()))))
    print("A chance do Brazil ganhar o hexa com esses jogadores {0} eh: {1}".format(possibility2.getDescription(),
                                                                                    possibility2.getPossibilityToHexa()))

    possibility3 = Taison(Thiago_Silva(Neymar(Coutinho(Paulinho(Team())))))
    if possibility3.getPossibilityToHexa() > 1:
        print("O Hexa ja eh realidade com esses jogadores {0}".format(possibility3.getDescription()))
    else:
        print("A chance do Brazil ganhar o hexa com esses jogadores {0} eh: {1}".format(possibility3.getDescription(),
                                                                                    possibility3.getPossibilityToHexa()))