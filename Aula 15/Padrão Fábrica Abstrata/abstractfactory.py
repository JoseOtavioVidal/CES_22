import abc

#The interface with the client
class PortalAcademicoElement:
    def __init__(self, mode, purpose, language):
        self.__mode = mode
        self.__purpose = purpose
        self.__language = language

    def getMode(self):
        return self.__mode

    def getPurpose(self):
        return self.__purpose

    def getLanguage(self):
        return self.__language

class StudentLoginPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "student", "login", language)

class StudentDashboardPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "student", "dashboard", language)

class StudentReportsPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "student", "reports", language)

class ProfessorLoginPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "professor", "login", language)

class ProfessorDashboardPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "professor", "dashboard", language)

class ProfessorReportsPortal(PortalAcademicoElement):
    def __init__(self, language):
        PortalAcademicoElement.__init__(self, "professor", "reports", language)

class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getLogin(self):
        pass

    @abc.abstractmethod
    def getDashboard(self):
        pass

    @abc.abstractmethod
    def getReports(self):
        pass

class PortalStudent(AbstractFactory):

    def __init__(self, language):
        self.language = language

    def getLogin(self):
        return StudentLoginPortal(self.language)

    def getDashboard(self):
        return StudentDashboardPortal(self.language)

    def getReports(self):
        return StudentReportsPortal(self.language)

class PortalProfessor(AbstractFactory):

    def __init__(self, language):
        self.language = language

    def getLogin(self):
        return ProfessorLoginPortal(self.language)

    def getDashboard(self):
        return ProfessorDashboardPortal(self.language)

    def getReports(self):
        return ProfessorReportsPortal(self.language)


if __name__ == "__main__":
    language = "portuguese"

    #Mode Student
    factory = PortalStudent(language)
    login = factory.getLogin()
    dashboard = factory.getDashboard()
    reports = factory.getReports()

    print("Portal na lingua: {}".format(login.getLanguage()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(login.getMode(), login.getPurpose()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(dashboard.getMode(), dashboard.getPurpose()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(reports.getMode(), reports.getPurpose()))

    language = "english"
    factory = PortalProfessor(language)
    login = factory.getLogin()
    dashboard = factory.getDashboard()
    reports = factory.getReports()

    print("Portal na lingua: {}".format( login.getLanguage()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(login.getMode(), login.getPurpose()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(dashboard.getMode(), dashboard.getPurpose()))
    print("Modo do Portal:{0} e elemento do portal {1}".format(reports.getMode(), reports.getPurpose()))
