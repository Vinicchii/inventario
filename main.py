import random

def inventario():
    mochila = ['lanches', ['sanduiche', 'kit kat', 'tostines'],  # índice 1
               'bebidas', ['água', 'nescafé', 'nesquik'],       # índice 3
               'jaqueta', ['jaqueta jeans'],                          # índice 5
               'cadernos', ['vinis guide', 'pythons guide']]          # índice 7
    
    carteira = ['documentos', ['RG', 'CPF'],                         # índice 1
                'cartões', ['cartão débito', 'cartão crédito'],      # índice 3
                'tickets', ['ticket estacionamento', 'ticket cinema']] # índice 5
    
    chaves = ['casa', ['acesso sua casa'],                           # índice 1
              'casa da vó', ['acesso a casa da vó']]                # índice 3
    
    return mochila, carteira, chaves

# Desempacotamento do inventário
mochila, carteira, chaves = inventario()

# Loop principal
while True:
    nav = int(input('O que você deseja acessar? mochila[0] carteira[1] chaves[2] sair[3]: '))
    
    if nav == 0:
        # Submenu da mochila
        while True:
            acesso = int(input('Qual item da mochila você quer? lanches[0] bebidas[1] jaqueta[2] cadernos[3] voltar[4]: '))
            if acesso == 0:
                while True:
                    pick = int(input('Qual lanche você deseja pegar? sanduiche[0] kit kat[1] tostines[2] voltar[3]: '))
                    if pick == 0:
                        print(f'Você pegou {mochila[1][0]}!')
                    elif pick == 1:
                        print(f'Você pegou {mochila[1][1]}!')
                    elif pick == 2:
                        print(f'Você pegou {mochila[1][2]}!')
                    elif pick == 3:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 1:
                while True:
                    pick = int(input('Qual bebida você quer pegar? água[0] nescafé[1] nesquik[2] voltar[3]: '))
                    if pick == 0:
                        print(f'Você pegou {mochila[3][0]}!')
                    elif pick == 1:
                        print(f'Você pegou {mochila[3][1]}!')
                    elif pick == 2:
                        print(f'Você pegou {mochila[3][2]}!')
                    elif pick == 3:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 2:
                print(f'Você pegou {mochila[5][0]}!')
            elif acesso == 3:
                while True:
                    pick = int(input('Qual caderno você deseja pegar? vinis-guide[0] pythons-guide[1] voltar[2]: '))
                    if pick == 0:
                        print(f'Você pegou {mochila[7][0]}!')
                    elif pick == 1:
                        print(f'Você pegou {mochila[7][1]}!')
                    elif pick == 2:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 4:
                break
            else:
                print('[ERRO] Você não digitou um número correspondente!')

    elif nav == 1:
        # Submenu da carteira
        while True:
            acesso = int(input('Qual item da carteira você quer pegar? documentos[0] cartões[1] tickets[2] voltar[3]: '))
            if acesso == 0:
                while True:
                    pick = int(input('Qual documento você deseja pegar? RG[0] CPF[1] voltar[2]: '))
                    if pick == 0:
                        print(f'Você pegou {carteira[1][0]}! Abreviação de Registro Geral.')
                    elif pick == 1:
                        print(f'Você pegou o {carteira[1][1]}! Conhecido como Certificado de Pessoa Física.')
                    elif pick == 2:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 1:
                while True:
                    pick = int(input('Qual cartão você deseja pegar? cartão débito[0] cartão crédito[1] voltar[2]: '))
                    if pick == 0:
                        print(f'Você pegou {carteira[3][0]}!')
                    elif pick == 1:
                        print(f'Você pegou {carteira[3][1]}!')
                    elif pick == 2:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 2:
                while True:
                    pick = int(input('Qual ticket você deseja pegar? ticket estacionamento[0] ticket cinema[1] voltar[2]: '))
                    if pick == 0:
                        print(f'Você pegou {carteira[5][0]}! Usado para validar o seu tempo em determinado estacionamento.')
                    elif pick == 1:
                        print(f'Você pegou {carteira[5][1]}! Possibilita acesso a um filme do cinema.')
                    elif pick == 2:
                        break
                    else:
                        print('[ERRO] Você não digitou um número correspondente!')
            elif acesso == 3:
                break
            else:
                print('[ERRO] Você não digitou um número correspondente!')

    elif nav == 2:
        # Submenu das chaves
        while True:
            acesso = int(input('Qual chave você deseja pegar? casa[0] casa da vó[1] voltar[2]: '))
            if acesso == 0:
                print(f'Você pegou as chaves de {chaves[0]}! Elas concedem {chaves[1][0]}.')
            elif acesso == 1:
                print(f'Você pegou as chaves da {chaves[2]}! Elas concedem {chaves[3][0]}.')
            elif acesso == 2:
                break
            else:
                print('[ERRO] Você não digitou um número correspondente!')

    elif nav == 3:

        fim = random.randint(1,4)
        if fim == 1:
            print('Chegando em casa. Encerrando o programa...')
            break
        elif fim == 2:
            print('Perdi a carteira. Encerrando o programa...')
            break
        elif fim == 3:
            print('Comprando novos lanches. Encerrando o programa...')
            break
        elif fim == 4:
            print('Esvaziando a mochila. Encerrando o programa...')
            break

    else:
        print('[ERRO] Você não digitou um número correspondente!')
