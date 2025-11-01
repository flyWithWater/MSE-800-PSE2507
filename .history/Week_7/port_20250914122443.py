


"""
Develop an Auckland Transport logistics system in port using Singleton and Factory design patterns. 
Refer to the attached figure for a schematic view of the project design. Use your creativity into your development. 
Share the result in GitHub with one short paragraph description. 

"""


# 1. AucklandTransportSystem class using Singleton pattern
# 2. Different Transport classes (Bus, Train, Ferry) implementing a common interface


from abc import ABC, abstractmethod
import threading


class AucklandTransportSystem:
    _instance = None
    _threading_lock = threading.Lock()


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AucklandTransportSystem, cls).__new__(cls)
        return cls._instance


    
    def __init__(self):
        self.transports = []

   
