""" CHAIN OF RESPONSIBILITY PATTERN
Consider a Bank Loan Processing System.
When a customer applies for a loan, the request passes through multiple
approval levels:

1. Clerk → Verifies documents
2. Manager → Approves medium loans
3. Regional Manager → Approves large loans
4. Head Office → Approves very large loans

Each authority has a loan approval limit.
If one level cannot approve, the request is forwarded to the next level.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        pass


class LoanRequest:
    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount
        self.approved = False
        self.approved_by = None
    
    def __repr__(self):
        status = f"Approved by {self.approved_by}" if self.approved else "Not approved"
        return f"LoanRequest({self.customer_name}, ${self.amount}, {status})"


class Clerk(Handler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.approval_limit = 1000
    
    def handle_request(self, request):
        if request.amount <= self.approval_limit:
            request.approved = True
            request.approved_by = "Clerk"
            print(f"Clerk: Approved loan of ${request.amount} for {request.customer_name}")
        else:
            print(f"Clerk: Cannot approve loan of ${request.amount}. Forwarding to Manager...")
            if self.next_handler:
                self.next_handler.handle_request(request)


class Manager(Handler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.approval_limit = 10000
    
    def handle_request(self, request):
        if request.amount <= self.approval_limit:
            request.approved = True
            request.approved_by = "Manager"
            print(f"Manager: Approved loan of ${request.amount} for {request.customer_name}")
        else:
            print(f"Manager: Cannot approve loan of ${request.amount}. Forwarding to Regional Manager...")
            if self.next_handler:
                self.next_handler.handle_request(request)


class RegionalManager(Handler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.approval_limit = 50000
    
    def handle_request(self, request):
        if request.amount <= self.approval_limit:
            request.approved = True
            request.approved_by = "Regional Manager"
            print(f"Regional Manager: Approved loan of ${request.amount} for {request.customer_name}")
        else:
            print(f"Regional Manager: Cannot approve loan of ${request.amount}. Forwarding to Head Office...")
            if self.next_handler:
                self.next_handler.handle_request(request)


class HeadOffice(Handler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.approval_limit = float('inf')
    
    def handle_request(self, request):
        request.approved = True
        request.approved_by = "Head Office"
        print(f"Head Office: Approved loan of ${request.amount} for {request.customer_name}")


def main():
    head_office = HeadOffice()
    regional_manager = RegionalManager(head_office)
    manager = Manager(regional_manager)
    clerk = Clerk(manager)
    
    # Test cases
    print("=" * 60)
    print("BANK LOAN PROCESSING SYSTEM - CHAIN OF RESPONSIBILITY")
    print("=" * 60)
    
    # Test 1: Small loan (handled by Clerk)
    print("\nTest 1: Small loan request")
    request1 = LoanRequest("Alice", 500)
    clerk.handle_request(request1)
    print(f"Result: {request1}\n")
    
    # Test 2: Medium loan (handled by Manager)
    print("Test 2: Medium loan request")
    request2 = LoanRequest("Bob", 5000)
    clerk.handle_request(request2)
    print(f"Result: {request2}\n")
    
    # Test 3: Large loan (handled by Regional Manager)
    print("Test 3: Large loan request")
    request3 = LoanRequest("Charlie", 30000)
    clerk.handle_request(request3)
    print(f"Result: {request3}\n")
    
    # Test 4: Very large loan (handled by Head Office)
    print("Test 4: Very large loan request")
    request4 = LoanRequest("Diana", 100000)
    clerk.handle_request(request4)
    print(f"Result: {request4}\n")
    
    # Test 5: Boundary case - exactly at approval limit
    print("Test 5: Boundary case - loan exactly at Manager's limit")
    request5 = LoanRequest("Eve", 10000)
    clerk.handle_request(request5)
    print(f"Result: {request5}\n")

    
if __name__ == "__main__":
    main()