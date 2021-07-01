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
        pass


        
