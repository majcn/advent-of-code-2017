import sys

class PrepareData:

    @staticmethod
    def __fetchData():
        inputdata = sys.stdin.readlines()
        return [x.rstrip('\n') for x in inputdata]

    @staticmethod
    def getDataAsStr():
        return [x.split() for x in PrepareData.__fetchData()]

    @staticmethod
    def getDataAsInt():
        return [map(int, x.split()) for x in PrepareData.__fetchData()]
