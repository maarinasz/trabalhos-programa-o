def organizar_nomes_por_ultima_letra(lista_nomes):
    lista_ordenada = sorted(lista_nomes, key=lambda x: x[-1])
    return lista_ordenada

nomes = ["Alexandre", "Alice", "André", "Arthur", "Arthur", "Artur", "Augusto", "Bernardo", "Bernardo", "Bruno", "Davi", "Diego", "Eduardo", "Fabrício", "Felipe", "Fernando", "Francisco", "Francisco", "Gabriel", "Gabriel", "Giovanna", "Giovanni", "Guilherme", "Guilherme", "Hector", "Henrique", "Inácio", "João", "João", "Joaquim", "Júlia", "Lauren", "Leonardo", "Leonardo", "Lucas", "Marina", "Matheus", "Matheus", "Paula", "Pedro", "Pedro", "Pedro", "Pedro", "Rafael", "Regis", "Sofia", "Stella", "Thiago", "Valentina", "Vicente", "Lucas"]

nomes_ordenados = organizar_nomes_por_ultima_letra(nomes)

print(nomes_ordenados)
