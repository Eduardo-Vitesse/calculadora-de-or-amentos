from tkinter import *
from tkinter import ttk

def new_window3():
    conv = Tk()
    conv.geometry("350x400+700+200")
    conv.title("Convite de Casamento")
    conv.resizable(0,0)

    #Função para fazer o calculo Convites
    def soma3():
        qnt = int(ent.get())
        ppl = str(papel.get())
        cor = str(cores.get())
        
        if qnt <= 500:
            qnt_tot = 100
        elif qnt <= 1000:
            qnt_tot = 200
        elif qnt <= 2000:
            qnt_tot = 250
        elif qnt <= 3500:
            qnt_tot = 300
        elif qnt <= 5000:
            qnt_tot = 400
        else:
            qnt_tot = 0

        if ppl == "Ap 115":
            ppl_tot = 10
        elif ppl == "Ap 150":
            ppl_tot = 20
        elif ppl == "Ap 240":
            ppl_tot = 30
        elif ppl == "Couchê 150":
            ppl_tot = 40
        elif ppl == "Couchê 300":
            ppl_tot = 50
        elif ppl == "Triplex":
            ppl_tot = 60
        else:
            ppl_tot = 0
        
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

        tot = (qnt_tot + ppl_tot + cor_tot)
        total["text"] = f'R$ {tot},00'

#Tela para o calculo Convites
    lb = Label(conv, text="Quantidade")
    lb.grid(row=0, column=0, padx=20, pady=20)
    ent = Entry(conv)
    ent.grid(row=0, column=1)

    lb2 = Label(conv, text="Tipo do Papel")
    lb2.grid(row=1, column=0, padx=10, pady=10)
    papel = ttk.Combobox(conv, values=[
        "Ap 115","Ap 150","Ap 240","Couchê 150","Couchê 300","Triplex"])
    papel.grid(row=1, column=1)

    cor = Label(conv, text="Cores das Vias")
    cor.grid(row=3, column=0, padx=10, pady=10)
    cores = ttk.Combobox(conv, values=[
        "1/0","1/1","4/0","4/1","4/4"])
    cores.grid(row=3, column=1)

    btn = Button(conv, text="Calcular", padx=15, command=soma3)
    btn.grid(row=4, column=0)

    total = Label(conv, text="R$ 0,00", padx=10, pady=10)
    total.grid(row=4, column=1)
