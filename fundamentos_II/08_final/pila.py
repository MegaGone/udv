class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, element):
        self.elementos.append(element)

    # UTILIZAMOS 0 PARA APLICAR FIFO
    def desapilar(self):
        if not self.pila_vacia():
            return self.elementos.pop(0)

    def pila_vacia(self):
        return len(self.elementos) == 0
