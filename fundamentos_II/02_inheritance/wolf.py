from animal import Animal

class Wolf(Animal):
    def roar(self):
        return super().roar()
    
    def howl(self):
        print(f"{self.name} was howling.")