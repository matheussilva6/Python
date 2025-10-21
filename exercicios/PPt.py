opc = 0

while True:
    print("1 - para receber um bom dia")
    print("2 - para receber uma boa tarde ")
    print("3 - para receber um boanoite ")
    print("4 - sair")
    opc=int(input("Introduza a opção (1-4): "))

    match opc:
        case 1:
            print("Bom dia!")
        case 2:
            print("Boa tarde!")
        case 3:
            print("Boa noite!")
        case 4:
            print("Adeus...")
            break