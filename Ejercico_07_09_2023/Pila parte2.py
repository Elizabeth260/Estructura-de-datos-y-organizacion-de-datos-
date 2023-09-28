class Pila:
    def __init__(self):
        # Crea una pila vacía.
        # La pila vacía se representa con una lista vacía
        self.items = []

    def apilar(self, x):
        # Agrega el elemento x a la pila.
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        # Devuelve el elemento tope y lo elimina de la pila. Si la pila está vacía levanta una excepción.
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        # Verifica si la pila está vacía.
        return len(self.items) == 0

    def mostrar(self):
        # Muestra todos los elementos de la pila.
        for elemento in self.items:
            print(elemento)
            
p = Pila()
op = 0

while op  != 5:
  print("1.- Apilar\n2.- Desapilar\n3.- Esta Vacia?\n4.- Imprimir Pila\n5.- Salir")
  op = int(input("-> "))
  if op == 1:
    tempApilar = input("Ingrese el elemento a apilar -> ")
    p.apilar(tempApilar)
  elif op == 2:
    p.desapilar()
  elif op == 3:
    p.es_vacia()
  elif op == 4:
    p.mostrar()
