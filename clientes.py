#Crianção de classe e também método de cadastramento
class Cliente:
  def __init__(self, cod, nome, endereco, telefone):
    self.cod = cod
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    
  def set_nome(self, novo_nome):
    self.nome = novo_nome

  def set_endereco(self, novo_endereco):
    self.endereco = novo_endereco

  def set_telefone(self, novo_telefone):
    self.telefone = novo_telefone

#Função de busca em lista para substituir get(x) dos dicionarios.
def busca(codigo, lista_Inicial):
  for elemento in lista_Inicial:
      if elemento.cod == codigo:
        return elemento
  return None

# Busca para procurar manutenção vinculado ao cliente
def busca_especifica(codigo,lista_Agendadas):
  for elemento in lista_Agendadas:
      if elemento.codinome[0] == codigo:
        return elemento
  return None

#ordenação por metódo de Bubble Sort
def ordenar_lista(listaClientes):
  t = len(listaClientes)
  for i in range(1, t):
    for j in range(t-1, i-1, -1):
      if (listaClientes[j-1].nome > listaClientes[j].nome):
        listaClientes[j],listaClientes[j-1] = listaClientes[j-1],listaClientes[j]
  return


def editarCli(codigo,edicao,listaClientes):
  if edicao == '1':
    novo_nome = input('Informe o novo nome: ').title()
    busca(codigo,listaClientes).set_nome(novo_nome)
    return
  if edicao == '2':
    novo_endereco = input('Informe o novo endereco: ')
    busca(codigo,listaClientes).set_endereco(novo_endereco)
    return
  if edicao == '3':
    novo_telefone = input('Informe o novo telefone: ')
    busca(codigo,listaClientes).set_telefone(novo_telefone)
    return


def excluirCli(codigo,listaClientes):
  resposta = input(f'\nDeseja excluir os dados de {busca(codigo,listaClientes).nome}? [S/N]\n ').lower()
  if resposta == 's':
    listaClientes.remove(busca(codigo,listaClientes))
    print('\nCliente excluído com sucesso!\n')
    return
  else: 
    print('\nCliente não deletado!\n')
    return        


def listarCli(listaClientes, pergunta):
  if len(listaClientes) == 0:
    print('\n\nNenhum dado Cadastrado!')
    return
  #Visualização completa dos clientes.
  if pergunta == '1':
    # Visualização para usuario
    print('\n\n    Cliente    |     Codigo    |   Endereço    |    Telefone   ')
    for i in range(len(listaClientes)):
      print(f'{listaClientes[i].nome:^15}|{listaClientes[i].cod:^15}|{listaClientes[i].endereco:^15}|{listaClientes[i].telefone:^15}')
    return
  #Visualização de cliente especificado por codigo.
  elif pergunta == '2':
    cod = input('\n\nQual o codigo do cliente a ser listado os dados? ')
    for elemento in listaClientes:
      if elemento.cod == cod:
        print(f'\nNome: {elemento.nome}')
        print(f'Endereco: {elemento.endereco}')
        print(f'Telefone: {elemento.telefone}')
        return
    print('Nenhum dado encontrado para este codigo!')
    return