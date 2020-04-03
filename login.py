from tkinter import *
from datetime import datetime
#import time
from index import main

root = Tk()
root.geometry("340x200+400+200")
root.title("Login")
root.resizable(width=False, height=False)

def logar():
    nome = str(user.get())
    psw = str(senha.get())
    if nome != 'Admin' or psw != '123456':
        msg2['text'] = "USUÁRIO OU SENHA INCORRETO..."
        msg['text'] = ""
    else:
        root.destroy()
        main()

img = PhotoImage(file="assets/icon.png")
Label(root, image=img).place(x=0, y=30)

Label(root, text="Usuário").place(x=120, y=10)
user = Entry(root)
user.place(x=120, y=30)

Label(root, text="Senha").place(x=120, y=70)
senha = Entry(root, show="*")
senha.place(x=120, y=90)

Button(root, text="Entrar", command=logar).place(x=240, y=130)

data = datetime.now()
today = data.strftime("%d/%m/%Y")
Label(root, text=today).place(x=120, y=130)

msg = Label(root, text="DIGITE O USUÁRIO E SENHA!", foreground='blue')
msg.place(x=40, y=170)

msg2 = Label(root, text="", foreground='red')
msg2.place(x=40, y=170)


root.mainloop()