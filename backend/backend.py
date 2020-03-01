import to_csv_parser_client as pc
import to_gateway_server as gs
import threading
import time
class Data():
    def __init__(self):
        self.data = None
        self._lock = threading.Lock()
    
    def updateData(self,d):
        with self._lock:
            self.data = d
    def getData(self):
        return self.data

def checkUpdate(data,parserClient):
    while(true):
        r = parserClient.checkUpdate()
        if(r.message):
            d = updateDataparserClient.update(data)
        time.sleep(10000)
    

if __name__ == "__main__":
    data = Data()
    parserClient = pc.parserClient()
    gatewayServer = gs.gatewayServer(data)
    x = threading.Thread(target=checkUpdate, args=(data,parserClient))
    gatewayServer.start()