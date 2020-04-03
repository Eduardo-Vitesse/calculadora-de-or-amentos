from tkinter import *
from personal import new_window1
from blocos import new_window2
from convites import new_window3

def main():
    root = Tk()
    root.geometry("320x200+700+200")
    root.title("Página Inicial")
    root.resizable(0,0)

    btn_perss = Button(root, text="Perssonalizados", command=new_window1)
    btn_perss.grid(row=0, column=0, padx=5)

    btn_blocos = Button(root, text="Blocos", command=new_window2)
    btn_blocos.grid(row=0, column=1)

    btn_convites = Button(root, text="Convites", command=new_window3)
    btn_convites.grid(row=0, column=2, padx=5)
            

    root.mainloop()
