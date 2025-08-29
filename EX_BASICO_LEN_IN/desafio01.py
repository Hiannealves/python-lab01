while True:
    A = input("Digite o lado A: ")
    B = input("Digite o lado B: ")
    C = input("Digite o lado C: ")
    
    if A.isdigit() and B.isdigit() and C.isdigit():
        A,B,C= int(A), int(B), int(C)
        if A>0 and B>0 and C>0:
         break
    else:
      print("Digite apenas números inteiros positivos!")

if( A <B+ C and B < A+ C and C < A + B) and (A >abs(B - C)  and B > abs(A - C) and C > abs(A -B)):
    print(" os valores podem formar um triângulo!")
else:
    print(" Os valores NÃo podem formar um triângulo")    



