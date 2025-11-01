


"""
Develop an Auckland Transport logistics system in port using Singleton and Factory design patterns. 
Refer to the attached figure for a schematic view of the project design. Use your creativity into your development. 
Share the result in GitHub with one short paragraph description. 

"""


# 1. AucklandTransportSystem class using Singleton pattern
# 2. Different Transport classes (Bus, Train, Ferry) implementing a common interface


from abc import ABC, abstractmethod
import threading
from enum import Enum



class AucklandTransportSystem:
    _instance = None
    _threading_lock = threading.Lock()


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._threading_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None

        return cls._instance

    def get_transport_system(self):
        return self._instance

    




class TransportFactory:
    @staticmethod
    def get_transport(transport_type):
        if transport_type == "bus":
            return Bus()
        elif transport_type == "train":
            return Train()
        elif transport_type == "ferry":
            return Ferry()
        else:
            raise ValueError("Unknown transport type")



# 3. Factory class to create transport objects based on input type
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Lorry(Transport):
    def deliver(self,):
        print("Delivering by Bus")

class Train(Transport):
    def deliver(self):
        print("Delivering by Train")

class Ferry(Transport):
    def deliver(self):
        print("Delivering by Ferry")
   

enum GoodsType:

    DANGEROUS = "Dangerous"
    CONTAINER = "Container"
    GENERAL = "General"
    REFRIGERATED = "Refrigerated"


class Goods(ABC):
    def _init_(self, goods_type, max_weight, max_length):
        self.goods_type = goods_type
        self.max_weight = max_weight
        self.max_length = max_length

    def get_info(self):
        return f"Goods Type: {self.goods_type}, Max Weight: {self.max_weight}, Max Length: {self.max_length}"
    

class DangerousGoods(Goods):

    def _init_(self, goods_type, max_weight, max_length, hazard_level):
        super()._init_(goods_type, max_weight, max_length)
        self.hazard_level = hazard_level


class ContainerGoods(Goods):

    def _init_(self):
        super()._init_("Container", max_weight, max_length)
        self.container_size = container_size


