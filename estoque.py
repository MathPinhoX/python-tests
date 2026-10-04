import json

def executar():
    dados=json.load(open("estoque.json",encoding="utf-8"))
    codigo=int(input("Código: "))
    tipo=input("E=Entrada / S=Saída: ").upper()
    qtd=int(input("Quantidade: "))
    p=next((x for x in dados["estoque"] if x["codigoProduto"]==codigo),None)
    if not p:
        print("Produto não encontrado"); return
    if tipo=="E": p["estoque"]+=qtd
    elif tipo=="S" and qtd<=p["estoque"]: p["estoque"]-=qtd
    else:
        print("Movimentação inválida"); return
    print("ID:",str(codigo)+"-"+str(qtd))
    print("Estoque final:",p["estoque"])
