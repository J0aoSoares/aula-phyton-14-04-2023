num = int(input("Me diga um número: "))
while num <=10:
    i =1
    print(f"A tabuada do {num} é: ")
    while i<=10:
        print(f"{num}*{i}={num*i}")
        i+=1
    num+=1