# X = 1

# while X != 0:
#     A = str(input("Digite seu nome\n"))
#     B = str(input("Digite seu sobrenome\n"))
#     C = str(input("Digite seu cargo\n"))
#     # D = str(input("Digite seu salário"))
#     if C == "Engenheiro":
#         print("Olá", A, B, "seu salario é de R$6,000")
#         print("Como Engenheiro, vc deve pagar 15 porcento de IR, que seria R$", 6000*(15/100))
#     elif C == "Médico":
#         print("Olá", A, B, "seu salário é de R$10,000")
#         print("Como Médico, vc deve pagar 20 porcento de IR, que seria R$", 10000*(20/100))
#     elif C == "Advogado":
#         print("Olá", A, B, "seu salário é de R$4,500")
#         print("Como Advogado, vc deve pagar 10 porcento de IR, que seria R$", 4500*(10/100))
#     elif C == "Programador":
#         print("Olá", A, B, "seu salário é de R$ 10,000")
#         print("Como Programador, vc deve pagar 20 porcento de IR, que seria R$", 10000*(20/100))    
    
#     X = int(input("Você deseja continuar?\n 1 - Sim\n 0 - Não\n"))


# def nome(A):
#     print(A)

# def sobrenome(B):
#     print(B)

# def cargo(C):
#     print("Olá, notamos que vc é um(a)", C)

def relatorioSalario(nome, sobrenome, cargo, salario):
    print("Olá", nome, sobrenome, "como", cargo, "seu salário é: ",salario)
    if salario <= 2000:
        print("Você está isento do imposto de renda")
    elif salario > 2000 and salario <= 3500:
        print("5 porcento de retirada do valor que é", (5/100)*salario)
    elif salario > 3500 and salario <= 6000:
        print("10 porcento de retirada do valor que é", (10/100)*salario)
    elif salario > 6000 and salario <= 8000:
        print("15 porcento de retirada do valor que é", (15/100)*salario)
    elif salario > 8000 and salario <= 10000:
        print("20 porcento de retirada do valor que é", (20/100)*salario)
    elif salario > 10000:
        print("25 porcento de retirada do valor que é", (25/100)*salario)

X = 1
while X != 0:
        
    nome = str(input("Digite seu nome\n")) 
    sobrenome = str(input("Digite seu sobrenome\n"))
    cargo = str(input("Digite seu cargo\n"))
    salario = int(input("Digite seu salário\n"))
    # nome(A)
    # sobrenome(B)
    # cargo(C)
    relatorioSalario(nome, sobrenome, cargo, salario)
    X = int(input("\nVocê quer continuar no processo?\n1 - Sim\n0 - Não\n"))