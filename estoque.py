import json
from time import time_ns

def executar():
    dados=json.load(open("estoque.json",encoding="utf-8"))
    codigo=int(input("Código: "))
    tipo=input("E=Entrada / S=Saída: ").upper()
    qtd=int(input("Quantidade: "))
    desc=input("Descrição: ")
    p=next((x for x in dados["estoque"] if x["codigoProduto"]==codigo),None)
    if not p or qtd<=0:
        print("Dados inválidos"); return
    if tipo=="E": p["estoque"]+=qtd
    elif tipo=="S" and qtd<=p["estoque"]: p["estoque"]-=qtd
    else:
        print("Movimentação inválida"); return
    print("ID:",time_ns())
    print("Descrição:",desc)
    print("Estoque final:",p["estoque"])
