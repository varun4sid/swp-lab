""" INTERPRETER PATTERN
Develop a customer support chatbot for banking services.
Users type messages like:

• “Check my balance”
• “Transfer 5000 to Ravi”
• “Show last 5 transactions”
• “Block my card if lost”

The chatbot must interpret the meaning of the sentence and execute the
correct banking service
"""

from abc import ABC, abstractmethod


class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.card_blocked = False

    def check_balance(self):
        print(f"{self.name}, your current balance is: ${self.balance}")
        
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")
        print(f"Successfully deposited ${amount}. New balance: ${self.balance}")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient funds for the transfer.")
            return
        self.balance -= amount
        self.transactions.append(f"Transferred ${amount} to {recipient}")
        print(f"Successfully transferred ${amount} to {recipient}. New balance: ${self.balance}")

    def show_transactions(self, count=5):
        print(f"Last {count} transactions:")
        for transaction in self.transactions[-count:]:
            print(transaction)

    def block_card(self):
        self.card_blocked = True
        print("Your card has been blocked due to loss or theft.")


class BankingExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass


class CheckBalanceExpression(BankingExpression):
    def __init__(self, customer):
        self.customer = customer

    def interpret(self):
        self.customer.check_balance()


class TransferExpression(BankingExpression):
    def __init__(self, customer, amount, recipient):
        self.customer = customer
        self.amount = amount
        self.recipient = recipient

    def interpret(self):
        self.customer.transfer(self.amount, self.recipient)


class ShowTransactionsExpression(BankingExpression):
    def __init__(self, customer, count):
        self.customer = customer
        self.count = count

    def interpret(self):
        self.customer.show_transactions(self.count)


class BlockCardExpression(BankingExpression):
    def __init__(self, customer):
        self.customer = customer

    def interpret(self):
        self.customer.block_card()


class BankingChatbot:

    def __init__(self, customer):
        self.customer = customer

    def parse(self, message):
        tokens = message.lower().split()

        if "balance" in tokens:
            return CheckBalanceExpression(self.customer)

        if "transfer" in tokens and "to" in tokens:
            amount_index = tokens.index("transfer") + 1
            recipient_index = tokens.index("to") + 1
            if recipient_index >= len(tokens):
                raise ValueError("A transfer recipient is required.")
            amount = float(tokens[amount_index].replace("$", "").replace(",", ""))
            if amount <= 0:
                raise ValueError("Transfer amount must be greater than zero.")
            recipient = " ".join(tokens[recipient_index:]).title()
            return TransferExpression(self.customer, amount, recipient)

        if "transactions" in tokens or "transaction" in tokens:
            count = 5
            if "last" in tokens:
                count_index = tokens.index("last") + 1
                if count_index >= len(tokens):
                    raise ValueError("A transaction count is required.")
                count = int(tokens[count_index])
            if count <= 0:
                raise ValueError("Transaction count must be greater than zero.")
            return ShowTransactionsExpression(self.customer, count)

        if "block" in tokens and "card" in tokens:
            return BlockCardExpression(self.customer)

        raise ValueError(f"I do not understand this banking request: {message}")

    def respond(self, message):
        expression = self.parse(message)
        expression.interpret()


if __name__ == "__main__":
    customer = Customer("Anita")
    customer.deposit(10000)
    chatbot = BankingChatbot(customer)

    for request in (
        "Check my balance",
        "Transfer 5000 to Ravi",
        "Show last 5 transactions",
        "cehck ma balance",
        "Block my card if lost",
    ):
        print(f"\n> {request}")
        chatbot.respond(request)