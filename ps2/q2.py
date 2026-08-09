from abc import ABC, abstractmethod

# --- Abstract Products ---
class Starter(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

class MainCourse(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

class Dessert(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


# --- Concrete Products: Vegetarian ---
class VegStarter(Starter):
    def get_name(self) -> str:
        return "Spring Rolls"

class VegMainCourse(MainCourse):
    def get_name(self) -> str:
        return "Paneer Tikka Masala"

class VegDessert(Dessert):
    def get_name(self) -> str:
        return "Vegan Chocolate Mousse"


# --- Concrete Products: Non-Vegetarian ---
class NonVegStarter(Starter):
    def get_name(self) -> str:
        return "Chicken Wings"

class NonVegMainCourse(MainCourse):
    def get_name(self) -> str:
        return "Grilled Salmon"

class NonVegDessert(Dessert):
    def get_name(self) -> str:
        return "New York Cheesecake"


# --- Abstract Factory ---
class MealFactory(ABC):
    @abstractmethod
    def create_starter(self) -> Starter:
        pass

    @abstractmethod
    def create_main_course(self) -> MainCourse:
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass


# --- Concrete Factories ---
class VegetarianMealFactory(MealFactory):
    def create_starter(self) -> Starter:
        return VegStarter()

    def create_main_course(self) -> MainCourse:
        return VegMainCourse()

    def create_dessert(self) -> Dessert:
        return VegDessert()

class NonVegetarianMealFactory(MealFactory):
    def create_starter(self) -> Starter:
        return NonVegStarter()

    def create_main_course(self) -> MainCourse:
        return NonVegMainCourse()

    def create_dessert(self) -> Dessert:
        return NonVegDessert()
    
    
def main():
    # Create a vegetarian meal
    veg_factory = VegetarianMealFactory()
    veg_starter = veg_factory.create_starter()
    veg_main_course = veg_factory.create_main_course()
    veg_dessert = veg_factory.create_dessert()

    print("Vegetarian Meal:")
    print(f"Starter: {veg_starter.get_name()}")
    print(f"Main Course: {veg_main_course.get_name()}")
    print(f"Dessert: {veg_dessert.get_name()}")

    # Create a non-vegetarian meal
    non_veg_factory = NonVegetarianMealFactory()
    non_veg_starter = non_veg_factory.create_starter()
    non_veg_main_course = non_veg_factory.create_main_course()
    non_veg_dessert = non_veg_factory.create_dessert()

    print("\nNon-Vegetarian Meal:")
    print(f"Starter: {non_veg_starter.get_name()}")
    print(f"Main Course: {non_veg_main_course.get_name()}")
    print(f"Dessert: {non_veg_dessert.get_name()}")
    

main()