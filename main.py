'''Autor: Cleidson Ramos de Carvalho
Componente Curricular: MI - Algoritmos I
Concluido em: 06/06/2021
Declaro que este código foi elaborado por mim de forma individual e não
contém nenhum trecho de código de outro colega ou de outro autor, tais
como provindos de livros e apostilas, e páginas ou documentos
eletrônicos da Internet. Qualquer trecho de código de outra autoria que
não a minha está destacado com uma citação para o autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para
fins de avaliação'''

# Programa Principal
from sistema import *
from clientes import *
from manutencao import *

anterior = 1
anterior2 = 1
lista_Inicial = []
lista_Manutencoes = []
listaM_Realizadas = []

#Tratamento de erro na busca das bascar de armazenamento dos dados. Caso seja a primeira vez a inicar o programa, as pastas e arquivos são criadas automaticamente.
try:
  anterior, anterior2 = retorno_Arquivos1(lista_Inicial, anterior, anterior2)
except:
  salvar_clientes(lista_Inicial)
  codigos(anterior,anterior2)
#Tratamento de erro na busca das bascar de armazenamento dos dados. É separado do primeiro tratamento pois podem contem dados de clientes, mas não obrigatoriamente de manutenções.
try:
  lista_Manutencoes, listaM_Realizadas = retorno_Arquivos2(lista_Manutencoes, listaM_Realizadas)
except:
  salvar_manutencaoA(lista_Manutencoes)
  salvar_manutencaoR(listaM_Realizadas)
    
    
