# VERIFICADOR DE PALINDROMO
#PEÇA AO USUSARIO UMA PALAVRA. VERIFIQUE SE É OU NÃO UM PALINDROMO.

palavra = input("Digite uma palavra")
inverso =""
indice = len(palavra) -1

while indice >= 0:
    inverso += palavra[indice]
    indice-=1
if palavra == inverso:
    print("A palavra é um palídromo!")    
else:
    print("A palavra não é um palíndromo!")    
