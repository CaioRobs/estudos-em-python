while(True):
    print("1- Bitcoins para reais")
    print("2- Reais para bitcoins")
    print("3- Fechar\n")
    option = input("Escolha uma opção: ")

    if option.isnumeric():
        operation = int(option)

        if (operation == 1):
            bitcoins = float(input("\nvalor em bitcoins: "))
            reais = bitcoins * 267323.27
            print(f"\n{bitcoins} bitcoins = {reais} reais\n")

        elif (operation == 2):
            reais = float(input("\nvalor em reais: "))
            bitcoins = reais / 267323.27
            print(f"\n{reais} reais = {bitcoins} bitcoins\n")

        elif (operation == 3):
            print("\nFechando aplicação...")
            break

        else:
            print("\nOpção inválida\n")
    else:
        print("\nOpção inválida\n")