#Início das funções Principal
opcao = ''
while opcao != '4':

  # Menu Inicial
  opcao = menuInicial()
  
  # Opção de sobre os Clientes
  if opcao == '1':

    acaoCliente = ''
    while acaoCliente != '5':
      
      # Menu Cliente
      acaoCliente = menuCliente()

      #Números referentes aos código individuais, buscados nos arquivos ou iniciado em 1.
      cod = anterior
      cod = str(cod)
      
      #Opção de Cadastramente de Cliente
      if acaoCliente == '1':

        nome = input('Informe o nome do Cliente: ').title()
        endereco = input('Informe o endereço do Cliente: ')
        telefone = input('Informe o telefone do Cliente: ')

        #Criando e Salvando a classe de cliente
        cliente = Cliente(cod, nome, endereco, telefone)
        lista_Inicial.append(cliente)
        anterior += 1
        print('\nCLIENTE CADASTRADO COM SUCESSO!\n')

        #Salvamento dos clientes no arquivo
        salvar_clientes(lista_Inicial)
        #Salvamento dos codigo no arquivo
        codigos(anterior,anterior2)

      #Edição de Cliente  
      elif acaoCliente == '2':

        cod = input('Qual o código do cliente a ser editado? ')

        #Tratamento de erro por código inválido!
        while busca(cod, lista_Inicial):

          edicao = input('Qual dado deseja alterar?\n[1] - Nome\n[2] - Endereço\n[3] - Telefone\n')

          #Tratamento de erro por opcao invalida!
          if edicao == '1' or edicao == '2' or edicao == '3':
            editarCli(cod,edicao,lista_Inicial)
            salvar_clientes(lista_Inicial)
            print('\nCliente editado com sucesso!\n')
            break
          else:  
            print('\nOpção Inválida!\n')

        else:
          print('\nCliente não cadatrado!\n')

      #Exclusão de Cliente  
      elif acaoCliente == '3':

        cod = input('Qual o código do cliente a ser excluído? ')

        #Tratamento de erro por código inválido!
        if busca(cod, lista_Inicial):

          #Condicional para confirmar a inexistência de manutenções para o cliente definido.
          if not busca_especifica(cod, lista_Manutencoes):
            excluirCli(cod, lista_Inicial)
            salvar_clientes(lista_Inicial)
          else:
            print('\nCliente não pode ser excluído!\n')
        
        else:
          print('\nCliente não cadatrado!\n')

      #Listagem de Cliente  
      elif acaoCliente == '4':
        
        while True:
          pergunta = input('Deseja a [1] Lista Completa ou [2] Busca pelo Código? ')
          #Tratamento de erro por opção inválida
          if pergunta == '1' or pergunta == '2':
            #Ordenação da lista pelo nome em ordem alfabética
            ordenar_lista(lista_Inicial)
            listarCli(lista_Inicial,pergunta)
            break
          else:
            print('\nOpção Inválida!\n')  
       
      #Tratamento de erro por opção inválida no menu Clientes!
      elif acaoCliente != '5':
        print('\nFunção não encontrada!\n')   

  # Opção de sobre as Manutenções
  elif opcao == '2':

    acaoManutencao = ''
    while acaoManutencao != '7':
      
      #Números referentes aos código individuais, buscados nos arquivos ou iniciado em 1.
      codManu = anterior2
      codManu = str(codManu)
      
      # Menu Cliente
      acaoManutencao = menuManutencao()
      
      #Agendamento de Manutenção
      if acaoManutencao == '1':

        cod = input('Qual o código do cliente referente a manutenção: ')

        #Tratamento de erro por código inválido!
        if busca(cod, lista_Inicial):

          #Opção visual de confirmação sobre qual cliente será adicionado a manutenção.
          resposta = input(f'\nDeseja adicionar uma manutenção ao cliente {busca(cod,lista_Inicial).nome}? [S/N]\n ').lower()

          if resposta == 's':

            peca = input('Informe o nome da peça: ').title()

            while True:
              #Tratamento de erro no valor da peça
              try:
                valor = float(input('Informe o valor da peça: '))
                break
              except ValueError:
                print('\nPreço incorreto! ex. 120.00\n')

            while True:

              tipo = input('A validade é em [M] meses ou [D] dias? ').upper()

              #Tratamento de erro no tipo de validade
              if tipo == 'M' or tipo == 'D':

                #Tratamento de erro na validade da peça
                try:
                  prazo = int(input('Informe o prazo de Validade da Peça: '))
                  break
                except ValueError:
                  print('\nPrazo incorreto! ex. 24 meses (2 anos) ou 45 dias\n')

              else:
                print('\nTipo de validade não reconhecida, digite novamente!\n')

            #Variável definida como tupla, após a saída do loop
            validade = (tipo,prazo)

            while True:
              agenda = input('Informe o dia para realização do serviço (dd/mm/aaaa): ')
              #Tratamento de Erro para o dia do Agendamento
              try:
                conversorTempo(agenda)
                break
              except:
                print('\nData incorreta ou inexistente! ex.(07/06/2021)\n')

            #Variável criada como tupla com codigo e nome do cliente, para caso apague o cliente o resistro de manutenção terá seu nome.    
            codinome = (cod, busca(cod, lista_Inicial).nome)

            #Criando e salvando a classe da manutenção
            servico = Servico(codManu, peca, valor, validade, agenda, codinome)
            lista_Manutencoes.append(servico)

            #Atualização de contador de códigos
            anterior2 += 1

            #Salvamento das manutenções no arquivo de agendadas
            salvar_manutencaoA(lista_Manutencoes)

            #Salvamento dos codigo no arquivo
            codigos(anterior,anterior2)

            print('\nMANUTENÇÃO CADASTRADA COM SUCESSO!\n')

          else:
            print('\nOperação Cancelada!\n')

        else:
          print('\nCliente não cadatrado!\n')
      
      #Edição de Manutenção
      elif acaoManutencao == '2':
        
        buscar = input('\nQual o código da manuteção a ser editado? ')
        #Tratamento de erro por código inválido!        
        if buscaM(buscar, lista_Manutencoes):

          resposta = input(f'\nDeseja editar os dados de {buscaM(buscar, lista_Manutencoes).peca}? [S/N] ').lower()

          while resposta == 's':
            edicao = input('\nQual dado deseja alterar?\n[1] - Nome da peça\n[2] - Valor\n[3] - Validade\n[4] - Agendamento\n')

            #Tratamento de erro por opcão inválida!
            if edicao == '1' or edicao == '2' or edicao == '3' or edicao == '4':

              editarMan(buscar,edicao,lista_Manutencoes)
              salvar_manutencaoA(lista_Manutencoes)
              print('\nManutenção editada com sucesso!\n')
              break
            
            else:
              print('\nOpção InvÁlida!\n')
          else:
            print('\nOperação Cancelada!\n')
        else:
          print('\nManutenção não cadatrada!\n')
        
      
      #Exclusão de Manutenção  
      elif acaoManutencao == '3':

        buscar = input('Qual o codigo da manutenção a ser excluido? ')
        
        #Tratamento de erro por código inválido!
        if buscaM(buscar, lista_Manutencoes):

          resposta = input(f'\nDeseja excluir os dados de {buscaM(buscar, lista_Manutencoes).peca}? [S/N]\n ').lower()

          if resposta == 's':

            lista_Manutencoes.remove(buscaM(buscar, lista_Manutencoes))
            salvar_manutencaoA(lista_Manutencoes)
            print('\nManutenção deletada com sucesso!\n')
            
          else: 
            print('\nOperação Cancelada!\n')

        else:
          print('\nManutenção não  encontrada!\n')
        
      
      #Realização de Manutenção  
      elif acaoManutencao == '4':

        buscar = input('Qual o código da manutenção que foi realizada? ')
        #Tratamento de erro por código inválido!
        if buscaM(buscar, lista_Manutencoes):
          realizarMan(buscar, lista_Manutencoes, listaM_Realizadas, codManu)
          #Salvamento das manutenções agendadas no arquivo
          salvar_manutencaoA(lista_Manutencoes)
          #Salvamento das manutenções realizadas no arquivo
          salvar_manutencaoR(listaM_Realizadas)
          anterior2 += 1
          #Salvamento dos codigo no arquivo
          codigos(anterior,anterior2)
        else:
          print('\nManutenção não encontrada!\n')
      
      #Listar Manutencões agendadas ou Realizadas
      elif acaoManutencao == '5':

          pergunta = input('Deseja a Lista de Manutenções Agendadas [1] ou Realizadas [2] ')

          #Tratamento de erro por opção inválida!
          if pergunta == '1' or pergunta == '2':
            listarMan(lista_Manutencoes, listaM_Realizadas, pergunta)

          else: 
            print('\nOpção Invalida!\n') 
      
      #Impressão de Manutenções
      elif acaoManutencao == '6':

        ordenar_por_data(lista_Manutencoes)
        imprimir_manutencoes(lista_Manutencoes)
        print('Relatorio Gerado e Armazenado na pasta "Relatorios/Saida".')
      
      #Tratamento de erro por opção inválida no menu Manutenções!
      elif acaoManutencao != '7':
        print('\nFunção não encontrada!\n')

  elif opcao == '3':
    while True:
      
      data = input('Informe o mês e ano para o relatorio (ex. 10/2021): ')
      
      #Variável para a primeira funcionalidade da Função conversorBalanco(data, teste) com apenas mês e ano.
      teste = 'n'
      
      try:
        #Caso seja inserido uma data inválida
        conversorBalancoMes(data, teste)
        ordenar_por_data(listaM_Realizadas)
        valor_BalancoMes(data, listaM_Realizadas)
        break
      except:
        print('\nData incorreta ou inexistente! ex.(06/2021)\n')

  #Tratamento de erro por opção inválida no menu Principal!
  elif opcao != '4':
    print('\nFunção não encontrada!\n')     