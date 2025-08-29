# VERIFICADOR DE STRING
#PEÇA AO USUÁRIO PARA DIGITAR UMA FRASE E UMA PALAVRA.
# VERIFIQUE SE A PALAVRA ESTÁ PRESENTE NA FRASE.

frase=input("Digite sua frase: ").lower()
palavra = input("Digite sua palavra: ").lower()

if palavra in frase:
    print("A palavra", palavra, "está presente na frase.")

else:
    print("A palavra", palavra, "não está presente na frase.")

