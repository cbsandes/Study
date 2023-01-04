def somas(A, X, Y, Z):
    soma1 = apito*X
    soma2 = bola*Y
    soma3 = cartao*Z

    # if X > 0 or Y > 0 or Z > 0:
    if X > 0:
        print("Então vc deseja comprar", X, "apitos, ? O preço ficaria", soma1)
        if Y > 0:
            print("Então vc deseja comprar", Y, "bolas? O preço ficaria", soma2)
            if Z > 0:
                print("Então vc deseja comprar", Z, "cartões? O preço ficaria", soma3)
    else:
        print("Então vc não quer comprar nada né")

    if (X + Y + Z) > 0:
        print("O resultado de suas compras deram", soma1+soma2+soma3 ,"reais")
    else:
        print("Vou deixar vc a sós para decidir")


apito = 1.50
bola = 10
cartao = 4

A = str(input("Bom dia, digite o seu nome \n"))
X = float(input("quantos apitos vc deseja comprar? \n"))
Y = float(input("Quantas bolas vc deseja comprar? \n"))
Z = float(input("Quantos cartões vc deseja comprar? \n"))

somas(A, X, Y, Z)
