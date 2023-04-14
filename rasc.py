'''
num1 = int(input("Me diga um número: "))
num2 = int(input("Me diga outro número: "))
num3 = int(input("Me diga outro número: "))
num4 = int(input("Me diga outro número: "))
num5 = int(input("Me diga outro número: "))
soma = num1+num2+num3+num4+num5

media = soma/5

resposta = input("O que você quer fazer? (soma ou média): ")

if resposta == "soma":
    print(f"Então o resultado é : {soma}")

elif resposta == "média":
    print(f"Então a resposta é: {media}")
else:
    if resposta != "soma" or resposta != "média":
        print("Então vai se foder, não quer brincar entao nao desce pro play arrombado")


i = 0
soma = 0

while i < 5:
    num = input("Me diga sua nota: ")
    while not num.isnumeric():
        num = input("Tem que ser número: ")
    soma += int(num)
    i+= 1
media = soma/i

print(f"A soma é : {soma} e a média é: {media} ")

'''