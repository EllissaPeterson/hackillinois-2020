class Data():
    def __init__(self):
        self.data = None
        self._lock = threading.Lock()
    
    def updateData(self,dict)
        with self._lock:
            self.data = d
    def getData(self):
        return self.data
    