from datetime import datetime
from dateutil.relativedelta import relativedelta

#Crianção de classe e também método de agendamento de manutenção
class Servico:
  def __init__(self, codManutencao, peca, valor, validade, agenda, codinome):
    self.codManu = codManutencao
    self.peca = peca
    self.valor = valor
    self.validade = validade
    self.agenda = agenda
    self.codinome = codinome

  def set_peca(self, novo_peca):
    self.peca = novo_peca
    
  def set_valor(self, novo_valor):
    self.valor = novo_valor

  def set_validade(self, novo_validade):
    self.validade = novo_validade  

  def set_agenda(self, novo_agenda):
    self.agenda = novo_agenda

#Função de busca em lista para substituir get(x) dos dicionarios.
def buscaM(codigo, lista_Agendadas):
  for elemento in lista_Agendadas:
      if elemento.codManu == codigo:
        return elemento
  return None

#Teste de data digitada corretamente.
def conversorTempo(agenda):
  datetime.strptime(agenda, "%d/%m/%Y").date()
  return

#Criação de nova data na realização da manutenção.
def novo_agendamento(data,meses):
  #Caso a validade seja em meses.
  if meses[0] == 'M':
    data = datetime.strptime(data, "%d/%m/%Y").date()
    novo_agenda = data + relativedelta(months=meses[1])
    novo_agenda = novo_agenda.strftime("%d/%m/%Y")
  #Caso a validade seja em dias.
  else:
    data = datetime.strptime(data, "%d/%m/%Y").date()
    novo_agenda = data + relativedelta(days=meses[1])
    novo_agenda = novo_agenda.strftime("%d/%m/%Y")
  return novo_agenda

def editarMan(codigo,edicao,lista_Agendadas):
  #Mudança de Nome
  if edicao == '1':
    novo_peca = input('\nInforme o novo nome da peça: ')
    buscaM(codigo, lista_Agendadas).set_peca(novo_peca)
    return
  #Mudança do preço da peça
  if edicao == '2':
    while True:
      try:
        novo_valor = float(input('\nInforme o valor da peça: '))
        break
      except ValueError:
        print('\nPreço incorreto! ex. 120.00\n')
    buscaM(codigo, lista_Agendadas).set_valor(novo_valor)
    return
  #Mudança da validade da peça
  if edicao == '3':
    while True:
      tipo = input('A validade é em [M] meses ou [D] dias? ').upper()
      if tipo == 'M' or tipo == 'D':
        try:
          prazo = int(input('\nInforme o prazo de Validade da Peça: '))
          novo_validade = tipo,prazo
          break
        except ValueError:
          print('\nValidade incorreta! ex. 24 (2 anos) ou 45 dias\n')
      else:
        print('\nTipo de validade não reconhecida, digite novamente!\n')
    buscaM(codigo, lista_Agendadas).set_validade(novo_validade)
    return
  #Mudança do dia da realização da manutenção
  if edicao == '4':
    while True:
      novo_agenda = input('\nInforme o dia para realização do serviço (dd/mm/aaaa): ')
      try:
        conversorTempo(novo_agenda)
        break
      except:
        print('\nData incorreta ou inexistente! ex.(07/06/2021)\n')
    buscaM(codigo, lista_Agendadas).set_agenda(novo_agenda)
    return
  
  
def realizarMan(codigo, lista_Agendadas, lista_Realizadas, codigoAtual):
  resposta = input(f'Confirma o realizamento do serviço {buscaM(codigo, lista_Agendadas).peca}? [S/N] ')
  if resposta == 's':
    # Variavel auxiliar de edição
    item = buscaM(codigo, lista_Agendadas)
    #Adicionando a manutenção a lista de realizadas
    lista_Realizadas.append(buscaM(codigo, lista_Agendadas))
    #excluindo a manutenção a lista de agendadas
    lista_Agendadas.remove(buscaM(codigo, lista_Agendadas))

    #Repassando informações mantidas do manutenção
    peca = item.peca
    valor = item.valor
    validade = item.validade
    codinome = item.codinome
    data = item.agenda

    #calculando novo agendamento
    agenda = novo_agendamento(data,validade)

    #Inserindo novo agendamento 
    servico = Servico(codigoAtual, peca, valor, validade, agenda, codinome)
    lista_Agendadas.append(servico)
    print('\n  MANUTENÇÃO REALIZADA E NOVO AGENDAMENTO MARCADO!\n')
    return    
  else:
    print('\n  Operação não realizada!\n')

def listarMan(lista_Agendadas, lista_Realizadas, pergunta):
  #Opção para manuteções Agendadas
  if pergunta == '1':
    if len(lista_Agendadas) == 0:
      print('\n\nNenhuma manutenção encontrada!')
      return
    # Visualização para usuario
    print(f'\n\n  Codigo    |    Peça    |    Valor   |  Validade  | Agendamento |  codigo/Cliente  ')
    
    for i in range(len(lista_Agendadas)):
      elemento = lista_Agendadas[i]
      print(f'{elemento.codManu:^12}|{elemento.peca:^12}|{elemento.valor:^12.2f}|{elemento.validade[1]:^8}{elemento.validade[0]:<4}|{elemento.agenda:^13}|{elemento.codinome[0]:>6} / {elemento.codinome[1]:<6}')
    return

  #Opção para manuteções Realizadas
  elif pergunta == '2':
    if len(lista_Realizadas) == 0:
      print('\n\nNenhuma manutenção encontrada!')
      return
    # Visualização para usuario
    print(f'\n\n   Codigo   |    Peça    |    Valor   |  Validade  | Agendamento |  codigo/Cliente  ')
    
    for i in range(len(lista_Realizadas)):
      elemento = lista_Realizadas[i]
      print(f'{elemento.codManu:^12}|{elemento.peca:^12}|{elemento.valor:^12.2f}|{elemento.validade[1]:^8}{elemento.validade[0]:<4}|{elemento.agenda:^12}|{elemento.codinome[0]:>6} / {elemento.codinome[1]:<6}')
    return

def ordenar_por_data(lista):
  #Mudança de data do formato string para o formato Data Python
  for elemento in lista:
    elemento.agenda = datetime.strptime(elemento.agenda, "%d/%m/%Y").date()
  #Ordenação da lista pelo método Bubble Sort pelas datas 
  t = len(lista)
  for i in range(1, t):
    for j in range(t-1, i-1, -1):
      if (lista[j-1].agenda > lista[j].agenda):
        lista[j],lista[j-1] = lista[j-1],lista[j]
  #Retransformando as datas para o formato de string
  for elemento in lista:
    elemento.agenda = elemento.agenda.strftime("%d/%m/%Y")
  return

def imprimir_manutencoes(lista_Agendadas):
  #Impressão em arquivo.txt as manutenções agendadas
  with open('Relatorios/Saida/Manutenções_Agendadas.txt', 'w') as arquivo:
    arquivo.write('Agendamento    |      Peca     |     Codigo    |     Valor     |    Validade   |   codigo/Cliente \n')
    for elemento in lista_Agendadas:
      arquivo.write(f'{elemento.agenda:<15}|{elemento.peca:^15}|{elemento.codManu:^15}|{elemento.valor:^15.2f}|{elemento.validade[1]:^10}{elemento.validade[0]:<5}|{elemento.codinome[0]:>6} / {elemento.codinome[1]:<6}\n')
  return