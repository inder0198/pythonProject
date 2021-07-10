class enc:
    def __init__(self):
        self.__bal=3000

    def getbal(self):
        print(self.__bal)

    def setbal(self,a):
        self.__bal = a

obj=enc()
obj.getbal()
obj.setbal(1000)
obj.getbal()
