"""
Consider an Online Food Delivery System (Swiggy / Zomato).
When a customer places an order, the system follows a fixed workflow,
regardless of the restaurant:
1. Accept order
2. Assign delivery partner
3. Deliver order
4. Collect feedback

Even though the flow is fixed, the following steps differs:
• Preparation time and method (Based on the type of restaurant)
• Packing food (Cloud kitchens use automated packing)
"""

import random
from abc import ABC, abstractmethod


class FoodDeliveryTemplate(ABC):
    def process_order(self):
        self.accept_order()
        self.prepare_food()
        self.pack_food()
        self.assign_delivery_partner()
        self.deliver_order()
        self.collect_feedback()

    def accept_order(self):
        print("Order accepted and recorded in the system.")

    def assign_delivery_partner(self):
        print("Delivery partner assigned to the order.")

    def deliver_order(self):
        print("Order delivered to the customer.")

    def collect_feedback(self):
        print("Customer feedback collected successfully.")

    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def pack_food(self):
        pass


class TraditionalRestaurant(FoodDeliveryTemplate):
    def prepare_food(self):
        print("Preparing food using the traditional kitchen method; estimated time: 25 minutes.")

    def pack_food(self):
        print("Packing food manually in takeaway boxes and paper bags.")


class CloudKitchen(FoodDeliveryTemplate):
    def prepare_food(self):
        print("Preparing food in an automated kitchen; estimated time: 12 minutes.")

    def pack_food(self):
        print("Packing food using automated sealing and packaging machines.")


class FoodDeliverySystem:
    def __init__(self, restaurant_type):
        if restaurant_type == "traditional":
            self.restaurant = TraditionalRestaurant()
        elif restaurant_type == "cloud":
            self.restaurant = CloudKitchen()
        else:
            raise ValueError("Invalid restaurant type. Choose 'traditional' or 'cloud'.")

    def process_order(self):
        self.restaurant.process_order()


def initialize_restaurants():
    restaurant_menu = {
        "Aroma Bites": ["Paneer Tikka", "Butter Naan", "Veg Biryani"],
        "Burger Hub": ["Classic Burger", "French Fries", "Cold Coffee"],
        "Fresh Bowl": ["Salad Bowl", "Wrap", "Smoothie"],
        "Spice Route": ["Dal Makhani", "Jeera Rice", "Roti"],
    }

    restaurants = {}
    for restaurant_name, dishes in restaurant_menu.items():
        restaurants[restaurant_name] = {
            "kitchen_type": random.choice(["traditional", "cloud"]),
            "dishes": dishes,
        }
    return restaurants


def menu(restaurants):
    print("\nAvailable Restaurants:")
    restaurant_names = list(restaurants.keys())

    for index, restaurant in enumerate(restaurant_names, start=1):
        kitchen_type = restaurants[restaurant]["kitchen_type"]
        print(f"{index}. {restaurant} ({kitchen_type} kitchen)")

    restaurant_choice = int(input("\nSelect a restaurant by number: "))
    if restaurant_choice < 1 or restaurant_choice > len(restaurant_names):
        raise ValueError("Invalid restaurant selection.")

    selected_restaurant = restaurant_names[restaurant_choice - 1]
    dishes = restaurants[selected_restaurant]["dishes"]

    print(f"\nMenu for {selected_restaurant}:")
    for index, dish in enumerate(dishes, start=1):
        print(f"{index}. {dish}")

    dish_choice = int(input("\nSelect a dish by number: "))
    if dish_choice < 1 or dish_choice > len(dishes):
        raise ValueError("Invalid dish selection.")

    selected_dish = dishes[dish_choice - 1]
    print(f"\nYou selected: {selected_restaurant} - {selected_dish}")

    kitchen_type = restaurants[selected_restaurant]["kitchen_type"]
    order_system = FoodDeliverySystem(kitchen_type)
    order_system.process_order()


def main():
    restaurants = initialize_restaurants()
    menu(restaurants)


if __name__ == "__main__":
    main()
