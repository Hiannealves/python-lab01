# BUSCA E SUBISTITUIÇÃO
# PEÇA AO USUSARIO PARA DIGITAR UMA FRASE E DUAS PALAVRAS
# A PRIMEIRA PALAVRA É A QUE SERA BUSCADA NA FRASE, E A SEGUNDA É A QUE SERÁ SUBSTITUIDA.
# FAÇA A SUBISTITUIÇÃO E IMPRIMA A NOVA FRASE.

frase = input("digite uma frase: ").lower()
palavra1 = input("digite uma palavra: ").lower()
palavra2 = input("Digte uma seggunda palavra: ").lower()

if palavra1 in frase:
    nova_frase = frase.replace(palavra1,palavra2)
    print(nova_frase)
else:
    print("Digite uma palavra válida")
