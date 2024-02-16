#Demetrio Torres Yanahi
def contarValles(lista):
    valles = 0
    contador = 0
    for paso in lista:
        if paso == 'U':
            contador += 1
            if contador == 0:
                valles += 1
        else:
            contador -= 1
    return valles


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)

    def preorden(self):
        return self._preorden_recursivo(self.raiz, [])

    def _preorden_recursivo(self, nodo_actual, lista):
        if nodo_actual:
            lista.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierda, lista)
            self._preorden_recursivo(nodo_actual.derecha, lista)
        return lista

    def inorden(self):
        return self._inorden_recursivo(self.raiz, [])

    def _inorden_recursivo(self, nodo_actual, lista):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda, lista)
            lista.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha, lista)
        return lista

    def postorden(self):
        return self._postorden_recursivo(self.raiz, [])

    def _postorden_recursivo(self, nodo_actual, lista):
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierda, lista)
            self._postorden_recursivo(nodo_actual.derecha, lista)
            lista.append(nodo_actual.valor)
        return lista

# Ejemplo de uso
arbol = ArbolBinarioOrdenado()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(4)

print("Preorden:", arbol.preorden())
print("Inorden:", arbol.inorden())
print("Postorden:", arbol.postorden())

print("Ejemplo problema del caminante: \"UDDDUUDUUDDDUDUUUD\":")
print("Número de valles: " + str(contarValles("UDDDUUDUUDDDUDUUUD")))
