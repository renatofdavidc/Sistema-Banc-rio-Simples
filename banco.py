#Sistema bancário simples, com função de depositar, sacar e ver extrato
'''Deve ser possível depositar valores positivos para minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário. Todos os depósitos devem ser armazenados
em uma variável e exibidos na operação de extrato.
    O sistema deve permitir relizar 3 saques diários, com limite máximo de R$500,00 por saque.
Caso o usuário não tenha saldo em conta, o sistema deve avisar. Todos os saques devem ser 
armazenados em uma variável e exibidos na operação de extrato.
    O extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve
ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir mensagem avisando.
    Valores no formato R$xxxx,xx
'''
saldo_da_conta = 0
numero_saques = 0
extrato = ''
limite_saques_diarios = 3
limite_valor_saque = 500
mensagem_menu = '''[1] - Ver saldo
[2] - Realizar depósito
[3] - Realizar saque
[4] - Ver extrato
[5] - Sair
'''

while True:
    print(mensagem_menu)
    opcao = (input('Digite uma opção: '))
    
    match opcao:
        case '1':
            print('===== SALDO DA CONTA =====')
            print('O saldo disponível é: ')
            print(f'R${saldo_da_conta:.2f}')
        case '2':
            print('===== DEPÓSITOS =====')
            valor_deposito = float(input('Digite um valor a ser depositado na conta: '))
            if valor_deposito<=0:
                print('Valor inválido!')
            else: 
                saldo_da_conta += valor_deposito
                print(f'O novo saldo é R${saldo_da_conta:.2f}')
                extrato += f'Depósito: R${valor_deposito:.2f}'
        case '3':
            print('===== SAQUE =====')
            if saldo_da_conta <= 0:
                print('Não há dinheiro para ser sacado!')
            else:
                valor_saque = int(input('Digite o valor a ser sacado (Limite de R$500,00): '))
                if valor_saque > saldo_da_conta:
                    print('Não há dinheiro suficiente na conta para realizar o saque!')
                else:
                    if valor_saque > 500 or valor_saque<=0:
                        print('O valor escolhido é maior do que o limite ou negativo, o saque não pode ser realizado.')
                    else:
                        if numero_saques < limite_saques_diarios:
                            saldo_da_conta -= valor_saque
                            extrato += f'Saque: R${valor_saque:.2f}'
                            print(f'O novo saldo é R${saldo_da_conta:.2f}')
                            numero_saques += 1
                        else:
                            print('ERRO! Limite de saques diários atingido.')
        case '4':
            print('===== EXTRATO =====')
            print('Não foram realizadas movimentações!' if not extrato else extrato)
            print(f'Saldo da conta: R${saldo_da_conta:.2f}')
        case '5':
            break