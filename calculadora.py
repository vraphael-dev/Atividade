contador = 0
soma = int()
sub = int()
div = int()
mut = int()

while contador != 1:
    print("1, para Adição")
    print("2, para Subtração")
    print("3, para Multiplicação")
    print("4, para Divisão")
    print("5, para Sair")
    decisao = int(input("Digite a operação que deseja com as opções citadas: "))

    if decisao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"O resultado da equação é: ", soma)
    elif decisao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        sub = num1 - num2
        print(f"O resultado da equação é: ", sub)
    elif decisao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        mut = num1 * num2
        print(f"O resultado da equação é: ", mut)
    elif decisao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        div = num1 / num2
        print(f"O resultado da equação é: ", div)
    elif decisao == 5:
        print("Programa encerrado.")
        contador = 1
    else: 
        print("Número inválido!")