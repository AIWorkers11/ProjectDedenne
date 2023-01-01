import csv

class Model:
    def __init__(self):
        self.modelname = "デデンネ"
        self.modelposx = 0
        self.modelposy = 0
        self.sendmes = ""

    def send(self,text):
        self.words = ModelIndex().indexes
        for word in self.words:
            if text == word[0]:
                self.sendmes = word[1]
                return
        self.sendmes = "デネ？"

    def getModelName(self):
        return self.modelname
    
    def getModelPosX(self):
        return self.modelposx

    def getModelPosY(self):
        return self.modelposy
    
    def getSendMessage(self):
        return self.sendmes

    def setModelPosX(self,x):
        self.modelposx = x

    def setModelPosY(self,y):
        self.modelposy = y

class ModelIndex:
    def __init__(self):
        filename = "Dedenne_words.csv"
        with open(filename,encoding="UTF-8",newline="") as f:
            csvreader = csv.reader(f)
            self.indexes = [row for row in csvreader]