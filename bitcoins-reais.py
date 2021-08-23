exchange_rate = 267323.27

while(True):
    print("\n1- Bitcoins para reais")
    print("2- Reais para bitcoins")
    print("3- Fechar\n")
    option = input("Escolha uma opção: ")

    if option.isnumeric():
        operation = int(option)
        print("\n[SOMENTE NUMEROS E .]")

        if (operation == 3):
            print("\nFechando aplicação...")
            break

        if (operation == 1):
            bitcoins = float(input("Insira valor em bitcoins: "))
            reais = bitcoins * exchange_rate
            print(f"\n{bitcoins} bitcoins = R$ {reais:.3f}\n")

        elif (operation == 2):
            reais = float(input("Insira valor em reais: "))
            bitcoins = reais / exchange_rate
            print(f"\nR$ {reais} = {bitcoins:.4f} bitcoins\n")

        else:
            print("\nOpção inválida, tente novamente")
    else:
        print("\nOpção inválida, tente novamente")
