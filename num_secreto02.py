numero_secreto = 50
for num in range(7):
  tentativa=int(input("Adivinhe qual é o número secreto?"))
  if tentativa==numero_secreto:
     print("Parabéns você acertou!!!")
     break
  
  elif tentativa <=45 :
     print("Mais!!!")

  elif tentativa >45 and tentativa <=49 :
     print("Está Quase lá!!!")

  elif tentativa >= 51 and tentativa <= 99 :
     print("Menos!!!")
else:
     print("Game Over :(")