class Pila(object):
    """Implementación de una Pila."""
    def __init__(self, *args):
        self.contenido = []
        for arg in args:
            self.contenido.append(arg)
        
    def __str__(self) -> str:
        rep = 'El contenido de la pila es ' + str(self.contenido)
        return rep

    def top(self):
        return self.contenido[-1]    
    
    def push(self, *args):
        for arg in args:
            self.contenido.append(arg)
        
    def pop(self):
        try:
            return self.contenido.pop()
        except IndexError:
            raise Exception("La pila está vacía")

    def len(self):
        "Devuelve la cantidad de objetos en la pila"
        return len(self.contenido)

    def is_empty(self):
        "Indica si la pila está vacía"
        if not self.contenido:
            return "La pila está vacía"
        else:
            return "Hay objetos en la pila"

        
            

