#Determina a quantidade de moedas e de cédulas na maquina
moeda_25_centavos = 0
moeda_50_centavos = 0
moeda_1_real = 0
cedula_2_reais = 0
cedula_5_reais = 2
cedula_10_reais = 0
cedula_20_reais = 0

#Determina o valor de cada moeda e cédula para relalizar as operações
moeda25 = 0.25
moeda50 = 0.50
moeda1 = 1
cedula2 = 2
cedula5 = 5
cedula10 = 10
cedula20 = 20

#Realiza o calculo do valor total em dinheiro da qunatidade de cada cedula e moeda
moeda25 *= moeda_25_centavos
moeda50 *= moeda_50_centavos
moeda1 *= moeda_1_real
cedula2 *= cedula_2_reais
cedula5 *= cedula_5_reais
cedula10 *= cedula_10_reais
cedula20 *= cedula_20_reais

#Determina a quantidade do produto na maquina
quantidade_coca = 1

#Define uma função global para que a quantidade de CocaCola seja mantida após o codigo reniciar
#Para isso é dada a particularidade global à variavel quantidade_coca
def armazenamento_coca(escolha):
    global quantidade_coca
    quantidade_coca=escolha

#Define o calculo para o valor total presente na maquina usando as variaveis definidas anteriormente para para definir o valor total da quantidade de cada cedula
moedas_totais_da_maquina = moeda25 + moeda50 + moeda1 + cedula2 + cedula5 + cedula10 + cedula20

#Define onde serão armazenados os numeros de PIX
numeros_armazenamento = []


#Função que define o armazenamento dos valores inseridos na maquina
def armazenar_moedas (valor_inserido):
    #Define as variaveis como globais para que possam ser usadas em todo o código
    global moeda_25_centavos, moeda_50_centavos, moeda_1_real, cedula_2_reais, cedula_5_reais, cedula_10_reais, cedula_20_reais
    
    #Define se o valor inserido é reconhecido no sistema e valida o valor logo em seguida,
    if valor_inserido in [0.25,0.50,1,2,5,10,20]:
        #Verifica qual cedula ou moeda foi inserida e realiza a soma
        if valor_inserido==0.25:
            moeda_25_centavos+=1
        elif valor_inserido==0.50:
            moeda_50_centavos+=1
        elif valor_inserido==1:
            moeda_1_real+=1
        elif valor_inserido==2:
            cedula_2_reais+=1
        elif valor_inserido==5:
            cedula_5_reais+=1
        elif valor_inserido==10:
            cedula_10_reais+=1
        elif valor_inserido ==20:
            cedula_20_reais+=1
    
#Define a função para armazenar os valores de PIX  
def armazenar_numero(numero_celular, valor):
    #Adiciona na lista os numeros usados no PIX e o valor da compra
    numeros_armazenamento.append([numero_celular, valor])

