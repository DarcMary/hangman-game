import random

# Lista de palavras
palavras = ["computador", "programação", "inteligencia", "desenvolvimento", "python"]

# Função para separar sílabas (simplificada)
def separar_silabas(palavra):
    # Padrões simples para separar as sílabas, como exemplo
    silabas = []
    palavra = palavra.lower()
    vogais = "aeiouáéíóúãõ"
    ultima_silaba = ""
    
    for i, letra in enumerate(palavra):
        if letra in vogais:
            if ultima_silaba:
                silabas.append(ultima_silaba)
            ultima_silaba = letra
        else:
            ultima_silaba += letra
    
    # Adiciona a última sílaba
    if ultima_silaba:
        silabas.append(ultima_silaba)
    
    return silabas

# Seleciona uma palavra aleatória
palavra_aleatoria = random.choice(palavras)
print(f"Palavra escolhida: {palavra_aleatoria}")

# Separa a palavra em sílabas
silabas = separar_silabas(palavra_aleatoria)
print(f"Sílaba(s): {silabas}")

# Percorrendo as sílabas
for silaba in silabas:
    print(f"Sílaba: {silaba}")