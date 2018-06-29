import abc
from time import sleep

class Context:

    def __init__(self, state):
         self._state = state

    def request(self):
         return self._state.acao()

class State(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def acao(self):
         pass

class Dormir(State):

    def acao(self):
        print("Vou dormir")
        sleep(5)
        print("Acordei")
        return True

class Comer(State):
    def acao(self):
        print("Digerir a comida")
        sleep(5)
        print("Refeição concluída")
        return True

class Estudar(State):

    def acao(self):
        print("Estudar")
        sleep(10)
        print("Terminei de estudar")
        return True

if __name__ == "__main__":
    estados = []
    estado = Estudar()
    estados.append(estado)
    estado = Comer()
    estados.append(estado)
    estado = Dormir()
    estados.append(estado)
    for i in range(len(estados)):
        pessoa = Context(estados[i])
        if pessoa.request():
            pass
        else:
            i = i-1