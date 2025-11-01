

class PaypalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class StripePayment:
    def process_payment(self, amount):
        print(f"Processing Stripe payment of {amount}")

class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount}")    


class PaymentHandler:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

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






