nome = str(input("Nome completo: "))
idade = int(input("Idade: "))

if idade >= 18:
    print(f"{nome} Você possui idade para fazer um cartão de crédito")
else:
    print(f"{nome} Você não possui idade para fazer um cartão de crédito")