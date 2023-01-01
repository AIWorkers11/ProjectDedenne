class user:
    def __init__(self,name="Guest"):
        self.username = name
    def getUserName(self):
        return self.username
    def setUserName(self,name):
        self.username = name