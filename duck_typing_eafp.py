class CardPayment:
    def pay(self, amount):
        print(f"Paid {amount} by card")


class BkashPayment:
    def pay(self, amount):
        print(f"Paid {amount} by bkash")   


class CashPayment:
    def pay(self, amount):
        print(f"Paid {amount} in cash") 


class Paypal:
    pass


def process_payment(payment_method, amount):
    try:
        payment_method.pay(amount)

    except AttributeError:
        print("Payment method doesn't exist!")   

            
process_payment(BkashPayment(), 500)  

process_payment(CardPayment(), 500) 

process_payment(CashPayment(), 500) 

process_payment(Paypal(), 500)             