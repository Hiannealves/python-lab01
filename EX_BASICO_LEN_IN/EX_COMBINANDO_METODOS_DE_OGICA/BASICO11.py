# VALIDADOR DE SENHA 1
# PEÇA AO USU PARA DIGITAR UMA SENHA. VERIFIQUE SE A SENHA TEM PELO MENOS 8 CARACTERES. 
# IMPRIMA SENHA VÁLIDA OU SENHA INVÁLIDA.

senha = input("Digite sua senha: ")

if len(senha) >= 8:
    print("Senha válida!")
else:
    print("Senha inválida!")