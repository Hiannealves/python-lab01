# CAÇA-PALAVRAS SIMPLES: PEÇA AO USUARIO PARA DIGITAR UMA FRASE
# CONTE QUANTAS VEZES A PALAVRA "A" APARECE NA FRASE USE LOWER

frase = input("Digite sua frase: ").lower()
contador = 0
indice = 0

while indice < len(frase):
    if frase[indice] in "a":
        contador +=1
    indice+=1
print("A letra 'a' apareu" ,contador, "vezes!")