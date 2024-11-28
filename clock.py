from tkinter import *
from tkinter.ttk import *
from time import strftime

# Cria a janela principal
root = Tk()
root.title("Clock")

# Define a função que atualiza a hora
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Cria o rótulo que exibirá a hora
label = Label(root, font=("ds-digital", 150), background="black", foreground="red")
label.pack(anchor='center')

# Inicia a atualização da hora
time()

# Inicia o loop principal da interface gráfica
mainloop()
