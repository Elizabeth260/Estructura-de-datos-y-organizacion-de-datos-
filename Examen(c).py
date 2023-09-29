def guardar_en_espiral(matriz):
    resultado = []
    while matriz:
        # Moverse hacia la derecha y guardar en la pila
        resultado.extend(matriz.popleft())
        if matriz:
            # Moverse hacia abajo y guardar en la pila
            for fila in matriz:
                resultado.append(fila.pop())
            # Moverse hacia la izquierda y guardar en la pila
            resultado.extend(reversed(matriz.pop()))
        if matriz:
            # Moverse hacia arriba y guardar en la pila
            for fila in reversed(matriz):
                resultado.append(fila.popleft())
    return resultado

def imprimir_matriz_en_espiral(matriz):
    resultado = guardar_en_espiral(matriz)
    n = len(matriz)
    m = len(matriz[0]) if matriz else 0
    for i in range(n * m):
        print(resultado[i], end="\t")
        if (i + 1) % m == 0:
            print()

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_deque = deque([deque(fila) for fila in matriz_ejemplo])

imprimir_matriz_en_espiral(matriz_deque)
