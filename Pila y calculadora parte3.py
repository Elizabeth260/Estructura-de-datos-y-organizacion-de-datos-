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

    def esPilaVacia(self):
        # Verifica si la pila está vacía.
        return len(self.items) == 0

    def mostrar(self):
        # Muestra todos los elementos de la pila.
        for elemento in self.items:
            print(elemento)

def calculadora_polaca(elementos):
    """Dada una lista de elementos que representan las componentes de
    una expresión en notacion polaca inversa, evalúa dicha expresión.
    Si la expresion está mal formada, levanta ValueError."""

    p = Pila()

    for elemento in elementos:
        print("DEBUG:", elemento)

        # Intenta convertirlo a número
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila ", numero)

        # Si no se puede convertir a número, debería ser un operando
        except ValueError:

            # Si no es un operando válido, levanta ValueError
            if elemento not in "+-*/ %" or len(elemento) != 1:
                raise ValueError("Operando inválido")

# Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.desapilar()
                print("DEBUG: desapila ", a1)
                a2 = p.desapilar()
                print("DEBUG: desapila ", a2)

            # Si hubo problemas al desapilar
            except ValueError:
                print("DEBUG: error pila faltan operandos")
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == " %":
                resultado = a2 % a1

            print("DEBUG: apila ", resultado)
            p.apilar(resultado)

 # Al final, el resultado debe ser lo único en la Pila
    res = p.desapilar()

    if p.esPilaVacia():
        return res
    else:
        print("DEBUG: error pila sobran operandos")
        raise ValueError("Sobran operandos")

def main():
    expresion = input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print(calculadora_polaca(elementos))

main()
