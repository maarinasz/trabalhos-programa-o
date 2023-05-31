lista = [2, 3, 7, 12, 2]
multiplicados = []

print("Valores originais da lista:")
for num in lista:
    print(num)

print("\nValores multiplicados por 2:")
for num in lista:
    resultado = num * 2
    multiplicados.append(resultado)
    print(resultado)

print("\nValores multiplicados em uma nova lista:")
print(multiplicados)
