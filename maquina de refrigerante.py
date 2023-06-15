#o código começa com essa parte que determina a quantidade de cada cédula presente na maquina 
moeda_25_centavos = 0
moeda_50_centavos = 0
moeda_1_real = 0
cedula_2_reais = 0
cedula_5_reais = 0
cedula_10_reais = 0
cedula_20_reais = 0

#é determinado valor de cada moeda para ficar mais fácil a soma total no valor da maquina
moeda25 = 0.25
moeda50 = 0.50
moeda1 = 1
cedula2 = 2
cedula5 = 5
cedula10 = 10
cedula20 = 20

#aqui é a parte onde é calculado o valor geral de cada tipo de cédula e  de moeda 
moeda25 *= moeda_25_centavos
moeda50 *= moeda_50_centavos
moeda1 *= moeda_1_real
cedula2 *= cedula_2_reais
cedula5 *= cedula_5_reais
cedula10 *= cedula_10_reais
cedula20 *= cedula_20_reais

#aqui é predeterminado a quantidade de cada produtoporém só possuimos a coca cola)
quantidade_coca = 10

#aqui ocorre a definição de uma função para que no perfil de administrador seja possível a quantidade de coca seja permanecida sempre que o código reiniciar
#e é posssível fazer isso dando a peculiariedade global a variavel quantidade_coca
def armazenamento_coca(escolha):
    global quantidade_coca
    quantidade_coca=escolha

#é calculado o valor total da maquina com a soma de todas as variáveis que levavam o valor total de cada tipo de cédula e moeda
moedas_totais_da_maquina = moeda25 + moeda50 + moeda1 + cedula2 + cedula5 + cedula10 + cedula20

#os numeros quando o pagamento é realizado em pix são armazenados nessa variavel 
numeros_armazenamento = []


#aqui é definido uma função que tem o objetivo de armazenar as moedas e cédulas da maquina 
def armazenar_moedas (valor_inserido):
    #aqui é definido que as variáveis de quantidade da maquina tem que ser global para que ela rode pelo código todo sem problemas
    global moeda_25_centavos, moeda_50_centavos, moeda_1_real, cedula_2_reais, cedula_5_reais, cedula_10_reais, cedula_20_reais
    
    #primeiro é realizado uma verificação para saber se a moeda ou cédula inserida é catalogada e valida no sistema
    if valor_inserido in [0.25,0.50,1,2,5,10,20]:
        #segundo ocorre novamente uma verificação para saber qual que foi a nota ou cédula inserida, 
        # e logo depois dessa verificação ocorre a soma na variavel de quantidade equivalente ao valor inserido 
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
    
#logo depois temos outra definição de função, porém dessa vez a função tem o objetivo de armazenar o numero de celular quando a opção de pagamento for pix   
def armazenar_numero(numero_celular, valor):
    numeros_armazenamento.append([numero_celular, valor])

