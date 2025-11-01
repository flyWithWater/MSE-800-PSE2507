

from abc import ABC, abstractmethod




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
    def create_payment_handler(self):
        pass

   

class CreditCardPaymentFactory(AbstractPaymentFactory):
    def create_payment_handler(self):
        return CreditCardPayment()

class PayPalPaymentFactory(AbstractPaymentFactory):
    def create_payment_handler(self):
        return PayPalPayment()


  
        
class SuperFactory:
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