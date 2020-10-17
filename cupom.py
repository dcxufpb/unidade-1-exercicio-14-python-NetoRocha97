# coding: utf-8

class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep

  def validar_campos_obrigatorios(self):
    
    if not self.logradouro:
      raise Exception ("O campo logradouro do endereço é obrigatório")

    if not self.municipio:
      raise Exception ("O campo município do endereço é obrigatório")

    if not self.estado:
      raise Exception ("O campo estado do endereço é obrigatório")

  def dados_endereco(self):

    self.validar_campos_obrigatorios()

    _logradouro = self.logradouro + ", "
    _numero = self.numero and str(self.numero) or "s/n"
    _complemento = self.complemento and " " + self.complemento or ""
    _bairro = self.bairro and self.bairro + " - " or ""
    _municipio = self.municipio + " - "

    _cep = self.cep and ("CEP:" + self.cep) or ""

    return (f"""{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{self.estado}
{_cep}""")

class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual
    self.vendas = []


  def vender(self, datahora, ccf, coo):
    nova_venda = Venda(self, datahora, ccf, coo)
    self.vendas.append(nova_venda)
    return nova_venda

  def validar_campos_obrigatorios(self):

    if not self.nome_loja:
      raise Exception ("O campo nome da loja é obrigatório")

    if not self.cnpj:
      raise Exception ("O campo CNPJ da loja é obrigatório")

    if not self.inscricao_estadual:
      raise Exception ("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):

    self.validar_campos_obrigatorios()

    _telefone = self.telefone and ("Tel " + self.telefone) or ""
    _telefone = (_telefone and self.endereco.cep) and (" " + _telefone) or _telefone

    _observacao = self.observacao and self.observacao or ""

    _cnpj = "CNPJ: " + self.cnpj
    _inscricao_estadual = "IE: " + self.inscricao_estadual
    
    return (f"""{self.nome_loja}
{self.endereco.dados_endereco()}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}""")

class Produto:

  def __init__(self, codigo, descricao, unidade, valor_unitario, 
               substituicao_tributaria):
    self.codigo = codigo
    self.descricao = descricao
    self.unidade = unidade
    self.valor_unitario = valor_unitario
    self.substituicao_tributaria = substituicao_tributaria                                                 

class ItemVenda:

  def __init__(self, item, produto, quantidade):
    self.item = item
    self.produto = produto
    self.quantidade = quantidade

  def validar_campos_obrigatorios(self):

    if not self.produto:
      raise Exception ("O campo produto da venda é obrigatório")

    if not self.quantidade:
      raise Exception ("O campo quantidade da venda é obrigatório")

  def valor_item(self):
    return self.quantidade * self.produto.valor_unitario

  def dados_item(self):
    
    self.validar_campos_obrigatorios()

    return '''{item} {codigo} {descricao} {qtd} {un} {vl_unit:.2f} {st} {vl_item:.2f}'''.format(
        item=self.item, codigo=self.produto.codigo, 
        descricao=self.produto.descricao, qtd=self.quantidade, 
        un=self.produto.unidade, vl_unit=self.produto.valor_unitario, 
        st=self.produto.substituicao_tributaria, vl_item=self.valor_item())


class Venda:

  def __init__(self, loja, datahora, ccf, coo, itens = []):
    self.loja = loja
    self.datahora = datahora
    self.ccf = ccf
    self.coo = coo
    self.itens = itens

  def verifica_duplicacao(self, codigo):
    for item in self.itens:
      if (item.produto.codigo == codigo):
        return True
    return False

  def validar_item_adicionado(self, produto, quantidade):

    if produto.valor_unitario <= 0:
      raise Exception ("Produto com valor unitário zero ou negativo")

    if quantidade <= 0:
      raise Exception ("Item com quantidade zero ou negativa")

    if self.verifica_duplicacao(produto.codigo):
      raise Exception ("Produto duplicado")


  def adicionar_item(self, item, produto, quantidade):
    
    for item_unico in item.itens:
	    self.validar_item_adicionado( item_unico.produto,  quantidade )
	    item_venda = ItemVenda( item_unico, item_unico.produto, quantidade )
	    self.itens.append( item_venda )


  def validar_campos_obrigatorios(self):

    if not self.loja:
      raise Exception ("O campo loda da venda é obrigatório")
       
    if not self.datahora:
      raise Exception ("O campo datahora da venda é obrigatório")

    if not self.ccf:
      raise Exception ("O campo ccf da venda é obrigatório")

    if not self.coo:
      raise Exception ("O campo coo da venda é obrigatório")

    if not self.itens:
      raise Exception ("O campo item da venda é obrigatório")


  def dados_venda(self):

    self.validar_campos_obrigatorios()

    texto_data = self.datahora.strftime("%d/%m/%Y")
    texto_hora = self.datahora.time().strftime("%H:%M:%S")
    
    _hora = texto_hora +"V"
    _ccf = "CCF:" + self.ccf
    _coo = "COO: " + self.coo
    
    return (f"""{texto_data} {_hora} {_ccf} {_coo}""")

  def dados_itens(self):
    dados = ["ITEM CODIGO DESCRICAO QTD UN VL UNIT(R$) ST VL ITEM(R$)"]
    for item_linha in self.itens:
      dados.append(item_linha.dados_item())
    return '\n'.join(dados)

  def calcular_total(self):
    totais = [item_linha.valor_item() for item_linha in self.itens]
    return sum(totais)

  def imprimir_cupom(self):
    dados_loja = self.loja.dados_loja()
    dados_venda = self.dados_venda()
    dados_itens = self.dados_itens()
    total = self.calcular_total()
    return '''{loja}
------------------------------
{venda}
   CUPOM FISCAL   
{itens}
------------------------------
TOTAL R$ {total:.2f}
'''.format(loja=dados_loja, venda=dados_venda, itens=dados_itens, total=total)