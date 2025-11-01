

class PaypalPayment:
    def process_payment(self, amount)->bool:
        print(f"Processing PayPal payment of {amount}")
        return True

class StripePayment:
    def process_payment(self, amount)->bool:
        print(f"Processing Stripe payment of {amount}")
        return True

class CreditCardPayment:
    def process_payment(self, amount)->bool:
        print(f"Processing Credit Card payment of {amount}")
        return True


class PaymentHandler:
    def __init__(self):
        self.payment_processor = None

    def checkout(payment_method, amount):
        if payment_method == 'paypal':
            payment_processor = PaypalPayment()
        elif payment_method == 'stripe':
            payment_processor = StripePayment()
        elif payment_method == 'credit_card':
            payment_processor = CreditCardPayment()
        else:
            raise ValueError("Unknown payment method")
        
        payment_processor.process_payment(amount)



class PaymentFactory:

    @staticmethod
    def get_payment_processor(method):
        if method == 'paypal':
            return PaypalPayment()
        elif method == 'stripe':
            return StripePayment()
        elif method == 'credit_card':
            return CreditCardPayment()
        else:
            raise ValueError("Unknown payment method")




class PaymentHandlerWithFactory:
    def __init__(self):
        self.payment_processor = None

    def checkout(payment_method, amount):
        payment_processor = PaymentFactory.get_payment_processor(payment_method)
        payment_processor.process_payment(amount)