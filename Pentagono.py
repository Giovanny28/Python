import math

# Pedir al usuario la medida del lado
lado = float(input("Ingresa la medida del lado del pentágono: "))

# Calcular perímetro
perimetro = 5 * lado

# Calcular apotema (fórmula para pentágono regular)
apotema = lado / (2 * math.tan(math.pi / 5))

# Calcular área
area = (perimetro * apotema) / 2

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Perímetro del pentágono: {perimetro:.2f}")
print(f"Apotema del pentágono: {apotema:.2f}")
print(f"Área del pentágono: {area:.2f}")
