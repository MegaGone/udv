class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, element):
        self.elementos.append(element)

    def desapilar(self):
        if not self.pila_vacia():
            return self.elementos.pop()

    def pila_vacia(self):
        return len(self.elementos) == 0
