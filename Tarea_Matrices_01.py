# ----------------------------------------------------------------------------------
matriz = []

num1 = 5

for i in range(3):
    fila = []
    for j in range(3):
        # Genero número aleatorio usando una fórmula simple
        # num = (a * num1 + c) para a=i+1 c:i+1
        num = ((i + 1) * num1 * (j + 1))
        fila.append(num)
    matriz.append(fila)

print("Matriz 3x3 con números aleatorios :")
for fila in matriz:
    print(fila)
# ----------------------------------------------------------------------------------
