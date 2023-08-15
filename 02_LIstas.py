# Listas
# Listas são uma forma de armazenar mais de um valor em uma
# unica variavel. Os valores podem ser de tipos diferentes.

# Uma lista de numeros
valores = [2, 3, 5, 7, 9, 11]

# Uma lista com valores de tipos variados
legumes = ["batata", "Tomate", "Abobrinha", "Cenoura"]

# Operações sobre listas

# 1) PERCURSO: significa percorrer a lista do primeiro ao
# ultimo elemento, fazendo algo com cada um deles.

# Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-" * 40)  # Traço de 40 hifens

# Imprimindo o dobro do valor de cada elemento da lista
for x in valores:
    print(x * 2)

print("-" * 40)  # Traço de 40 hifens

# 2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA PSIÇÃO ESPECIFICADA
# Paramentros:
# 1°: a posição odne sera inserido o novo elemento
# 2°: o novo elemento a ser inserido

legumes.insert(2, "Mandioquinha")
print(legumes)
legumes.insert(0, "Beterraba")
print(legumes)

print("-" * 40)  # Traço de 40 hifens

# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECIFICA

print("Elemento na QUARTA posição", valores[3])
print("Elemento na PRIMEIRA posição", valores[0])
print("Elemento na ULTIMA posição", valores[-1])
print("Elemento na PENULTIMA posição", valores[-2])
