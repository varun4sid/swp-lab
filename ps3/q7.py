"""
We have a real application service that performs business operations.
We want to add logging, monitoring, and access tracking without
changing the original service code.

Use proxy pattern to implement this functionality.
"""

from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def perform_operation(self):
        pass
    
class RealService(Service):
    def perform_operation(self):
        print("Performing the actual business operation.")
        
    def additional_method(self):
        print("This is an additional method in the real service.")
        
class ServiceProxy(Service):
    def __init__(self, real_service):
        self.real_service = real_service

    def log_access(self, user):
        print(f"Logging access to the service by user: {user}")

    def monitor_performance(self):
        print("Monitoring performance of the service.")

    def track_usage(self):
        print("Tracking usage of the service.")
        
    def perform_operation(self):
        self.log_access("Varun")
        self.monitor_performance()
        self.track_usage()
        self.real_service.perform_operation()
        
        
def main():
    real_service = RealService()
    proxy_service = ServiceProxy(real_service)
    proxy_service.perform_operation()
    
    
main()