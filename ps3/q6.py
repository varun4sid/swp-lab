"""
You’re building a text editor where:
a. Each character on screen is represented by a Character object.
b. Characters share common formatting like font, size, color (intrinsic
state).
c. Their position (x, y) is unique (extrinsic state).

Use flyweight pattern to implement this functionality.
"""

class Character:
    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def display(self, x, y):
        print(f"Character: '{self.char}' at ({x}, {y}) with font: {self.font}, size: {self.size}, color: {self.color}")
        

class CharacterFactory:
    _flyweights = {}

    @classmethod
    def get_character(cls, char, font, size, color):
        key = (char, font, size, color)
        if key not in cls._flyweights:
            cls._flyweights[key] = Character(char, font, size, color)
        return cls._flyweights[key]
    

def main():
    char1 = CharacterFactory.get_character('A', 'Arial', 12, 'Black')
    char2 = CharacterFactory.get_character('B', 'Arial', 12, 'Black')
    char3 = CharacterFactory.get_character('A', 'Arial', 12, 'Black')

    char1.display(10, 20)
    char2.display(30, 40)
    char3.display(50, 60)
    
    print("char1 and char3 are the same object:", char1 is char3)
    
    
main()