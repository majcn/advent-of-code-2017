import sys

class PrepareData:

    @staticmethod
    def fetchData():
        inputdata = sys.stdin.readlines()
        return [x.rstrip('\n') for x in inputdata]

    @staticmethod
    def getDataAsStr():
        return [x.split() for x in PrepareData.fetchData()]

    @staticmethod
    def getDataAsInt():
        return [map(int, x.split()) for x in PrepareData.fetchData()]
