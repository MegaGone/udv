class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    # VALOR 0 EN MÉTDO POP ELIMINA EL PRIMER ELEMENTO DEL ARRAY
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
