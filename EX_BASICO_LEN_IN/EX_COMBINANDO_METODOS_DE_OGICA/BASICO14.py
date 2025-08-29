""" INVERSOR DE PALAVRAS
PEÇA AO USUSARIO UMA PALAVRA
USANDO LEN E UM LAÇO WHILE, IMPRIMA A PALAVRA DE TRAS PARA FRENTe"""

palavra=input("Digite uma palavra: ").lower()
indice = len(palavra)-1
inverso = ""

while indice >=0:
    inverso+=palavra[indice]
    indice-=1
print("Palavra invertida", inverso)    
