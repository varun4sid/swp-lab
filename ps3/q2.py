"""
As part of home automation we need to control different appliances
such as :
a. Lights
b. Fans
c. TV, etc

These appliances need to be controlled with different types of
operations such as :
a. On or Off (toggle)
b. Increase or decrease (regulator)

"""

from abc import ABC, abstractmethod

class Appliance(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def toggle(self):
        pass

    @abstractmethod
    def regulate(self, level):
        pass


class Light(Appliance):
    def toggle(self):
        print(f"{self.name} light toggled.")

    def regulate(self, level):
        print(f"{self.name} light brightness set to {level}.")
        
        
class Fan(Appliance):
    def toggle(self):
        print(f"{self.name} fan toggled.")

    def regulate(self, level):
        print(f"{self.name} fan speed set to {level}.")
        
        
class TV(Appliance):
    def toggle(self):
        print(f"{self.name} TV toggled.")

    def regulate(self, level):
        print(f"{self.name} TV volume set to {level}.")
        
        
class RemoteControl:
    def __init__(self, appliance):
        self.appliance = appliance

    def toggle(self):
        self.appliance.toggle()

    def regulate(self, level):
        self.appliance.regulate(level)
        
        
def main():
    appliances = {
        "light": Light("Living Room"),
        "fan": Fan("Bedroom"),
        "tv": TV("Home Theater")
    }

    while True:
        appliance_type = input("Enter the appliance type (light, fan, tv) or 'exit' to quit: ").lower()
        if appliance_type == 'exit':
            break

        if appliance_type in appliances:
            remote = RemoteControl(appliances[appliance_type])
            action = input("Enter action (toggle, regulate): ").lower()

            if action == "toggle":
                remote.toggle()
            elif action == "regulate":
                level = input("Enter level (e.g., brightness for light, speed for fan, volume for tv): ")
                remote.regulate(level)
            else:
                print("Invalid action. Please try again.")
        else:
            print("Invalid appliance type. Please try again.")


main()