import sys
from lib import Leap 

class Listener(Leap.Listener):
    def __init__(self): 
        super(Listener, self).__init__()

    def onInit(self, controller):
        pass  
