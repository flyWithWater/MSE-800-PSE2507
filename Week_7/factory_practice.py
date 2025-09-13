

from abc import ABC, abstractmethod


# None-Factory style implementation
"""
    Characteristics of None-Factory Pattern:
    1. The object creation code is mixed with the area where we use the object.  
        -> Every time we need to modify or add a new payment method, we have to modify the code in the payment handler class as well.


"""

class PaymentHandler:
    def process_payment(self, payment_method, amount):
        self.processor = None


    def process_payment(self, payment_method,amount):
        if payment_method == "credit_card":
            self.processor = CreditCardPayment()
            self.processor.process_payment(amount)
        elif payment_method == "paypal":
            self.processor = PayPalPayment()
            self.processor.process_payment(amount)
        elif payment_method == "cash": # newly added payment method
            self.processor = CashPayment() # newly added payment method
            self.processor.process_payment(amount) # newly added payment method
        else:
            raise ValueError("Unknown payment method")
        


class AbstractPayment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass



class CreditCardPayment(AbstractPayment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")



# Factory Method Pattern Implementation
"""
    Characteristics of Factory Method Pattern:
    1. Seperates the object creating code from the area where we use the object.
         -> When we need to add a new payment method, we only need to create a new factory class without modifying the existing code.

    2. Every time we need to add a new payment method, we have to create a new factory class and a new payment class. It can lead to an increase in the number of classes in the code level.
"""

class PaymentFactory:
    @staticmethod
    def create_payment_handler(payment_type):
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "paypal":
            return PayPalPayment()
        else:
            raise ValueError("Unknown payment type")
        



class PaymentHandlerWithFactory:


    def process_payment(self, payment_type, amount):
        handler = PaymentFactory.create_payment_handler(payment_type)
        handler.process_payment(amount)





class AbstractPaymentFactory(ABC):
    @abstractmethod
    def create_payment_handler(self)->PaymentHandler:
        pass

   

class CreditCardPaymentFactory(AbstractPaymentFactory):
    def create_payment_handler(self):
        return CreditCardPayment()

class PayPalPaymentFactory(AbstractPaymentFactory):
    def create_payment_handler(self):
        return PayPalPayment()


  
        
class PaymentFactory:
    @staticmethod
    def get_payment_factory(payment_type):
        if payment_type == "credit_card":
            return CreditCardPaymentFactory()
        elif payment_type == "paypal":
            return PayPalPaymentFactory()
        elif payment_type == "cash":
            return CashPaymentFactory()
        else:
            raise ValueError("Unknown payment type")


class CashPayment(AbstractPayment):
    def process_payment(self, amount):
        print(f"Processing cash payment of {amount}")



class CashPaymentFactory(AbstractPaymentFactory):
    def create_payment_handler(self):
        return CashPayment()