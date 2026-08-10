import copy

class CoverLetter:
    def __init__(self, body):
        self.body = body
        self.recipient_name = ""
        
    def clone(self):
        return copy.deepcopy(self)
    
    def set_recipient(self, recipient_name):
        self.recipient_name = recipient_name
        
    def render(self):
        header = f"To:\n{self.recipient_name}\n\n"
        return header + self.body
    

class BulkLetterGenerator:
    def __init__(self, template):
        self.template = template
        
    def generate_letters(self, recipient_names):
        letters = []
        
        for name in recipient_names:
            letter = self.template.clone()
            letter.set_recipient(name)
            letters.append(letter.render())
            
        return letters
    
    
def main():
    standard_template = "Hello. Thank you for sponsoring my work! I am grateful for your support."
    cover_letter_template = CoverLetter(standard_template)
    
    generator = BulkLetterGenerator(cover_letter_template)
    recipient_names = ["Alice", "Bob", "Charlie"]
    letters = generator.generate_letters(recipient_names)
    
    for letter in letters:
        print(letter)
        
        
main()