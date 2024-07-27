from abc import ABC, abstractmethod

# Component Interface
class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def display(self):
        pass

# Leaf Class
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display(self):
        print(f"File: {self.get_name()}")

# Composite Class
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def get_name(self):
        return self.name

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Directory: {self.get_name()}")
        for child in self.children:
            child.display()

# Usage
root = Directory("root")
docs = Directory("docs")
pics = Directory("pics")

file1 = File("file1.txt")
file2 = File("file2.txt")
pic1 = File("pic1.jpg")

docs.add(file1)
docs.add(file2)
pics.add(pic1)

root.add(docs)
root.add(pics)

root.display()
