

from abc import ABC, abstractmethod




class PaymentHandler:
    def process_payment(self, payment_method, amount):
        self.processor = None


    def process_payment(self, payment_method,amount):
        if payment_method == "credit_card":
            self.processor = CreditCardPaymentHandler()
            self.processor.process_payment(amount)
        elif payment_method == "paypal":
            self.processor = PayPalPaymentHandler()
            self.processor.process_payment(amount)
        else:
            raise ValueError("Unknown payment method")
        






class CreditCardPayment:
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



