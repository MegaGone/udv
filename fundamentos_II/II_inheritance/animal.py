class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age

    def eat(self):
        print(f"{self.name} it's eating.")

    def sleep(self):
        print(f"{self.name} it's sleeping.")

    def walk(self):
        print(f"{self.name} it's walking.")
    
    def roar(self):
        print(f"{self.name} it's roaring.")

    def get_age(self):
        return self._age
    
    def set_age(self, new_age: int):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Age cannot be negative.")