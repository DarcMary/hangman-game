import random
from words import categories

categoria_escolhida = random.choice(list(categories.keys()))
palavra_escolhida = random.choice(categories[categoria_escolhida])

letras = list(palavra_escolhida)
palavra_oculta = ["_" if letra != " " else " " for letra in palavra_escolhida]

print(f"Categoria: {categoria_escolhida}")
print("Palavra: ", " ".join(palavra_oculta))

while "_" in palavra_oculta:
    letra_usuario = input("Digite uma letra:").lower()

    if letra_usuario in letras:
        print(f"A letra '{letra_usuario}' está na palavra!")
        for i in range(len(letras)):
            if letras[i] == letra_usuario:
                palavra_oculta[i] = letra_usuario
    else:
        print(f"A letra '{letra_usuario}' não está na palavra.")

    print("Palavra: ", " ".join(palavra_oculta))

print("Parabéns, você descobriu a palavra!")
