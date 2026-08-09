from abc import ABC, abstractmethod

class PaymentGateway:
    @abstractmethod
    def send(self, amount):
        pass
        
class CreditCardPayment(PaymentGateway):
    def send(self, amount):
        print("Processing credit card payment of amount:", amount)
        
class DebitCardPayment(PaymentGateway):
    def send(self, amount):
        print("Processing debit card payment of amount:", amount)
        
class UPIPayment(PaymentGateway):
    def send(self, amount):
        print("Processing UPI payment of amount:", amount)
        
class NetBankingPayment(PaymentGateway):
    def send(self, amount):
        print("Processing net banking payment of amount:", amount)
        
class WalletPayment(PaymentGateway):
    def send(self, amount):
        print("Processing wallet payment of amount:", amount)
        
class PaymentProcessor:
    @staticmethod
    def create_payment_gateway(payment_type):
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "debit_card":
            return DebitCardPayment()
        elif payment_type == "upi":
            return UPIPayment()
        elif payment_type == "net_banking":
            return NetBankingPayment()
        elif payment_type == "wallet":
            return WalletPayment()
        else:
            raise ValueError("Invalid payment type")
        
        
def main():
    payment_type = input("Enter payment type (credit_card, debit_card, upi, net_banking, wallet): ")
    amount = float(input("Enter amount to be paid: "))
    
    payment_gateway = PaymentProcessor.create_payment_gateway(payment_type)
    payment_gateway.send(amount)
    
    
main()