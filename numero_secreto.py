numero_secreto = 22
for num in range(5):
  tentativa=int(input("Adivinhe qual é o número secreto?"))
  if tentativa==numero_secreto:
     print("Parabéns você acertou!!!")
     break
  elif tentativa >= numero_secreto:
     print("Muito alto!!!")
  elif tentativa <= numero_secreto:
     print("Muito baixo!!!")      
else:
     print("Game Over :(")