opc = 0

while True:
    print("\n--- Jogo ---")
    print("Jogador 1, escolha:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Sair do Jogo")
    
    opc = int(input("Introduza a opção (1-4): "))

    match opc:
        
        case 1:
            print("Jogador 1 escolheu: PEDRA")
            j2 = int(input("Jogador 2, escolha (1-Pedra, 2-Papel, 3-Tesoura): "))
            
            if j2 == 1:
                print("EMPATE!")
            elif j2 == 2:
                print("Jogador 2 VENCE!")
            elif j2 == 3:
                print("Jogador 1 VENCE!")
            else:
                print("Opção inválida.")

        case 2:
            print("Jogador 1 escolheu: PAPEL")
            j2 = int(input("Jogador 2, escolha (1-Pedra, 2-Papel, 3-Tesoura): "))
            
            if j2 == 1:
                print("Jogador 1 VENCE!")
            elif j2 == 2:
                print("EMPATE!")
            elif j2 == 3:
                print("Jogador 2 VENCE!")
            else:
                print("Opção inválida.")

        case 3:
            print("Jogador 1 escolheu: TESOURA")
            j2 = int(input("Jogador 2, escolha (1-Pedra, 2-Papel, 3-Tesoura): "))
            
            if j2 == 1:
                print("Jogador 2 VENCE!")
            elif j2 == 2:
                print("Jogador 1 VENCE!")
            elif j2 == 3:
                print("EMPATE!")
            else:
                print("Opção inválida.")

        case 4:
            print("Adeus...")
            break 

        case _:
            print("Opção inválida! Tente novamente.")
