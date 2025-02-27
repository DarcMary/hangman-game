import random

palavras = ["computador", "programação", "software", "hardware", "internet", "inteligência artificial", "criptografia", "cibersegurança", "desenvolvimento", "algoritmo", "backend", "frontend", "javascript", "python", "react", "database", "servidor", "cloud", "rede", "dados", "bit", "byte", "blockchain", "criptomoeda"]

palavra_aleatoria = random.choice(palavras)

letras = list(palavra_aleatoria)
palavra_oculta = ["_" if letra != " " else " " for letra in palavra_aleatoria]

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
