# CAÇA LETRAS
# PEÇA AO USUARIO PARA DIGITAR UMA FRASE E UMA LETRA.
# USANDO WWHILE, ENCONTRE TODAS AS POSIÇÕES INDICES ONDE A LETRA
# APARECE NA FRASE E IMPRIMA-AS.
# VOCÊ PODE USAR STRING COMO LISTA DE CARACTERES

frase = input("Digite uma frase de sua preferência: ").lower()
letra = input("Agora digite uma letra: ")
indice = 0
contador = 0

while indice > len(frase):
   if frase[indice] == letra:
      print("Letra encontada na posição: ", indice)
   else:
      contador += 1
      indice +=1
      break
print(" A frase apareceu", contador, "vez(es).")     
   