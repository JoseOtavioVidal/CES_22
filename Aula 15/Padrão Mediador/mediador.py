from random import randint
from time import sleep

class Mediator:
    def __init__(self):
        self._aviao = None
        self._jatinho = None
        self.isAnyoneInTheAirstrip = False
        self.isLand = [False, False]

    def setAviao(self, aviao):
        self._aviao = aviao

    def setJatinho(self, jatinho):
        self._jatinho = jatinho


    def manage(self):
        if not self.isLand[0]:
            m = self._aviao.requestToLand()
            if m and not(self.isAnyoneInTheAirstrip):
                print("Tower Control: You're allowed to land")
                self.isAnyoneInTheAirstrip = True
                self.isLand[0] = True
                self._aviao.land()
                sleep(5)
            else:
                print("Tower Control:  You can't land right now. Wait a few moments")
                self._aviao.response(False)
        if not self.isLand[1]:
            m = self._jatinho.requestToLand()
            if m and not(self.isAnyoneInTheAirstrip):
                print("Tower Control: You're allowed to land")
                self.isAnyoneInTheAirstrip = True
                self.isLand[1] = True
                self._jatinho.land()
            else:
                print("Tower Control:  You can't land right now. Wait a few moments")
                self._jatinho.response(False)

    def getIsTheAirStripFree(self):
        return self.isAnyoneInTheAirstrip

    def everyoneIsInTheGround(self):
        if self.isLand[0] and self.isLand[1]:
            return True
        else:
            self.isAnyoneInTheAirstrip = False
            return False

class Aviao():
    def __init__(self, mediator):
        self._mediator = mediator

    def requestToLand(self):
        print("Airplane: I'd like to land")
        if randint(0, 10) < 3:
            return True
        else:
            return False

    def land(self):
       print("Airplane: I'm landing")

    def response(self, answerToRequest):
        if answerToRequest == False:
            print("Airplane: I'll wait")


class Jatinho():
    def __init__(self, mediator):
        self._mediator = mediator

    def requestToLand(self):
        print("Small aircraft: I'd like to land")
        if randint(0, 10) < 8:
            return True
        else:
            return False

    def land(self):
       print("Small aircraft: I'm landing")

    def response(self, answerToRequest):
        if not answerToRequest:
            print("Small aircraft: I'll wait")

if __name__ == "__main__":
    mediator = Mediator()
    aviao = Aviao(mediator)
    jatinho = Jatinho(mediator)
    mediator.setAviao(aviao)
    mediator.setJatinho(jatinho)
    while not mediator.everyoneIsInTheGround():
        mediator.manage()