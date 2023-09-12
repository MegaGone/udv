from animal import Animal

class Lion(Animal):
    def roar(self):
        return super().roar()
    
    def purr(self):
        print(f"{self.name} was purring.")