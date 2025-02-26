"""
 Desenvolver um jogo clássico da forca onde o jogador tenta adivinhar
uma palavra oculta letra por letra.
 Pode incluir funcionalidades como seleção de categorias de palavras,
gráficos simples para representar o progresso do jogo e contagem de
tentativas.
 É um projeto que permite explorar estruturas de dados como listas e
strings, além de laços de repetição e condicionais.
"""
import random

palavras = ["computador", "programação", "software", "hardware", "internet", "inteligência artificial", "criptografia", "cibersegurança", "desenvolvimento", "algoritmo", "backend", "frontend", "javascript", "python", "html", "css", "react", "database", "servidor", "cloud", "rede", "dados", "bit", "byte", "blockchain", "criptomoeda"]

palavra_aleatoria = random.choice(palavras)

letras = list(palavra_aleatoria)
print(letras)

letra_usuario = input("Digite uma letra para começar o jogo:").lower()

if letra_usuario in letras:
    print(f"A letra '{letra_usuario}' está na palavra!")
else:
    print(f"A letra '{letra_usuario}' não está na palavra.")
