moeda_25_centavos = 0
moeda_50_centavos = 2
moeda_1_real = 6
cedula_2_reais = 30
cedula_5_reais = 20
cedula_10_reais = 10
cedula_20_reais = 2

moeda25 = 0.25
moeda50 = 0.50
moeda1 = 1
cedula2 = 2
cedula5 = 5
cedula10 = 10
cedula20 = 20

moeda25 *= moeda_25_centavos
moeda50 *= moeda_50_centavos
moeda1 *= moeda_1_real
cedula2 *= cedula_2_reais
cedula5 *= cedula_5_reais
cedula10 *= cedula_10_reais
cedula20 *= cedula_20_reais

quantidade_coca = 5

moedas_totais_da_maquina = moeda25 + moeda50 + moeda1 + cedula2 + cedula5 + cedula10 + cedula20

numeros_armazenamento = []


def armazenar_numero(numero_celular, valor):
    numeros_armazenamento.append([numero_celular, valor])


reiniciar = 's'

while reiniciar == 's':
    print('1 - Usuário')
    print('2 - Administrador')

    usg = int(input('Qual usuário você deseja? '))

    while usg > 2 or usg < 1:
        print('Usuário inválido')
        print('1 - Usuário')
        print('2 - Administrador')
        usg = int(input('Qual usuário você deseja? '))

    if usg == 2:
        print('Opções do Administrador:')
        print('a - Verificar quantidade de cédulas e moedas')
        print('b - Mudar quantidade de cédulas')
        print('c - Mudar quantidade de moedas')
        print('d - Verificar estoque de produtos')
        print('e - Mudar quantidade de produtos no estoque')
        print('f - Verificar os telefones registrados no PIX e o valor pago')

        escolha_admin = input('Escolha uma opção: ')

        if escolha_admin == 'a':
            print('Quantidade de cédulas:')
            print('Cédulas de 2 reais:', cedula_2_reais)
            print('Cédulas de 5 reais:', cedula_5_reais)
            print('Cédulas de 10 reais:', cedula_10_reais)
            print('Cédulas de 20 reais:', cedula_20_reais)
            print('Quantidade de moedas:')
            print('Moedas de 25 centavos:', moeda_25_centavos)
            print('Moedas de 50 centavos:', moeda_50_centavos)
            print('Moedas de 1 real:', moeda_1_real)
        elif escolha_admin == 'b':
            print('Escolha a cédula que deseja modificar:')
            print('1 - Cédulas de 2 reais')
            print('2 - Cédulas de 5 reais')
            print('3 - Cédulas de 10 reais')
            print('4 - Cédulas de 20 reais')

            escolha_cedula = int(input('Digite o número da cédula: '))

            if escolha_cedula == 1:
                nova_qtd = int(input('Digite a nova quantidade de cédulas de 2 reais: '))
                cedula_2_reais = nova_qtd
                print('Quantidade de cédulas de 2 reais atualizada.')
            elif escolha_cedula == 2:
                nova_qtd = int(input('Digite a nova quantidade de cédulas de 5 reais: '))
                cedula_5_reais = nova_qtd
                print('Quantidade de cédulas de 5 reais atualizada.')
            elif escolha_cedula == 3:
                nova_qtd = int(input('Digite a nova quantidade de cédulas de 10 reais: '))
                cedula_10_reais = nova_qtd
                print('Quantidade de cédulas de 10 reais atualizada.')
            elif escolha_cedula == 4:
                nova_qtd = int(input('Digite a nova quantidade de cédulas de 20 reais: '))
                cedula_20_reais = nova_qtd
                print('Quantidade de cédulas de 20 reais atualizada.')
            else:
                print('Opção inválida.')

        elif escolha_admin == 'c':
            print('Escolha a moeda que deseja modificar:')
            print('1 - Moedas de 25 centavos')
            print('2 - Moedas de 50 centavos')
            print('3 - Moedas de 1 real')

            escolha_moeda = int(input('Digite o número da moeda: '))

            if escolha_moeda == 1:
                nova_qtd = int(input('Digite a nova quantidade de moedas de 25 centavos: '))
                moeda_25_centavos = nova_qtd
                print('Quantidade de moedas de 25 centavos atualizada.')
            elif escolha_moeda == 2:
                nova_qtd = int(input('Digite a nova quantidade de moedas de 50 centavos: '))
                moeda_50_centavos = nova_qtd
                print('Quantidade de moedas de 50 centavos atualizada.')
            elif escolha_moeda == 3:
                nova_qtd = int(input('Digite a nova quantidade de moedas de 1 real: '))
                moeda_1_real = nova_qtd
                print('Quantidade de moedas de 1 real atualizada.')
            else:
                print('Opção inválida.')
        elif escolha_admin == 'd':
            print('a maquina possui', quantidade_coca, 'latinhas de coca')

        elif escolha_admin == 'e':
            quantidade_coca = int(input('digite a quantidade que deseja modificar: '))
            print('agora a quantidade de coca é de', quantidade_coca)
        if escolha_admin == 'f':
            print('os numeros e pagamentos no pix são: ', numeros_armazenamento)
        else:
            print('Opção inválida.')

    if usg == 1:
        coca_cola = 1

        print('1 - Coca Cola = 5$')

        pedido = int(input('Digite 1 para selecionar a bebida, o valor unitário da bebida é de 5 reais. '))
        qtde = int(input('Qual a quantidade de latinhas que deseja comprar?'))

        if pedido == 1:
            print('1 - Dinheiro')
            print('2 - Pix')
            modo_pagamento = int(input('Qual a forma de pagamento? '))
            if modo_pagamento == 2:
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                numero_celular = input('Insira seu número de telefone (DDD) xxxxx-xxxx: ')
                valor_pg = float(input('Insira o valor da compra: '))
                if numero_celular != 0:
                    armazenar_numero(numero_celular, valor_pg)
                else:
                    print('Número de telefone inválido.')
                if valor == valor_pg:
                    print('Pagamento efetuado com sucesso!')
                else:
                    print('Valor insuficiente')

            elif modo_pagamento == 1:
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                pagamento = float(input('Insira o dinheiro necessário: '))

                if pagamento > moedas_totais_da_maquina:
                    print('Não é possível fazer a compra.')
                elif pagamento < valor:
                    print('Pagamento insuficiente.')
                else:
                    troco = pagamento - valor
                    troco_disponivel = moedas_totais_da_maquina

                    cedulas_troco = []
                    moedas_troco = []

                    while troco > 0:
                        if troco >= 20 and cedula_20_reais > 0:
                            cedulas_troco.append(20)
                            cedula_20_reais -= 1
                            troco -= 20
                        elif troco >= 10 and cedula_10_reais > 0:
                            cedulas_troco.append(10)
                            cedula_10_reais -= 1
                            troco -= 10
                        elif troco >= 5 and cedula_5_reais > 0:
                            cedulas_troco.append(5)
                            cedula_5_reais -= 1
                            troco -= 5
                        elif troco >= 2 and cedula_2_reais > 0:
                            cedulas_troco.append(2)
                            cedula_2_reais -= 1
                            troco -= 2
                        elif troco >= 1 and moeda_1_real > 0:
                            moedas_troco.append(1)
                            moeda_1_real -= 1
                            troco -= 1
                        elif troco >= 0.50 and moeda_50_centavos > 0:
                            moedas_troco.append(0.50)
                            moeda_50_centavos -= 1
                            troco -= 0.50
                        elif troco >= 0.25 and moeda_25_centavos > 0:
                            moedas_troco.append(0.25)
                            moeda_25_centavos -= 1
                            troco -= 0.25
                        else:
                            break

                    if troco == 0:
                        print('Pagamento efetuado com sucesso!')
                        for cedula in cedulas_troco:
                            print('Seu troco é de', cedula, 'reais')
                        for moeda in moedas_troco:
                            print('Seu troco é de', moeda, 'real')
                    else:
                        print('Não é possível dar o troco com as cédulas/moedas disponíveis.')

    reiniciar = input('Deseja reiniciar? (s/n): ')
