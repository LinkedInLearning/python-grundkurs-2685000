class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return f"{self.name} ({self.alter})"