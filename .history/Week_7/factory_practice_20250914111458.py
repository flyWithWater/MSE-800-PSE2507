

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
        






class CreditCardPaymentHandler(PaymentHandler):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPaymentHandler(PaymentHandler):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")





class PaymentFactory:
    @staticmethod
    def create_payment_handler(payment_type):
        if payment_type == "credit_card":
            return CreditCardPaymentHandler()
        elif payment_type == "paypal":
            return PayPalPaymentHandler()
        else:
            raise ValueError("Unknown payment type")
        



class PaymentHandlerWithFactory:


    def process_payment(self, payment_type, amount):
        handler = PaymentFactory.create_payment_handler(payment_type)
        handler.process_payment(amount)