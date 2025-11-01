


"""
Develop an Auckland Transport logistics system in port using Singleton and Factory design patterns. 
Refer to the attached figure for a schematic view of the project design. Use your creativity into your development. 
Share the result in GitHub with one short paragraph description. 

"""


# 1. AucklandTransportSystem class using Singleton pattern
# 2. Different Transport classes (Bus, Train, Ferry) implementing a common interface


from abc import ABC, abstractmethod
import stat
import threading
from enum import Enum


class Goods(ABC):

    def __init__(self, goods_type):
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
    _instance:"AucklandTransportSystem" = None
    _threading_lock = threading.Lock()



    def __init__(self):
        self._delivery_approaches:list[DeliveryApproach] = []
        for transport in delivery_approaches:
            self._delivery_approaches.append(TransportFactory.get_transport(transport))


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._threading_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None

        return cls._instance

    @staticmethod
    def get_transport_system():
        if not AucklandTransportSystem._instance:
            AucklandTransportSystem._instance = AucklandTransportSystem()
        return AucklandTransportSystem._instance

    def destribute_goods(self, goods:Goods):
        for approach in self._delivery_approaches:
            if approach.can_handle_goods(goods):
                approach.deliver(goods)
                return
        print("No available delivery approach can handle this type of goods.")

        



class RefrigeratedLorry(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Refrigerated Lorry")

    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.REFRIGERATED


class Lorry(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Bus")

    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.CONTAINER, GoodsType.GENERAL


class Train(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Train")
    
    def can_handle_goods(self, goods: 'Goods'):
        return goods.goods_type == GoodsType.DANGEROUS, GoodsType.CONTAINER, GoodsType.GENERAL,GoodsType.DANGEROUS

class Ferry(DeliveryApproach):
    def deliver(self,goods:Goods):
        print("Delivering by Ferry")
    

    def can_handle_goods(self, goods:Goods):
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
        elif transport_type == "refrigerated_lorry":
            return RefrigeratedLorry()
        else:
            raise ValueError("Unknown transport type")




class GoodsType(Enum):
    DANGEROUS = "Dangerous"
    CONTAINER = "Container"
    GENERAL = "General"
    REFRIGERATED = "Refrigerated"



class DangerousGoods(Goods):

    def _init_(self):
        super().__init__(GoodsType.DANGEROUS)
        
        


class ContainerGoods(Goods):

    def _init_(self):
        super().__init__(GoodsType.CONTAINER)

class GeneralGoods(Goods):

    def _init_(self):
        super().__init__(GoodsType.GENERAL)

class RefrigeratedGoods(Goods):
    def _init_(self):
        super().__init__(GoodsType.REFRIGERATED)





def main():
    
    ats = AucklandTransportSystem.get_transport_system()
    

    goods1 = DangerousGoods()
    goods2 = ContainerGoods()
    goods3 = GeneralGoods()
    goods4 = RefrigeratedGoods()

    ats.destribute_goods(goods1)
    ats.destribute_goods(goods2)
    ats.destribute_goods(goods3)
    ats.destribute_goods(goods4)

if __name__=="__main__":
    main()