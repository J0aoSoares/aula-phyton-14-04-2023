num1 = int(input("Diga um número: "))
num2 = int(input("Diga outro número: "))
menor = num1
maior = num2
if num2<num1:
    menor = num2
    maior = num1
while menor<=maior:
    print(menor)
    menor+=1