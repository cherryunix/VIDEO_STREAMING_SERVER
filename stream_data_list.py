from multiprocessing import Queue

class StreamDataList():
    def __init__(self):
        self._streamdatalist = {}
    
    def addqueue(self,remoteaddr):
        self._streamdatalist[remoteaddr] = Queue()
    
    def getqueue(self,remoteaddr):
        return self._streamdatalist[remoteaddr]
    