#É definido a variavel usada como condição para que o código renicie usando o loop de while
reiniciar = 's'
#É iniciado o loop while para sempre manter o código rodando mantendo as informações salvas
while reiniciar == 's':
    print('1 - Usuário')
    print('2 - Administrador')

    usg = int(input('Qual usuário você deseja? '))
    #Loop while para impedir que outra opção seja escolhida ao invés dos perfis de usuarios.
    while usg > 2 or usg < 1:
        print('Usuário inválido')
        print('1 - Usuário')
        print('2 - Administrador')
        usg = int(input('Qual usuário você deseja? '))


    if usg == 2:
        #Opções de administrador
        print('Opções do Administrador:')
        print('a - Verificar quantidade de cédulas e moedas')
        print('b - Mudar quantidade de cédulas')
        print('c - Mudar quantidade de moedas')
        print('d - Verificar estoque de produtos')
        print('e - Mudar quantidade de produtos no estoque')
        print('f - Verificar os telefones registrados no PIX e o valor pago')

        escolha_admin = input('Escolha uma opção: ')
        #Quantidade de cedulas e moedas presentes atualmente na maquina
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

            #Area onde pode modificar a quantidade de cedulas escolhida
            #Se ocorrer alguma opção que não encaixe o codigo vai reinicializar
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
                #Se for escolhida alguma opção não ultizavel, replica opção invalida e pergunta se quer reiniciar
                print('Opção inválida.')

        elif escolha_admin == 'c':
            
            print('Escolha a moeda que deseja modificar:')
            print('1 - Moedas de 25 centavos')
            print('2 - Moedas de 50 centavos')
            print('3 - Moedas de 1 real')
            
            escolha_moeda = int(input('Digite o número da moeda: '))
            #Area onde pode modificar a quantidade de moedas escolhida
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
                #Se for escolhida alguma opção não ultizavel, replica opção invalida e pergunta se quer reiniciar
                print('Opção inválida.')
        
        #Mostra a quantidade de latas na maquina
        elif escolha_admin == 'd':
            print('A máquina possui', quantidade_coca, 'latinhas de Coca Cola')
        #Modifica a quantidade de latas presentes na maquina
        elif escolha_admin == 'e':
            nova_quantidade_coca = int(input('Digite a quantidade que deseja modificar: '))

            #Operação para a modificação de latas na maquina
            quantidade_coca = (nova_quantidade_coca + quantidade_coca)
            
            print('A quantidade de latinhas é de', quantidade_coca)
        #Mostra a lista presente na função armazenar_numero que contem os numeros usados no PIX e os valores comprados respectivamente
        elif escolha_admin == 'f':
            print('Número e valor pago, respectivamente: ', numeros_armazenamento)
        #Se for escolhida alguma opção não ultizavel, replica opção invalida e pergunta se quer reiniciar
        else:
            print('Opção inválida.')

    if usg == 1:
        #Ao escolher o perfil de usurio a maquina analisa se tem produtos no estoque.
        if quantidade_coca <= 0:
            #Caso não tenha ela replica:
            print('Desculpe, nossa máquina está sem estoque')
        #Caso tenha produtos no estoque, a maquina continua normalmente
        else:
           coca_cola = 1
        #Aqui é pedido para selecionar o produto
        print('1 - Coca Cola = 5$')
        pedido = int(input('Digite 1 para selecionar a bebida, o valor unitário é de 5 reais. '))
        #Se for escolhida alguma opção não ultizavel, replica opção invalida e pergunta se quer reiniciar       
        if pedido != 1:
            print('Opção inválida!')

        #Verifica-se a quantidade do produto desejada:
        else:
         qtde = int(input('Qual a quantidade de latinhas que deseja comprar?'))
         #Caso a quantidade desejada ultrapasse a quantidade de produtos presentes na maquina ele replica:
        if qtde > quantidade_coca:
            print('Quantidade de unidades solicitadas maior que o estoque é capaz de fornecer')
        
        else:
         if pedido == 1:
            #É perguntado o metodo de pagamento requerido
            print('1 - Dinheiro')
            print('2 - Pix')
            modo_pagamento = int(input('Qual a forma de pagamento? '))
            #Método de pagamento PIX
            if modo_pagamento == 2:
                #É efetuado a multiplicação para mostrar o valor total a ser pago
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                #É colocado um input para colocar o numero de telefone do PIX e o valor
                numero_celular = input('Insira seu número de telefone (DDD) xxxxx-xxxx: ')
                valor_pg = float(input('Insira o valor da compra'))
                
                #Realiza uma verificação se o numero de telefone é válido ou não
                if numero_celular != 0:
                    #Caso for válido ocorre a chamada da função armazenar_numero
                    #Onde é armazenado na matriz de duas colunas na função
                    armazenar_numero(numero_celular, valor_pg)
                else:
                #Se for escolhida alguma opção não ultizavel, replica opção invalida e pergunta se quer reiniciar
                    print('Número de telefone inválido.')
                #Caso o for inserido o valor certo de compra o código realiza a compra com sucesso
                if valor == valor_pg:
                    #Logo após ocorre a subtração da qauntidade de latas presentes na maquina com a quantidade de latas retiradas
                    quantidade_coca = quantidade_coca - qtde
                    print('Pagamento efetuado com sucesso!')

                #Entretanto se o valor inserido for diferente ele determina como incorreto e pergunta se quer reiniciar
                else:
                    print('Valor incorreto')
                    #Porém ainda armazena a chave o valor inserido


            #Método de pagamento dinheiro
            elif modo_pagamento == 1:
                #É efetuado a multiplicação para mostrar o valor total a ser pago
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                #Logo após ser mostrado o valor total a ser pago, a maquina pede para que seja inserido o valor de cada nota 
                pagamento = float(input('Insira o dinheiro necessário: '))
            
                #logo após ocorre a chamada da função para armazenar na variavel a quantidade de cédulas e moedas usadas na hora do pagamento
                armazenar_moedas(pagamento)
               
               #Aqui ocorre a verificação caso o numero inserido seja invalido ou não esta nas opções de cédulas e moedas aceitas pela máquina
                while pagamento not in [0.25,0.50,1,2,5,10,20]:
                    print('pagamento invalido')
                    pagamento = float(input('insira o dinheiro necessário: '))
                    #e novamente ocorre o chamado da função para que armazene na maquina a quantidade inserida na hora do pagamento
                    armazenar_moedas(pagamento)
                #Logo abaixo é um sistema para que armazene o valor inserido caso a moeda ou cédula tenha um valor inferior ao do produto
                dinheiro_faltante=((pagamento-valor)*-1)
                #A variavel dinheiro_faltante pega como valor a quantidade inserida no pagamento e diminui com o valor para que pegue o resto a ser pago
                #e é multiplicado por -1 para que não dê nenhum valor negativo
                pg1=0
                #a variavel pg1 tem a funcionalidade ir somando a si o valor inserido no pagamento 
                pg1 +=pagamento
                #logo após a soma do pg1 com a valor inserido no pagamento, a variavel pagamento vai armazenando até que o valor do produto seja menor
                pagamento=pg1

                #enquanto os valores inserido na variavel pagamento for menor que o valor da maquina é realizado este while
                while dinheiro_faltante > 0 :
                     print('valor faltante é de ', dinheiro_faltante)
                     pagamento = float(input('insira o dinheiro faltante: '))
                     #novamente ocorre a chamada da função para que armazene no interior da maquina a quantidade de cada moeda ou cedula
                     armazenar_moedas(pagamento)
                     #ocorre novamente uma verificação para saber se a nota ou moeda inserida é valida ou não 
                     while pagamento not in [0.25,0.50,1,2,5,10,20]:
                            print('pagamento invalido')
                            pagamento = float(input('insira o dinheiro necessário: '))
                     #aqui ocorre novamente o armazenamento da variavel pagamento até que o valor inserido seja maior que o valor do produto
                     pagamento = (pagamento + pg1)
                     #novamente ocorre a verificação para saber se o dinheiro faltante é maior ou não que zero e assim reinicar ou não o pagamento até que seja finalizado completamente
                     dinheiro_faltante = ((pagamento - valor) * -1)
                     pg1 = pagamento
                #aqui ocorre uma verificação para saber se a maquina vai ter troco ou não caso o valor inserido na hora do pagamento seja maior que o valor do produto
                if pagamento > moedas_totais_da_maquina:
                    print('Não é possível fazer a compra.')
                #porém se o valor inserido na hora de pagamento for menor que o valor do produto é dado como pagamento insuficiente
                elif pagamento < valor:
                    print('Pagamento insuficiente.')
                
                #porém caso o contrario aconteça a maquina inicia o seu sistema de troco     
                else:
                    #é criado a variavel troco onde pega o valor inserido no pagamento e diminui pelo valor do produto para saiba a quantidade de moedas ou cédulas a ser devolvidas
                    troco = pagamento - valor
                    #a maquina toma como parametro se ela tem troco ou não a quantidade total que tem na maquina
                    troco_disponivel = moedas_totais_da_maquina

                    #é criado duas listas para que seja organizado dentro delas a quantidade de troco que deve ser passado para o cliente
                    #além de facilitar na hora de mostrar para o usuairo as notas e moedas que ele recebeu de troco, o código fica BEM menor
                    cedulas_troco = []
                    moedas_troco = []

                    #se for necessario a realização de um troco a maquina começa a verificar qual é a moeda ou cédula que precisa ser dado
                    while troco > 0:
                        #se o troco for maior que o valor da cedula, e isso ocorre do maior para o menor para que facilite para a maquina saber qual nota o moeda dar de troco
                        #e depois de verificar se o troco for maior que o valor da cédula, ocorre a verificação para saber se a maquina possui notas ou moedas o suficiente em seu armazenamento para que seja possivel realizar o troco 
                        #logo após se a maquina tiver em seu armazento a quantidade o suficiente para dar o troco, ele adiciona às listas cedulas_troco ou moedas_troco para que haja uma separação na hora de apresentar o troco para o usuario
                        #depois de tudo isso é retirado da maquina a quantidade de moeda ou cédula 
                        #e o valor do troco ira diminui cada vez que passar por cada uma das cedulas ou moedas até que chegue a zero 
                        #depois de tudo isso o código da continuidade 
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
                    #quando a variavel troco chegar a zero ou for zero, a maquina chega a seus ajustes finais                 
                    if troco == 0:
                        #a compra é realizada com sucesso e é tirado da maquina a quantidade de coca na qual o usuario comprou 
                        quantidade_coca = quantidade_coca - qtde
                        print('Pagamento efetuado com sucesso!')
                        #e é printado separadamente a quantidade de moedas ou cédulas que deve ser retirado como troco pelo usuario
                        for cedula in cedulas_troco:
                            print('Seu troco é de', cedula, 'reais')
                        for moeda in moedas_troco:
                            print('Seu troco é de', moeda, 'real')
                    else:
                        #caso a maquina não tenha as cédulas ou moedas certas para que seja realizada a compra ela nega pois é impossível por exemplo dar uma nota de 3 como troco
                        print('Não é possível dar o troco com as cédulas/moedas disponíveis.')
            else:
                #caso o modo de pagamento inserido não seja nem pix nem dinheiro o código printa como invalido 
                print('Modo de pagamento inválido')

    #e aqui é quando qualquer parte do nosso código chega ao final, e é feito uma escolha para caso queira reiniciar o código volta para a seleção de usuario
    #caso contrario o programa simplesmente se encerra
    reiniciar = input('Deseja reiniciar? (s/n): ')