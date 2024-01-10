class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

users = [User('fuck', 10) for i in range(100)]
