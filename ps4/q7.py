""" STATE PATTERN
Consider an E-commerce platform (like Amazon / Flipkart).
When a customer places an order, it goes through multiple states:
1. Order Placed
2. Payment Confirmed
3. Shipped
4. Out for Delivery
5. Delivered
6. Cancelled / Returned

The system’s behaviour changes depending on the current order state.
Example:
• You can cancel only before shipping
• You can track only after shipping
• You can return only after delivery
"""

from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def cancel_order(self, order):
        pass

    @abstractmethod
    def track_order(self, order):
        pass

    @abstractmethod
    def return_order(self, order):
        pass


class OrderPlacedState(OrderState):
    def cancel_order(self, order):
        order.set_state(CancelledState())
        print("Order cancelled successfully.")

    def track_order(self, order):
        print("Tracking is not available before shipment.")

    def return_order(self, order):
        print("Return is not allowed before delivery.")


class PaymentConfirmedState(OrderState):
    def cancel_order(self, order):
        order.set_state(CancelledState())
        print("Order cancelled after payment confirmation.")

    def track_order(self, order):
        print("Tracking is not available before shipment.")

    def return_order(self, order):
        print("Return is not allowed before delivery.")


class ShippedState(OrderState):
    def cancel_order(self, order):
        print("Order cannot be cancelled after it has been shipped.")

    def track_order(self, order):
        print(f"Tracking your order: Package is on the way. Current status: {order.status}")

    def return_order(self, order):
        print("Return is not allowed before delivery.")


class OutForDeliveryState(OrderState):
    def cancel_order(self, order):
        print("Order cannot be cancelled once it is out for delivery.")

    def track_order(self, order):
        print(f"Tracking your order: Out for delivery. Current status: {order.status}")

    def return_order(self, order):
        print("Return is not allowed before delivery.")


class DeliveredState(OrderState):
    def cancel_order(self, order):
        print("Order cannot be cancelled after delivery.")

    def track_order(self, order):
        print(f"Tracking your order: Delivered on {order.delivery_date}.")

    def return_order(self, order):
        order.set_state(ReturnedState())
        print("Return request accepted successfully.")


class CancelledState(OrderState):
    def cancel_order(self, order):
        print("This order is already cancelled.")

    def track_order(self, order):
        print("This order is cancelled and cannot be tracked.")

    def return_order(self, order):
        print("Cancelled orders cannot be returned.")


class ReturnedState(OrderState):
    def cancel_order(self, order):
        print("This order has already been returned.")

    def track_order(self, order):
        print("Tracking is unavailable for returned orders.")

    def return_order(self, order):
        print("This order has already been returned.")


class Order:
    def __init__(self):
        self.status = "Order Placed"
        self.delivery_date = "N/A"
        self.state = OrderPlacedState()

    def set_state(self, state):
        self.state = state
        self.status = state.__class__.__name__.replace("State", "").replace("Order", "")
        if self.status == "Placed":
            self.status = "Order Placed"
        elif self.status == "Confirmed":
            self.status = "Payment Confirmed"
        elif self.status == "Shipped":
            self.status = "Shipped"
        elif self.status == "OutForDelivery":
            self.status = "Out for Delivery"
        elif self.status == "Delivered":
            self.status = "Delivered"
        elif self.status == "Cancelled":
            self.status = "Cancelled"
        elif self.status == "Returned":
            self.status = "Returned"

    def cancel_order(self):
        self.state.cancel_order(self)

    def track_order(self):
        self.state.track_order(self)

    def return_order(self):
        self.state.return_order(self)

    def confirm_payment(self):
        self.set_state(PaymentConfirmedState())
        print("Payment confirmed.")

    def ship_order(self):
        self.set_state(ShippedState())
        print("Order shipped.")

    def mark_out_for_delivery(self):
        self.set_state(OutForDeliveryState())
        print("Order is out for delivery.")

    def deliver_order(self):
        self.delivery_date = "2026-09-20"
        self.set_state(DeliveredState())
        print("Order delivered successfully.")


if __name__ == "__main__":
    order = Order()

    print("Initial status:", order.status)
    order.track_order()
    order.cancel_order()

    order1 = Order()
    order1.confirm_payment()
    order1.cancel_order()
    order1.track_order()

    order2 = Order()
    order2.confirm_payment()
    order2.ship_order()
    order2.track_order()
    order2.cancel_order()

    order3 = Order()
    order3.confirm_payment()
    order3.ship_order()
    order3.mark_out_for_delivery()
    order3.deliver_order()
    order3.return_order()

    