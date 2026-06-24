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


# Argumento mutavel (D2)
def add(n, p, q, hist=None):
    if hist is None:
        hist = []
    produtos.append({"nome": n, "preco": p, "qtd": q})
    hist.append(n)
    print("Produto adicionado!")


def vender(nome, quantidade):
    for i in range(len(produtos)):
        if produtos[i]["nome"] == nome:
            if produtos[i]["qtd"] >= quantidade:
                produtos[i]["qtd"] = produtos[i]["qtd"] - quantidade
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


# calcula o total de uma compra (usado no relatorio)
def calcular_total(preco, quantidade):
    t = preco * quantidade
    # D3: Retirada de Magic Numbers
    if t > LIMITE_PRECO_DESCONTO_SIMULACAO:
        descontoSimulacao = t * PERCENTUAL_DESCONTO_SIMULACAO                   
        t -= descontoSimulacao
    return t


def listar():
    print("=== PRODUTOS ===")
    for x in produtos:
        print(x["nome"] + " - R$" + str(x["preco"]) + " - qtd: " + str(x["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for x in produtos:
        # Retirada de Magic Numbers (D3)
        if x["qtd"] < LIMITE_ESTOQUE_BAIXO:        
            print(x["nome"] + " esta com estoque baixo (" + str(x["qtd"]) + ")")


# funcao antiga, nao usamos mais
# def exportar():
#     f = open("dados.txt", "w")
#     for x in produtos:
#         f.write(str(x))
#     f.close()


def relatorio_vendas():
    # TODO: implementar de verdade
    pass


def menu():
    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        op = input("Opcao: ")
        if op == "1":
            n = input("Nome: ")
            p = float(input("Preco: "))
            q = int(input("Qtd: "))
            add(n, p, q)
        elif op == "2":
            n = input("Nome do produto: ")
            q = int(input("Quantidade: "))
            vender(n, q)
        elif op == "3":
            listar()
        elif op == "4":
            relatorio_estoque_baixo()
        elif op == "5":
            s = input("Senha: ")
            if s == SENHA_ADMIN:
                print("Acesso liberado")
            else:
                print("Senha errada")
        elif op == "0":
            break
        else:
            print("Opcao invalida")


menu()
