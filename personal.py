from tkinter import *
from tkinter import ttk

def new_window1():
    jan = Tk()
    jan.geometry("350x400+700+200")
    jan.title("Pérsonalizados")
    jan.resizable(0,0)

    #Função para fazer o calculo Personalizados
    def soma():
        qnt = int(ent.get())
        ppl = str(papel.get())
        med = str(medida.get())
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

        if med == "9x5cm":
            med_tot = 10
        elif med == "10x15cm":
            med_tot = 20
        elif med == "15x21cm":
            med_tot = 30
        elif med == "A4":
            med_tot = 40
        elif med == "A3":
            med_tot = 50
        elif med == "42x30cm":
            med_tot = 60
        elif med == "90x120cm":
            med_tot = 70
        else:
            med_tot = 0

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

        tot = (qnt_tot + ppl_tot + med_tot + cor_tot)
        total["text"] = f'R$ {tot},00'

    lb = Label(jan, text="Quantidade")
    lb.grid(row=0, column=0, padx=10, pady=10)
    ent = Entry(jan)
    ent.grid(row=0, column=1)

    lb2 = Label(jan, text="Tipo do Papel")
    lb2.grid(row=1, column=0, padx=10, pady=10)
    papel = ttk.Combobox(jan, values=[
        "Ap 115","Ap 150","Ap 240","Couchê 150","Couchê 300","Triplex"])
    papel.grid(row=1, column=1)

    lb3 = Label(jan, text="Tamanho")
    lb3.grid(row=2, column=0, padx=10, pady=10)
    medida = ttk.Combobox(jan, values=[
        "9x5cm","10x15cm","15x21cm","A4","A3","42x30cm","90x120cm"])
    medida.grid(row=2, column=1)

    lb4 = Label(jan, text="Cores")
    lb4.grid(row=3, column=0, padx=10, pady=10)
    cores = ttk.Combobox(jan, values=[
        "1/0","1/1","4/0","4/1","4/4"])
    cores.grid(row=3, column=1)

    btn = Button(jan, text="Calcular", padx=15, command=soma)
    btn.grid(row=4, column=0)

    total = Label(jan, text="R$ 0,00", padx=10, pady=10)
    total.grid(row=4, column=1)
