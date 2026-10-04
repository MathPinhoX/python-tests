import json

def taxa_comissao(valor):
    if valor < 100:
        return 0
    if valor < 500:
        return 0.01
    return 0.05

def executar():
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    resumo = {}
    for venda in dados["vendas"]:
        vendedor = venda["vendedor"]
        valor = venda["valor"]
        comissao = valor * taxa_comissao(valor)

        if vendedor not in resumo:
            resumo[vendedor] = {"total": 0, "comissao": 0}

        resumo[vendedor]["total"] += valor
        resumo[vendedor]["comissao"] += comissao

    for vendedor, info in resumo.items():
        print(vendedor, round(info["comissao"], 2))
