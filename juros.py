from datetime import date, datetime

def executar():
    valor=float(input("Valor: R$ "))
    venc=datetime.strptime(input("Vencimento DD/MM/AAAA: "),"%d/%m/%Y").date()
    dias=max((date.today()-venc).days,0)
    juros=valor*0.025*dias
    print("Dias em atraso:",dias)
    print("Juros: R$",round(juros,2))
    print("Valor atualizado: R$",round(valor+juros,2))
