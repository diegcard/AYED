class Node():
    def __init__(self,val,izquierda = None, derecha = None):
        self.val = val
        self.izquierda = izquierda
        self.derecha = derecha

def Arbol_Minimo(root):
    if root is None:
        return None
    if root.izquierda is None:
        return root.val
    return Arbol_Minimo(root.izquierda)

def Arbol_Maximo(root):
    if root is None:
        return None
    if root.derecha is None:
        return root.val
    return Arbol_Maximo(root.derecha)

