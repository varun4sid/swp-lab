"""COMMAND PATTERN
A company develops a Smart Home Automation System where a mobile app
or voice assistant can control multiple devices:
• Lights (ON/OFF, Brightness control)
• Fan (ON/OFF, Speed control)
• Air Conditioner (ON/OFF, Temperature control)
• Door Lock (Lock/Unlock)

Users can also:
• Schedule actions
• Undo last action
• Execute macro commands (e.g., “Good Night” turns off everything)
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def on(self):
        self.is_on = True
        print("Light is ON")

    def off(self):
        self.is_on = False
        print("Light is OFF")

    def set_brightness(self, brightness):
        if not 0 <= brightness <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        self.brightness = brightness
        print(f"Light brightness set to {brightness}%")


class Fan:
    def __init__(self):
        self.is_on = False
        self.speed = 0

    def on(self):
        self.is_on = True
        print("Fan is ON")

    def off(self):
        self.is_on = False
        print("Fan is OFF")

    def set_speed(self, speed):
        if not 0 <= speed <= 5:
            raise ValueError("Fan speed must be between 0 and 5")
        self.speed = speed
        print(f"Fan speed set to {speed}")


class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 24

    def on(self):
        self.is_on = True
        print("Air conditioner is ON")

    def off(self):
        self.is_on = False
        print("Air conditioner is OFF")

    def set_temperature(self, temperature):
        if not 16 <= temperature <= 30:
            raise ValueError("Temperature must be between 16 and 30 degrees")
        self.temperature = temperature
        print(f"Air conditioner temperature set to {temperature} degrees")


class DoorLock:
    def __init__(self):
        self.is_locked = True

    def lock(self):
        self.is_locked = True
        print("Door is locked")

    def unlock(self):
        self.is_locked = False
        print("Door is unlocked")


class DeviceCommand(Command):
    def __init__(self, device, action, reverse_action, state_attribute, desired_state):
        self.device = device
        self.action = action
        self.reverse_action = reverse_action
        self.state_attribute = state_attribute
        self.desired_state = desired_state
        self.previous_state = None

    def execute(self):
        self.previous_state = getattr(self.device, self.state_attribute)
        self.action()

    def undo(self):
        if self.previous_state == self.desired_state:
            self.action()
        else:
            self.reverse_action()


class LightOnCommand(DeviceCommand):
    def __init__(self, light):
        super().__init__(light, light.on, light.off, "is_on", True)


class LightOffCommand(DeviceCommand):
    def __init__(self, light):
        super().__init__(light, light.off, light.on, "is_on", False)


class LightBrightnessCommand(Command):
    def __init__(self, light, brightness):
        self.light = light
        self.brightness = brightness
        self.previous_brightness = None

    def execute(self):
        self.previous_brightness = self.light.brightness
        self.light.set_brightness(self.brightness)

    def undo(self):
        if self.previous_brightness is not None:
            self.light.set_brightness(self.previous_brightness)


class FanOnCommand(DeviceCommand):
    def __init__(self, fan):
        super().__init__(fan, fan.on, fan.off, "is_on", True)


class FanOffCommand(DeviceCommand):
    def __init__(self, fan):
        super().__init__(fan, fan.off, fan.on, "is_on", False)


class FanSpeedCommand(Command):
    def __init__(self, fan, speed):
        self.fan = fan
        self.speed = speed
        self.previous_speed = None

    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.set_speed(self.speed)

    def undo(self):
        if self.previous_speed is not None:
            self.fan.set_speed(self.previous_speed)


class AirConditionerOnCommand(DeviceCommand):
    def __init__(self, air_conditioner):
        super().__init__(
            air_conditioner, air_conditioner.on, air_conditioner.off, "is_on", True
        )


class AirConditionerOffCommand(DeviceCommand):
    def __init__(self, air_conditioner):
        super().__init__(
            air_conditioner, air_conditioner.off, air_conditioner.on, "is_on", False
        )


class TemperatureCommand(Command):
    def __init__(self, air_conditioner, temperature):
        self.air_conditioner = air_conditioner
        self.temperature = temperature
        self.previous_temperature = None

    def execute(self):
        self.previous_temperature = self.air_conditioner.temperature
        self.air_conditioner.set_temperature(self.temperature)

    def undo(self):
        if self.previous_temperature is not None:
            self.air_conditioner.set_temperature(self.previous_temperature)


class DoorUnlockCommand(DeviceCommand):
    def __init__(self, door_lock):
        super().__init__(door_lock, door_lock.unlock, door_lock.lock, "is_locked", False)


class DoorLockCommand(DeviceCommand):
    def __init__(self, door_lock):
        super().__init__(door_lock, door_lock.lock, door_lock.unlock, "is_locked", True)


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = list(commands)

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()


class RemoteControl:
    def __init__(self):
        self.last_command = None
        self.scheduled_commands = []

    def press(self, command):
        command.execute()
        self.last_command = command

    def undo(self):
        if self.last_command is not None:
            self.last_command.undo()
            self.last_command = None

    def schedule(self, command):
        self.scheduled_commands.append(command)

    def run_scheduled_commands(self):
        for command in self.scheduled_commands:
            self.press(command)
        self.scheduled_commands.clear()


def main():
    light = Light()
    fan = Fan()
    air_conditioner = AirConditioner()
    door_lock = DoorLock()

    remote = RemoteControl()
    remote.press(LightOnCommand(light))
    remote.press(LightBrightnessCommand(light, 60))
    remote.press(FanSpeedCommand(fan, 3))
    remote.press(TemperatureCommand(air_conditioner, 22))
    remote.undo()

    good_night = MacroCommand([
        LightOffCommand(light),
        FanOffCommand(fan),
        AirConditionerOffCommand(air_conditioner),
        DoorLockCommand(door_lock),
    ])
    remote.press(good_night)
    remote.undo()

    remote.schedule(AirConditionerOnCommand(air_conditioner))
    remote.schedule(TemperatureCommand(air_conditioner, 22))
    remote.run_scheduled_commands()


if __name__ == "__main__":
    main()