import comissoes, estoque, juros

while True:
    print("\n1 - Comissões")
    print("2 - Movimentação de estoque")
    print("3 - Juros por atraso")
    print("0 - Sair")
    op=input("Opção: ")
    if op=="1": comissoes.executar()
    elif op=="2": estoque.executar()
    elif op=="3": juros.executar()
    elif op=="0": break
    else: print("Opção inválida")
