from tkinter import *
from tkinter import ttk

def new_window2():
    bloc = Tk()
    bloc.geometry("350x400+700+200")
    bloc.title("Blocos")
    bloc.resizable(0,0)

    #Função para fazer o calculo Blocos
    def soma2():
        qnt = int(ent.get())
        cor = str(cores.get())
        qt1 = str(qt.get())
        carb1 = str(carb.get())
        capadiv = str(via.get())
        picote = str(pic.get())
        numdiv = str(num.get())

        if qnt <= 5:
            qnt_tot = 100
        elif qnt <= 10:
            qnt_tot = 200
        elif qnt <= 20:
            qnt_tot = 250
        elif qnt <= 35:
            qnt_tot = 300
        elif qnt <= 50:
            qnt_tot = 400
        else:
            qnt_tot = 0

        if cor == "1/0":
            cor_tot = 10
        elif cor == "1/1":
            cor_tot = 20
        elif cor == "4/0":
            cor_tot = 30
        elif cor == "4/1":
            cor_tot = 40
        elif cor == "4/4":
            cor_tot = 50
        else:
            cor_tot = 0

        if qt1 == "1":
            qt1_tot = 10
        elif qt1 == "2":
            qt1_tot = 20
        elif qt1 == "3":
            qt1_tot = 30
        elif qt1 == "4":
            qt1_tot = 40
        elif qt1 == "5":
            qt1_tot = 50
        else:
            qt1_tot = 0

        if carb1 == "Sem carbono":
            carb1_tot = 25
        elif carb1 == "Carbonado":
            carb1_tot = 35
        elif carb1 == "Auto copiativo":
            carb1_tot = 50

        if capadiv == "50/1":
            capa = 25
        elif capadiv == "100/1":
            capa = 50
        else:
            capa = 0

        if picote == "Sim":
            serrilha = 50
        elif picote == "Não":
            serrilha = 5
        else:
            serrilha = 0

        if numdiv == "Sim":
            numero = 50
        elif numdiv == "Não":
            numero = 5
        else:
            numero = 0

        tot = (qnt_tot + cor_tot + qt1_tot + carb1_tot + capa + serrilha + numero)
        total["text"] = f'R$ {tot},00'

#Tela do calculo dos Blocos
    lb = Label(bloc, text="Quantidade")
    lb.grid(row=0, column=0, pady=20)
    ent = Entry(bloc)
    ent.grid(row=0, column=1)

    lb2 = Label(bloc, text="Vias")
    lb2.grid(row=1, column=0)
    via = ttk.Combobox(bloc, values=[
        "50/1","100/1"])
    via.grid(row=1, column=1, pady=10)

    cor = Label(bloc, text="Cor impressão")
    cor.grid(row=3, column=0, padx=10, pady=10)
    cores = ttk.Combobox(bloc, values=[
        "1/0","1/1","4/0","4/1","4/4"])
    cores.grid(row=3, column=1)

    quantV = Label(bloc, text="Quant. de Vias")
    quantV.grid(row=4, column=0, pady=20)
    qt = ttk.Combobox(bloc, values=[
        "1","2","3","4","5"])
    qt.grid(row=4, column=1)

    picote = Label(bloc, text="Picote")
    picote.grid(row=5, column=0)
    pic = ttk.Combobox(bloc, values=[
        "Sim","Não"])
    pic.grid(row=5, column=1)

    numero = Label(bloc, text="Numerado")
    numero.grid(row=6, column=0)
    num = ttk.Combobox(bloc, values=[
        "Sim","Não"])
    num.grid(row=6, column=1, pady=20)

    carbono = Label(bloc, text="Carbono")
    carbono.grid(row=7, column=0, pady=20)
    carb = ttk.Combobox(bloc, values=[
        "Sem carbono","Carbonado","Auto copiativo"])
    carb.grid(row=7, column=1)

    btn = Button(bloc, text="Calcular", command=soma2)
    btn.grid(row=8, column=0)

    total = Label(bloc, text="R$ 0,00", padx=10)
    total.grid(row=8, column=1)
