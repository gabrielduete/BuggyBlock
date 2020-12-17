import tkinter as tk
from tkinter import *
import joguin

def Infos():
    infos = tk.Toplevel() 
    infos.geometry('300x300')
    infos.resizable(width=0, height=0)
    infos.title("BuggyBlock - Infos")
    image2 = PhotoImage(file="imagens/telaInfo.png")
    image1 = Label(infos, image=image2)
    image1.place(x=0, y=0)
    infos.mainloop()

menu = tk.Tk() 
menu.geometry('500x500')
menu.resizable(width=0, height=0)
menu.title("BuggyBlock")
menu.iconphoto(False, tk.PhotoImage(file='imagens/imgLogo.png'))

image2 = PhotoImage(file="imagens/imgTela.png")
image1 = Label(menu, image=image2)
image1.place(x=0, y=0)

button1 = tk.Button(menu, command = joguin.main, text="JOGAR!", activebackground='#A020F0', width = '10', height = '2', background='#8B008B', font='MathJax_SansSerif')
button1.place(x=130, y=380)

button2 = tk.Button(menu, command = Infos, text="Instruções", activebackground='#A020F0', width = '10', height = '2', background='#8B008B', font='MathJax_SansSerif')
button2.place(x=240, y=380)

#joguin.SomPrincipal()
menu.mainloop()