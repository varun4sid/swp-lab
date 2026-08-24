""" OBSERVER PATTERN
Consider a Stock Market Monitoring Application used by investors.
Features:
• Investors subscribe to stock updates
• Receive alerts when price changes
• Track multiple stocks
• Get real-time notifications
Example:
• If TCS price rises → Investors get alert
• If Infosys falls → Subscribers get notification
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, stock_name, price):
        pass
    
    
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
    

class StockMarket(Subject):
    def __init__(self):
        self._observers = []
        self._stocks = {}
        self._updated_stock = None

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def set_stock_price(self, stock_name, price):
        if price < 0:
            raise ValueError("Stock price cannot be negative.")
        self._stocks[stock_name] = price
        self._updated_stock = stock_name
        self.notify_observers()

    def get_stock_price(self, stock_name):
        return self._stocks.get(stock_name)

    def notify_observers(self):
        if self._updated_stock is None:
            return
        price = self._stocks[self._updated_stock]
        for observer in self._observers:
            observer.update(self._updated_stock, price)


class Investor(Observer):
    def __init__(self, name):
        self.name = name
        self.alerts = []

    def update(self, stock_name, price):
        alert = f"{self.name}: {stock_name} price changed to {price}"
        self.alerts.append(alert)
        print(alert)


if __name__ == "__main__":
    stock_market = StockMarket()
    investor1 = Investor("Anita")
    investor2 = Investor("Rahul")

    stock_market.register_observer(investor1)
    stock_market.register_observer(investor2)

    stock_market.set_stock_price("TCS", 3850)
    stock_market.set_stock_price("Infosys", 1520)

    stock_market.remove_observer(investor2)
    stock_market.set_stock_price("TCS", 3900)
