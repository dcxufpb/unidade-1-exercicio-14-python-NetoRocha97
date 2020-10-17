# coding: utf-8

import cupom
import pytest
import unittest
from datetime import datetime
from cupom import Venda, Endereco, Loja, ItemVenda, Produto

test = unittest.TestCase()

#verificações
def verifica_campo_obrigatorio_Venda(mensagem_esperada, venda):
    with pytest.raises(Exception) as excinfo:
        venda.dados_venda()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

def verifica_campo_obrigatorio_ItemVenda(mensagem_esperada, itemVenda):
    with pytest.raises(Exception) as excinfo:
        itemVenda.dados_item()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

    
def valida_item(mensagem_esperada, item, produto, quantidade):
    with pytest.raises(Exception) as excinfo:
        venda.adicionar_item(item, produto, quantidade)
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

def valida_impressao(mensagem_esperada, venda):
    with pytest.raises(Exception) as excinfo:
        venda.imprimir_cupom()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"

DATA_HORA = "11/11/11 11:11:11V"
CCF_VENDA = "021784"
COO_VENDA = "035804"
QUANTIDADE01 = 2
QUANTIDADE02 = 3
UNIDADE= "R$"
SUBSTITUICAO_TRIBUTARIA = ST = "ST" 
CODIGO1 = "001"
DESCRICAO1 = "Maçã"
VALOR_UNITARIO1 = VU1 = 1.11
VALOR_UNITARIO3 = -2
CODIGO2 = "002"
DESCRICAO2 = "Banana"
VALOR_UNITARIO2 = VU2 = 2
CODIGO3 = "003"
CODIGO4 = "004"
ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

produto1 = cupom.Produto(100, "Banana", "cx", 7.45, "ST")
produto2 = cupom.Produto(101, "Laranja", "cx", 3.32, "ST")

DATA_HORA_VENDA = datetime(2020, 11, 25, 10, 30, 40)

venda = cupom.Venda(LOJA_COMPLETA, DATA_HORA_VENDA, CCF_VENDA, COO_VENDA)
# Validações

LOJA_VAZIA = cupom.Venda("", DATA_HORA_VENDA, CCF_VENDA, COO_VENDA)
LOJA_NULA = cupom.Venda(None, DATA_HORA_VENDA, CCF_VENDA, COO_VENDA)

DATA_HORA_VAZIO = cupom.Venda(LOJA_COMPLETA, "", CCF_VENDA, COO_VENDA)
DATA_HORA_NULO = cupom.Venda(LOJA_COMPLETA, None, CCF_VENDA, COO_VENDA)

CCF_VENDA_VAZIO = cupom.Venda(LOJA_COMPLETA, DATA_HORA_VENDA, "", COO_VENDA)
CCF_VENDA_NULO = cupom.Venda(LOJA_COMPLETA, DATA_HORA_VENDA, None, COO_VENDA)

COO_VENDA_VAZIO = cupom.Venda(LOJA_COMPLETA, DATA_HORA_VENDA, CCF_VENDA, "")
COO_VENDA_NULO = cupom.Venda(LOJA_COMPLETA, DATA_HORA_VENDA, CCF_VENDA, None)

def test_valida_loja():
    verifica_campo_obrigatorio_Venda(
        "O campo loda da venda é obrigatório", LOJA_VAZIA)
    verifica_campo_obrigatorio_Venda(
        "O campo loda da venda é obrigatório", LOJA_NULA)
        
def test_valida_datahora():
    verifica_campo_obrigatorio_Venda(
        "O campo datahora da venda é obrigatório", DATA_HORA_VAZIO)
    verifica_campo_obrigatorio_Venda(
        "O campo datahora da venda é obrigatório", DATA_HORA_NULO)

def test_valida_ccf():
    verifica_campo_obrigatorio_Venda(
        "O campo ccf da venda é obrigatório", CCF_VENDA_VAZIO)
    verifica_campo_obrigatorio_Venda(
        "O campo ccf da venda é obrigatório", CCF_VENDA_NULO)

def test_valida_coo():
    verifica_campo_obrigatorio_Venda(
        "O campo coo da venda é obrigatório", COO_VENDA_VAZIO)
    verifica_campo_obrigatorio_Venda(
        "O campo coo da venda é obrigatório", COO_VENDA_NULO)

enderecoCompleto = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO,
                            ESTADO, CEP)
                            
lojaCompleta = cupom.Loja(NOME_LOJA, enderecoCompleto, TELEFONE, OBSERVACAO, CNPJ, 
                    INSCRICAO_ESTADUAL) 
                    
venda_sem_itens = Venda(
    lojaCompleta,
    CCF_VENDA,
    COO_VENDA,
    DATA_HORA_VENDA
)

produto01 = Produto(
    CODIGO1, 
    DESCRICAO1, 
    UNIDADE, 
    VALOR_UNITARIO1, 
    SUBSTITUICAO_TRIBUTARIA
)

produto02 = Produto(
    CODIGO2, 
    DESCRICAO2, 
    UNIDADE, 
    VALOR_UNITARIO2, 
    SUBSTITUICAO_TRIBUTARIA
    )

produto03 = Produto(
    CODIGO3, 
    DESCRICAO1, 
    UNIDADE, 
    VALOR_UNITARIO3, 
    SUBSTITUICAO_TRIBUTARIA
)

produto04 = Produto(
    CODIGO4, 
    DESCRICAO2, 
    UNIDADE, 
    VALOR_UNITARIO2, 
    SUBSTITUICAO_TRIBUTARIA
    )

produto_gratis = Produto(
    CODIGO1, 
    DESCRICAO1, 
    UNIDADE, 
    0, 
    SUBSTITUICAO_TRIBUTARIA
    )
    
item01 = ItemVenda(1, produto01, QUANTIDADE01)

item02 = ItemVenda(2, produto01, QUANTIDADE02)

vendaComDoisItens = Venda(
    lojaCompleta, 
    CCF_VENDA, COO_VENDA, 
    DATA_HORA_VENDA, 
    [item01, item02]
    )

item03 = ItemVenda(3, produto03, QUANTIDADE01)

item04 = ItemVenda(4, produto04, QUANTIDADE02)

vendaComDoisItensNegativo = Venda(
    lojaCompleta, 
    CCF_VENDA, COO_VENDA, 
    DATA_HORA_VENDA, 
    [item03, item04]
    )

MENSAGEM_VENDAS_SEM_ITEM = "O campo item da venda é obrigatório"
MENSAGEM_ITEM_DUPLICADO = "Produto duplicado"
MENSAGEM_VALOR_PRODUTO = "Produto com valor unitário zero ou negativo"
MENSAGEM_QUANT_ITEM = "Item com quantidade zero ou negativa"

def test_sem_itens():
    valida_impressao(
        MENSAGEM_VENDAS_SEM_ITEM, 
        venda_sem_itens)

def test_duplicacao_item():
    valida_item(
        MENSAGEM_ITEM_DUPLICADO, 
        vendaComDoisItens, 
        produto01, 
        5)

def test_valor_produto():
    valida_item(
        MENSAGEM_VALOR_PRODUTO, 
        vendaComDoisItensNegativo,
        produto_gratis,
        3)

def test_quant_item():
    valida_item(
        MENSAGEM_QUANT_ITEM, 
        venda_sem_itens,
        produto01,
        0)