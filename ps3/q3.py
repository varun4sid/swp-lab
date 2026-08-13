"""
Implement file explorer functionality to support navigation – folders can
contain files or sub-folders and so on.
"""

from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass
    
    
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")
        
        
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)
            
            
def main():
    root = Folder("Root")
    folder1 = Folder("Folder1")
    folder2 = Folder("Folder2")
    folder3 = Folder("Folder3")
    file1 = File("File1.txt")
    file2 = File("File2.txt")
    file3 = File("File3.txt")
    file4 = File("File4.txt")

    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    folder2.add(folder3)
    folder3.add(file4)
    root.add(folder1)
    root.add(folder2)

    root.display()
    

main()