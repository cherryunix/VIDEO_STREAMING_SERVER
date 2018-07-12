import os
from pylive import live
from stream_data_list import StreamDataList
from multiprocessing import Queue,Process

import cv2

filepath = "/home/vbuntu/02.MOV"

streamdatalist = StreamDataList()
streamdatalist.addqueue(filepath)

class Test_CV():
    def __init__(self,filepath):
        self._filepath = filepath
        self._cap = cv2.VideoCapture(self._filepath)
        self._queue = streamdatalist.getqueue(self._filepath)

    def getProperty(self):
        height = cv.GetCaptureProperty(self._cap,cv.CV_CAP_PROP_FRAME_HEIGHT)
        width = cv.GetCaptureProperty(self._cap,cv.CV_CAP_PROP_FRAME_WIDTH)
        return height,width
    
    def readFile(self):
        while True:
            ret,frame = cap.read()
            if ret:
                self._queue.put(frame)
    
    def start_live_loop(self):
        p = Process(target=self.readFile)
        p.start()
        

        

class Live():
    def __init__(self,remoteaddr,broadcastaddr,width,height):
        self._remoteaddr = remoteaddr
        self._broadcastaddr = broadcastaddr
        self._queue = streamdatalist.getqueue(self._remoteaddr)
        self._width = width
        self._height = height



    def _live_loop(self):
        def callback():
            return self._queue.get()
        
        live.start(url = 'unicast',
        width = self._width,
        height = self._height,
        buffersize = 65535,
        callback = callback,
        rtspPort = 12345
        )

    def start_live_loop_processing(self):
        p = Process(target = self._live_loop)
        p.daemon = True
        p.start()
    
def test_multithread():
    cvclient = Test_CV(filepath)
    height,width = cvclient.getProperty()
    live = Live(filepath,'',height,width)
    cvclient.start_live_loop()
    live.start_live_loop_processing()


if __name__ == "__main__":
    test_multithread()
