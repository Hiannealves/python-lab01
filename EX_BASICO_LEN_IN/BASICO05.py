# VERIFICADOR DE EMAIL
# PEÇA AO USUSÁRIO QUE DIGITE UM E-MAIL. VERIFIQUE E IMPRIMA SE O EMAIL CONTÉM O CARACTER "@"

email = input("Digite o seu e-mail: ").lower()
 
if "@" in email:
    print("E-mail cadastrado com sucesso!")
else:
    print("Digite um endereço de e-mail válido.")
