from random import randint
lista = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
count = 0
count1 = 0
draw = 0
i = 1
nome = input("Digite seu nome!")

choice = input("Digite Y para melhor de 3 ou X para melhor de 5")

if choice == 'Y':

    while i < 3:
        perguntar = int(input('''Escolha uma opcao para se jogar: 

        [0] Pedra
        [1] Papel
        [2] Tesoura
 
        Digite sua escolha: '''))

        print(f'O computador escolheu: {lista[computador]}')
        print(f'O jogador escolheu: {lista[perguntar]}')

        if computador == 0:
            if perguntar == 0:
                print("Empate")
                draw += 1
                i += 1
            elif perguntar == 1:
                print(f'{nome} Venceu!')
                count += 1
                i += 1
            elif perguntar == 2:
                print("Computador venceu!")
                count1 += 1
                i += 1


        elif computador == 1:
            if perguntar == 0:
                print("Computador venceu!")
                count1 += 1
                i += 1
            elif perguntar == 1:
                print("Empate!")
                draw += 1
                i += 1
            elif perguntar == 2:
                print(f'{nome} Venceu!')
                count += 1
                i += 1


            elif computador == 2:
                if perguntar == 0:
                    print(f'{nome} Venceu!')
                    count += 1
                    i += 1
                elif perguntar == 1:
                    print("Computador venceu!")
                    count1 += 1
                    i += 1
                elif perguntar == 2:
                    print("Empate!")
                    draw += 1
                    i += 1

            if count > count1:
                print(f'{nome} Venceu a partida!')
            else:
                print("Computador venceu a partida!")



                

