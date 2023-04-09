class Logger():
    def __init__(self, typeOfLogger):
        self.logger = typeOfLogger
    
    def showInfo(self, info):
        if self.logger == "INFO":
            print("INFO: " + str(info))

    def showWarn(self, warn):
        if self.logger == "INFO" or self.logger == "WARN":
            print("WARN: " + str(warn))
    
    def showError(self, error):
        print("ERROR: " + str(error))