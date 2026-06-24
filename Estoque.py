# Sistema de Controle de Estoque e Vendas
# versao 2.0 - correções iniciais de dívida técnica
# autor:  Integrantes do relatório

import datetime
import os

# D1: Configurações do sistema 
# D1: Senha obtida via variável de ambiente
SENHA_ADMIN = os.getenv("ESTOQUE_ADMIN_PWD")

# D3: Magic Numbers
LIMITE_ESTOQUE_BAIXO = 5
LIMITE_PRECO_DESCONTO_VENDA = 100
PERCENTUAL_DESCONTO_VENDA = 0.10  
LIMITE_PRECO_DESCONTO_SIMULACAO = 200
PERCENTUAL_DESCONTO_SIMULACAO = 0.15  

produtos = []


# Argumento mutavel (D2) e Ajuste de variáveis (D4)
def add(nome, preco, quantidade, hist=None):
    if hist is None:
        hist = []
    produtos.append({"nome": nome, "preco": preco, "qtd": quantidade})
    hist.append(nome)
    print("Produto adicionado!")


def vender(nome, quantidade):
# D6: Iteracao manual com range(len) aceita conscientemente
    for i in range(len(produtos)):
        if produtos[i]["nome"] == nome:
            if produtos[i]["qtd"] >= quantidade:
                produtos[i]["qtd"] = produtos[i]["qtd"] - quantidade
                # D4: Ajuste de nomenclaturas 
                total = produtos[i]["preco"] * quantidade
                
                # D3: Retirada de Magic Numbers 
                if total > LIMITE_PRECO_DESCONTO_VENDA:
                    descontoVenda = total * PERCENTUAL_DESCONTO_VENDA
                    total -= descontoVenda
                print("Venda realizada. Total: " + str(total))
                return total
            else:
                print("Estoque insuficiente")
                return 0
    print("Produto nao encontrado")
    return 0


# D4: Ajuste de nomenclaturas 
def calcular_total(preco, quantidade):
    total = preco * quantidade
    # D3: Retirada de Magic Numbers
    if total > LIMITE_PRECO_DESCONTO_SIMULACAO:
        descontoSimulacao = total * PERCENTUAL_DESCONTO_SIMULACAO                   
        total -= descontoSimulacao
    return total


def listar():
    print("=== PRODUTOS ===")
    for produto in produtos:
        print(produto["nome"] + " - R$" + str(produto["preco"]) + " - qtd: " + str(produto["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for produto in produtos:
        # Retirada de Magic Numbers (D3)
        if produto["qtd"] < LIMITE_ESTOQUE_BAIXO:        
            print(produto["nome"] + " esta com estoque baixo (" + str(produto["qtd"]) + ")")


# D7: exclusão do bloco de codigo morto comentado (funcao exportar).


def relatorio_vendas():
    # D8: Funcionalidade Incompleta (Pagar Depois).
    # TODO: Implementar a logica real de consolidacao de vendas no proximo ciclo.
    pass


def menu():
    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        opcao = input("Opcao: ")
        
        # D5: Cadeia de if/elif sequencial
        if opcao == "1":
            nome_input = input("Nome: ")
            preco_input = float(input("Preco: "))
            qtd_input = int(input("Qtd: "))
            add(nome_input, preco_input, qtd_input)
        elif opcao == "2":
            nome_input = input("Nome do produto: ")
            qtd_input = int(input("Quantidade: "))
            vender(nome_input, qtd_input)
        elif opcao == "3":
            listar()
        elif opcao == "4":
            relatorio_estoque_baixo()
        elif opcao == "5":
            senha = input("Senha: ")
            if senha == SENHA_ADMIN:
                print("Acesso liberado")
            else:
                print("Senha errada")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")


menu()
