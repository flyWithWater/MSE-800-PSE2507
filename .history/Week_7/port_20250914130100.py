


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


class Goods(ABC):

    def _init_(self, goods_type):
        self.goods_type = goods_type

    def get_info(self):
        return f"Goods Type: {self.goods_type}"
    

# 3. Factory class to create transport objects based on input type
class DeliveryApproach(ABC):
    @abstractmethod
    def deliver(self,goods:Goods):
        pass
    
    def can_handle_goods(self, goods: 'Goods'):
        pass


delivery_approaches = ["lorry", "train", "ferry"]


class AucklandTransportSystem:
    _instance = None
    _threading_lock = threading.Lock()



    def __init__(self):
        self._delivery_approaches = []
        for transport in delivery_approaches:
            self._delivery_approaches.append(TransportFactory.get_transport(transport))


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._threading_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None

        return cls._instance

    def get_transport_system(self):
        return self._instance

    
    def destribute_goods(self, goods:Goods):
        for approach in self._delivery_approaches:
            if approach.can_handle_goods(goods):
                approach.deliver()
                return
        print("No available delivery approach can handle this type of goods.")

        






class Lorry(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Bus")

    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.CONTAINER, GoodsType.GENERAL, GoodsType.REFRIGERATED


class Train(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Train")
    
    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.DANGEROUS, GoodsType.CONTAINER, GoodsType.GENERAL,GoodsType.DANGEROUS

class Ferry(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Ferry")
    

    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.DANGEROUS, GoodsType.CONTAINER, GoodsType.GENERAL,GoodsType.REFRIGERATED,GoodsType.DANGEROUS
   


class TransportFactory:
    @staticmethod
    def get_transport(transport_type)->DeliveryApproach:
        if transport_type == "lorry":
            return Lorry()
        elif transport_type == "train":
            return Train()
        elif transport_type == "ferry":
            return Ferry()
        else:
            raise ValueError("Unknown transport type")




class GoodsType(Enum):
    DANGEROUS = "Dangerous"
    CONTAINER = "Container"
    GENERAL = "General"
    REFRIGERATED = "Refrigerated"


    

class DangerousGoods(Goods):

    def _init_(self):
        super()._init_(GoodsType.DANGEROUS)
        


class ContainerGoods(Goods):

    def _init_(self):
        super()._init_(GoodsType.CONTAINER)

class GeneralGoods(Goods):

    def _init_(self):
        super()._init_(GoodsType.GENERAL)

class RefrigeratedGoods(Goods):
    def _init_(self):
        super()._init_(GoodsType.REFRIGERATED)





def main():
    
    ats = AucklandTransportSystem.get_transport_system())
    

    goods1 = DangerousGoods(GoodsType.DANGEROUS)
    goods2 = ContainerGoods()
    goods3 = GeneralGoods()
    goods4 = RefrigeratedGoods()

    port1.destribute_goods(goods1)
    port1.destribute_goods(goods2)
    port1.destribute_goods(goods3)
    port1.destribute_goods(goods4)