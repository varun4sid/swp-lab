"""MEDIATOR PATTERN
A company builds an online team chat application (similar to Slack /
WhatsApp groups / MS Teams).
Features to be supported:
• Users join chat rooms
• Send messages to group
• Private messaging
• Notifications
• User join/leave alerts
"""

from abc import ABC, abstractmethod

class ChatRoomMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user):
        pass

    @abstractmethod
    def add_user(self, user):
        pass
    

class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users = []

    def send_message(self, message: str, sender):
        for u in self.users:
            if u != sender:
                u.receive_message(message, sender)

    def add_user(self, user):
        self.users.append(user)
        
        
class User:
    def __init__(self, name: str, chat_room: ChatRoomMediator):
        self.name = name
        self.chat_room = chat_room
        self.chat_room.add_user(self)

    def send_message(self, message: str):
        print(f"{self.name} sends message: {message}")
        self.chat_room.send_message(message, self)

    def receive_message(self, message: str, sender):
        print(f"{self.name} received message from {sender.name}: {message}")
        
        
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Harry", chat_room)
    user2 = User("Hermione", chat_room)
    user3 = User("Ron", chat_room)
    
    user1.send_message("Where is platform 9 and 3 quarters?")
    user2.send_message("It's in King's Cross Station, London.")
    user3.send_message("No way, Sherlock!")