""" STRATEGY PATTERN
Consider an E-commerce application.
When a customer checks out, they can choose different payment methods:
• Credit Card
• Debit Card
• UPI
• Net Banking
• Wallets
Each payment method has different processing logic, but the checkout flow
remains the same.
"""

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder, cvv, expiry_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            raise ValueError("Invalid credit card number.")
        if len(self.cvv) not in (3, 4) or not self.cvv.isdigit():
            raise ValueError("Invalid CVV.")

        print(f"Processing credit card payment of ${amount} for {self.card_holder}")
        print("Card verified. Payment approved.")
        return True


class DebitCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder, cvv, expiry_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            raise ValueError("Invalid debit card number.")
        if len(self.cvv) != 3 or not self.cvv.isdigit():
            raise ValueError("Invalid CVV.")

        print(f"Processing debit card payment of ${amount} for {self.card_holder}")
        print("Debit card authentication successful.")
        return True


class UpiPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if "@" not in self.upi_id or len(self.upi_id.split("@")) != 2:
            raise ValueError("Invalid UPI ID format.")

        print(f"Processing UPI payment of ${amount} for UPI ID: {self.upi_id}")
        print("UPI request sent and approved.")
        return True


class NetBankingPayment(PaymentStrategy):
    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if not self.bank_name or not self.account_number:
            raise ValueError("Bank name and account number are required.")
        if len(self.account_number) < 8:
            raise ValueError("Account number is too short.")

        print(f"Processing net banking payment of ${amount} from {self.bank_name} account {self.account_number}")
        print("Bank authentication successful. Funds transferred.")
        return True


class WalletPayment(PaymentStrategy):
    def __init__(self, wallet_id, balance=0):
        self.wallet_id = wallet_id
        self.balance = balance

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if not self.wallet_id:
            raise ValueError("Wallet ID is required.")
        if amount > self.balance:
            raise ValueError(f"Insufficient wallet balance. Available balance: ${self.balance}")

        self.balance -= amount
        print(f"Processing wallet payment of ${amount} using wallet {self.wallet_id}")
        print(f"Wallet balance updated: ${self.balance}")
        return True


class Checkout:
    def __init__(self, payment_strategy=None):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        if self.payment_strategy is None:
            raise ValueError("No payment method selected.")
        return self.payment_strategy.pay(amount)


if __name__ == "__main__":
    payments = [
        ("Valid Credit Card", CreditCardPayment("1234567890123456", "Alice Smith", "234", "12/29"), 250),
        ("Valid Debit Card", DebitCardPayment("6543210987654321", "Alice Smith", "987", "06/28"), 180),
        ("Valid UPI", UpiPayment("alice@oksbi"), 120),
        ("Valid Net Banking", NetBankingPayment("HDFC", "9876543210"), 550),
        ("Valid Wallet", WalletPayment("WAL-001", 1000), 300),
        ("Invalid Credit Card Number", CreditCardPayment("12345", "Bob Jones", "234", "12/29"), 150),
        ("Invalid UPI ID", UpiPayment("invalidupi"), 99),
        ("Insufficient Wallet Balance", WalletPayment("WAL-002", 50), 100),
        ("Zero Amount", CreditCardPayment("1111222233334444", "Cara Lee", "123", "01/30"), 0),
    ]

    for name, strategy, amount in payments:
        checkout = Checkout(strategy)
        try:
            print(f"\nAttempting: {name}")
            result = checkout.process_payment(amount)
            if result:
                print(f"Payment successful for {name}.")
        except ValueError as e:
            print(f"Payment failed for {name}: {e}")
        except Exception as e:
            print(f"Unexpected error for {name}: {e}")