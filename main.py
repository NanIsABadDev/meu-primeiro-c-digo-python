idade = int(input("Qual é a sua idade? Digite: "))

if idade <= 13:
    print("Você é criança")

elif idade <= 17:
    print("Você é adolescente")

elif idade <= 59:
    print("Você é adulto")

else:
    print("Você é idoso")