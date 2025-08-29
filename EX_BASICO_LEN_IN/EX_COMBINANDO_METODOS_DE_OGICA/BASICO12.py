# VALIDADOR DE SENHA 2
# PEÇA AO USU PARA DIGITAR UMA SENHA.
# VERIFIQUE SE A SENHA CONTÉM A PALAVRA SENHA.
# SE SIM IMPRIMA SENHA FRACA, CASO CONTRARIO,
# IMPRIMA SENHA FORTE

senha = input("Cadastre sua senha:")
if "senha" in senha:
    print("Senha fraca!")
else:
   print("Senha forte!") 
