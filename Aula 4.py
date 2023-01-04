def condicoes(X, imc):
    if X >= 18 and X <= 32:
        print("Vimos que vc ainda é jovem, seu imc é: ", imc)
        if imc >= 18.5 and imc <= 25:
            print("Seu imc está na média")
        elif imc < 18.5:
            print("Está abaixo do peso")
        elif imc > 25:
            print("Está com sobrepeso")

    elif X >= 33 and X <= 61:
        print("Vemos que vc ja é adulto, e seu imc é: ", imc)
        if imc >= 18.5 and imc <= 25:
            print("Seu imc está na média")
        elif imc < 18.5:
            print("Está abaixo do peso")
        elif imc > 25:
            print("Está com sobrepeso")

    elif X > 61:
        print("Vimos que vc ja é idoso, seu imc é: ", imc)
        if imc >= 18.5 and imc <= 25:
            print("Seu imc está na média")
        elif imc < 18.5:
            print("Está abaixo do peso")
        elif imc > 25:
            print("Está com sobrepeso")

    elif X < 18:
        print("Vc ainda é muito jovem")

qntEntrev = 0
somaX = 0
somaPeso = 0
somaAltura = 0

Y = 1
while Y != 0:
    
    X = float(input("Digite a sua idade\n"))
    peso = float(input("Qual o seu peso\n"))
    altura = float(input("Qual sua altura?\n"))
    # sexo = int(input("Digite o número referente ao seu sexo\n"))
    somaX = somaX + X
    somaPeso = somaPeso + peso
    somaAltura = somaAltura + altura
    qntEntrev += 1
    
    imc = float(peso / (altura*altura))
    
    condicoes(X, imc)
        
    Y = float(input("Vc gostaria de continuar fazendo a pesquisa?\n 1 - Sim\n 0 - Não\n"))


print()
print("A quantidade de entrevistados foi: ", qntEntrev)
print("A média de idades é: ", (somaX/qntEntrev))
print("A média de peso é: ", (somaPeso/qntEntrev))
print("A média de altura é: ", (somaAltura/qntEntrev))


