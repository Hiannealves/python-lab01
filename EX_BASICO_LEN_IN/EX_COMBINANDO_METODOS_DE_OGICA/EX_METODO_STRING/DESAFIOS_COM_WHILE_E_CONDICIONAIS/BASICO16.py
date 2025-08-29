# primeiro e ultimo caractere
# PEÇA AO USUARIO PARA DIGITAR UMA PALAVRA. SE A PALAVRA TIVER MAIS DE 5 CARACTERES,
# # IMPRIMA O PRIMEIRO E ULTIMO CARACTERE. CASO CONTRARIO
# IMPRIMA A PALAVRA INTEIRA.

palavra = input("digite uma palavra: ").lower()

while True:
    if len(palavra) == 5:
        print("Primeiro caractere" ,palavra[0])
        print("Primeiro caractere" ,palavra[4])
        break
    else:
        print(palavra)    
    break