#aqui temos a "palavra chave" para que ocorra a reinicialização do código após o uso de qualquer um dos usuarios
reiniciar = 's'
#logo depois é usado o while para que toda vez que for digitado "s" na opção reiniciar (que esta no final do código) o código inicie da seleção de perfil 
while reiniciar == 's':
    #abaixo ocorre a seleção de qual sera o perfil desejado para a maquina rodar
    print('1 - Usuário')
    print('2 - Administrador')

    usg = int(input('Qual usuário você deseja? '))
    #apenas um sistema basico para que se repita até que seja digitado um perfil valido
    while usg > 2 or usg < 1:
        print('Usuário inválido')
        print('1 - Usuário')
        print('2 - Administrador')
        usg = int(input('Qual usuário você deseja? '))


    if usg == 2:
        #se o perfil escolhido for o do administrado ele tera acesso a todas as opções que esta abaixo
        print('Opções do Administrador:')
        print('a - Verificar quantidade de cédulas e moedas')
        print('b - Mudar quantidade de cédulas')
        print('c - Mudar quantidade de moedas')
        print('d - Verificar estoque de produtos')
        print('e - Mudar quantidade de produtos no estoque')
        print('f - Verificar os telefones registrados no PIX e o valor pago')

        escolha_admin = input('Escolha uma opção: ')

        if escolha_admin == 'a':
            #aqui apenas nos mostra a quantidade de cada cedula e moeda que esta presente na maquina
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
            #aqui ocorre a seleção de qual sera a cédula escolida para ter seu valor mudado 
            print('Escolha a cédula que deseja modificar:')
            print('1 - Cédulas de 2 reais')
            print('2 - Cédulas de 5 reais')
            print('3 - Cédulas de 10 reais')
            print('4 - Cédulas de 20 reais')

            escolha_cedula = int(input('Digite o número da cédula: '))

            #logo após a escolha o código verifica qual foi a cédula escolida e da um input para que seja digitado a nova quantidade de cédula,
            #e se a cédula não estiver presente nas opções de escolha o código devolve que o valor inserido é invalido
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
            #aqui ocorre o mesmo caso para que ocorra a seleção de qual sera a moeda escolida para ter seu valor mudado 
            print('Escolha a moeda que deseja modificar:')
            print('1 - Moedas de 25 centavos')
            print('2 - Moedas de 50 centavos')
            print('3 - Moedas de 1 real')

            escolha_moeda = int(input('Digite o número da moeda: '))
            #logo após a escolha o código verifica qual foi a cédula escolida e da um input para que seja digitado a nova quantidade de cédula,
            #e se a cédula não estiver presente nas opções de escolha o código devolve que o valor inserido é invalido
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
        
        #apenas é mostrado a quantidade de cocas na maquina
        elif escolha_admin == 'd':
            print('A máquina possui', quantidade_coca, 'latinhas de coca')
        #aqui ocorre a modificação na quantidade de cocas presentes na maquina
        elif escolha_admin == 'e':
            nova_quantidade_coca = int(input('digite a quantidade que deseja modificar: '))
            #ocorre a chamada da função para que seja mudada permanentemente durante o uso da maquina a quantidade de cocas presente no armazenamento
            armazenamento_coca(nova_quantidade_coca)
            print('A quantidade de latinhas é de', quantidade_coca)
        #aqui é onde é mostrado para o administrador o numero de telefone e o valor pago quando a opção de pagamento for pix no perfi do usuário 
        elif escolha_admin == 'f':
            print('Número e valor pago, respectivamente: ', numeros_armazenamento)
        #se for escolido uma opção q não exite é mostrado q a opção é invalida
        else:
            print('Opção inválida.')

    if usg == 1:
        #a primeira ação da maquina quando o perfil escolido é de usuario é analisar se a maquina possui quantidade o suficiente de produtos para que seja possivel realizar a 
        if quantidade_coca <= 0:
            print('Desculpe, nossa máquina está sem estoque')
        #e se ouver a quantidade o suficiente ele continua o código normalmente
        else:
           coca_cola = 1
        #aqui é mostrado quais que são os produtos que a maquina tem (por enquanto somente coca cola )
        print('1 - Coca Cola = 5$')
        #aqui ocorre o input para saber qual que vai ser o produto escolido para que seja realizado a compra, 
        pedido = int(input('Digite 1 para selecionar a bebida, o valor unitário é de 5 reais. '))
        #como não tem outro produto além da coca é definido como se a sua escolha for diferente de 1(coca cola) a maquina não é capaz de realizar a compra
        if pedido != 1:
            print('Número inválido!')

        #logo após selecionar o produto lhes é perguntado qual a quantidade do produto é desejada
        else:
         qtde = int(input('Qual a quantidade de latinhas que deseja comprar?'))
         #e se a maquina possui menos produto do que o que é desejado ele n é possível de realizar a compra
        if qtde > quantidade_coca:
            print('Quantidade de unidades solicitadas maior que o estoque é capaz de fornecer')
        #após forncer a quantidade desejada e a maquina possuir produtos o suficiente é perguntado qual sera a forma de pagamento 
        else:
         if pedido == 1:
            print('1 - Dinheiro')
            print('2 - Pix')
            modo_pagamento = int(input('Qual a forma de pagamento? '))
            #se o modo de pagamento for pix ele puxa o usuario para essa parte do código onde é feita somente para o modo de pagamento pix
            if modo_pagamento == 2:
                #é multiplicado o valor da coca pela quantidade para que seja adiquirido o valor total a ser pago
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                #depois de mostrado o valor total a ser pago lhes é fornecido 2 input para q seja recolhido pela maquina o numero de telefone e o valor a ser pago 
                numero_celular = input('Insira seu número de telefone (DDD) xxxxx-xxxx: ')
                valor_pg = float(input('Insira o valor da compra: '))
                #logo após acontece o reconhecimento para saber se o numero de telefone é valido ou não
                
                if numero_celular != 0:
                    #e se for válido ocorre a chamada da função armazenar_numero
                    # onde é armazenado em uma matriz de 2 colunas e infinitas linhas o numero de telefone e o valor pago por esse numero de telefone
                    armazenar_numero(numero_celular, valor_pg)
                else:
                    #se for invalido somente é printado eu o numero é invalido
                    print('Número de telefone inválido.')
                #se o for inserido o valor certo de compra o código realiza a compra com sucesso
                if valor == valor_pg:
                    #logo após ocorre a subtração do valor de cocas presente na maquina com o valor de cocas retirado
                    quantidade_coca = quantidade_coca - qtde
                    print('Pagamento efetuado com sucesso!')

                #entretanto se o valor inserido for diferente ele determina como incorreto e encerra o código
                else:
                    print('Valor incorreto')
                    # porém mesmo assim armazena na matriz o numero e o valor inserido


            #se o modo de pagamento escolhido for em dinheiro ocorrera todo esse processo abaixo
            elif modo_pagamento == 1:
                #é multiplicado o valor da coca pela quantidade para que seja adiquirido o valor total a ser pago
                valor = 5 * qtde
                print('O valor a ser pago é de', valor, 'reais')
                #logo após é mostrado o valor total a ser pago, e pede para que seja inserido o valor de cada nota 
                pagamento = float(input('Insira o dinheiro necessário: '))
                #logo após ocorre a chamda da função para que seja armazenada na variavel de quantidade de cada cédula e moeda da maquina o valor inserido na hora do pagamento
                armazenar_moedas(pagamento)
               
               #aqui ocorre a verificação caso o numero inserido seja invalido ou não esta nas opções de cédulas e moedas aceitas pela máquina
                while pagamento not in [0.25,0.50,1,2,5,10,20]:
                    print('pagamento invalido')
                    pagamento = float(input('insira o dinheiro necessário: '))
                    #e novamente ocorre o chamado da função para que armazene na maquina a quantidade inserida na hora do pagamento
                    armazenar_moedas(pagamento)
                #logo abaixo é um sistema para que armazene o valor inserido caso a moeda ou cédula tenha um valor inferior ao do produto
                dinheiro_faltante=((pagamento-valor)*-1)
                #a variavel dinheiro_faltante pega como valor a quantidade inserida no pagamento e diminui com o valor para que pegue o resto a ser pago
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