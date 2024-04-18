# Funções do sistema do Gerenciador
import os
from pickle import dump, load
from datetime import datetime

def menuInicial():
  print('\n\n   GERENCIADOR DE MANUTENÇÕES\n\n')
  print('[1] - Menu Clientes')
  print('[2] - Menu Manutenções ')
  print('[3] - Balanço do Mês ')
  print('[4] - Sair ')
  resposta = input()
  os.system('cls' if os.name == 'nt' else 'clear')
  return resposta

def menuCliente():
  print('\n\n   MENU CLIENTES\n\n')
  print('[1] - Cadastrar Novo Cliente')
  print('[2] - Editar Dados do Cliente ')
  print('[3] - Excluir Cliente ')
  print('[4] - Listar Cliente ')
  print('[5] - Voltar o Menu anterior')
  resposta = input()
  os.system('cls' if os.name == 'nt' else 'clear')
  return resposta

def menuManutencao():
  print('\n\n   MENU MANUTENÇÕES\n\n')
  print('[1] - Agendar Manutenção')
  print('[2] - Editar Manutenção')
  print('[3] - Excluir Manutenção ')
  print('[4] - Realizar Manutenção ')
  print('[5] - Listar Manutenções ')
  print('[6] - Imprimir Manutenções')
  print('[7] - Voltar o Menu anterior')
  resposta = input()
  os.system('cls' if os.name == 'nt' else 'clear')
  return resposta 


def salvar_clientes(listaClientes):
  #Metodo de criação de pasta caso não exista
  if not os.path.exists('Relatorios/Interno'):
   os.makedirs('Relatorios/Interno')
   os.makedirs('Relatorios/Saida')
  #Parte responsável por salvar Clientes em formato binário
  with open('Relatorios/Interno/dadosC.dat','wb') as arquivo:
    for elemento in listaClientes:
      dump(elemento,arquivo)

def salvar_manutencaoA(lista_Agendadas):
  #Parte responsável por salvar Manuteções agendadas em formato binário
  with open('Relatorios/Interno/dadosMA.dat','wb') as arquivo:
    for elemento in lista_Agendadas:
      dump(elemento,arquivo)
  
def salvar_manutencaoR(lista_Realizadas):
  #Parte responsável por salvar Manuteções realizadas em formato binário
  with open('Relatorios/Interno/dadosMR.dat','wb') as arquivo:
    for elemento in lista_Realizadas:
      dump(elemento,arquivo)

def codigos(anterior,anterior2):
  #Parte responsável por salvar codigos atuais de clientes e manutenções em formato binário
  with open('Relatorios/Interno/codigos.dat','wb') as arquivo:
    dump(anterior,arquivo)
    dump(anterior2,arquivo)

def retorno_Arquivos1(listaClientes, anterior, anterior2):
  #Parte responsável por retornar lista de clientes do formato binário
  with open('Relatorios/Interno/dadosC.dat','rb') as arquivo:
    while True:
      try:
        elemento = load(arquivo)
        listaClientes.append(elemento)
      except EOFError:
        break
  #Parte responsável por retornar lista de códigos do formato binário
  with open('Relatorios/Interno/codigos.dat','rb') as arquivo:
      anterior = load(arquivo)
      anterior2 = load(arquivo)
  return anterior, anterior2

def retorno_Arquivos2(lista_Agendadas, lista_Realizadas):
  #Parte responsável por retornar lista de manutenções agendadas do formato binário
  with open('Relatorios/Interno/dadosMA.dat','rb') as arquivo:
    while True:
      try:
        elemento = load(arquivo)
        lista_Agendadas.append(elemento)
      except EOFError:
        break
  #Parte responsável por retornar lista de manutenções realizadas do formato binário
  with open('Relatorios/Interno/dadosMR.dat','rb') as arquivo:
    while True:
      try:
        elemento = load(arquivo)
        lista_Realizadas.append(elemento)
      except EOFError:
        break
  return lista_Agendadas, lista_Realizadas


def conversorBalancoMes(data,teste):
  #Condicional responsável por testar se mês e ano estão corretos
  if teste == 'n':
    datetime.strptime(data, "%m/%Y").date()
    return True
  elif teste == 's':
    #Condicional responsável tranformar (dd/mm/aaaa) em (mm/aaaa) para padronizar
    data = datetime.strptime(data, "%d/%m/%Y").date()
    data = data.strftime("%m/%Y")
    return data

def valor_BalancoMes(data, lista_Realizadas):
  balanco_mes = []
  teste = 's'
  for elemento in lista_Realizadas:
    agenda = elemento.agenda
    agenda = conversorBalancoMes(agenda,teste)
    #Tendo a data informada pelo usuario e data padronizada pelo conversor, é feita a comparação
    if agenda == data:
      balanco_mes.append(elemento)
    
  if len(balanco_mes) == 0:
    print(f'\n\nNão foi encontrada nenhuma manutenção no período de {data}!')
    return
  
  else:
    total = 0
    quant = 0
    print('\n\nAgendamento |     Peca   |   Codigo   |   Valor    |  Validade  | codigo/Cliente\n')
    for elemento in balanco_mes:
      total += elemento.valor
      quant += 1
      print(f'{elemento.agenda:<12}|{elemento.peca:^12}|{elemento.codManu:^12}|{elemento.valor:^12.2f}|{elemento.validade[1]:^8}{elemento.validade[0]:<4}|{elemento.codinome[0]:>6} / {elemento.codinome[1]:<6}')

    #Saindo do loop, é mostrado os valores abaixo
    print(f'\n\nMês: {data}\nManutenções: {quant}\nValor Total: R$ {total:.2f}')

    gravar = input('Deseja gravar esses informações em um arquivo externo [S/N]?').lower()
    if gravar == 's':
      with open('Relatorios/Saida/Balanço_do_Mês.txt', 'w') as arquivo:
        arquivo.write('Agendamento |     Peca   |   Codigo   |   Valor    |  Validade  | codigo/Cliente\n\n')
        for elemento in balanco_mes:
          arquivo.write(f'{elemento.agenda:<12}|{elemento.peca:^12}|{elemento.codManu:^12}|{elemento.valor:^12.2f}|{elemento.validade[1]:^8}{elemento.validade[0]:<4}|{elemento.codinome[0]:>6} / {elemento.codinome[1]:<6}\n')
        arquivo.write(f'\n\nMês: {data}\nManutenções: {quant}\nValor Total: R$ {total:.2f}')
    else:
      print('Gravação não Realizada!')
    return