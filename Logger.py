class Logger():
    typeOfLogger = None
    __instance = None
    @staticmethod 
    def getInstance(typeOfLogger = "INFO"):
        if Logger.__instance == None:
            Logger.__instance = Logger(typeOfLogger)
        return Logger.__instance
    
    def __init__(self, typeOfLogger):
        self.typeOfLogger = typeOfLogger

    def showInfo(self, info):
        if self.typeOfLogger == "INFO":
            print("INFO: " + str(info))

    def showWarn(self, warn):
        if self.typeOfLogger == "INFO" or self.typeOfLogger == "WARN":
            print("WARN: " + str(warn))
    
    def showError(self, error):
        print("ERROR: " + str(error))