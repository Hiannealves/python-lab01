# CONTADOR DE VOGAIS
# PEÇA AO USUÁRIO PARA DIGITAR UMA PALAVRA.
# USANDO WHILE , CONTE E IMPRIMA O NÚMERO TOTAL DE VOGAIS(A, E, I, O ,U) NA PALAVRA.

palavra = input("Digite uma palavra").lower()
contador_vogais = 0
indice = 0
 
while indice < len(palavra):
    if palavra[indice] in "a e i o u":
        contador_vogais +=1
    indice+=1

    print("número total de vogais", contador_vogais)    

