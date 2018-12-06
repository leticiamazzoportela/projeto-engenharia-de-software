from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from config import config
from main import execute
import _thread


info_str = """O arquivo de entrada deve ser uma planilha no formato CSV, seguindo o seguinte padrão:

|planta 1|
|planta 2|
|planta 3|
...
|planta n|
"""

def raise_frame(frame):
    frame.tkraise()

def getFile():
    name = askopenfilename(filetypes=(("CSV file", "*.csv"),))
    if (name):
        config.filename = name

def getFolder():
    name = askdirectory()
    if (name):
        config.dirname = name
        print(name)

def raise_frame(frame):
    frame.tkraise()

def start(frame):
    if (config.filename and config.dirname):
        raise_frame(frame)
        _thread.start_new_thread(execute, ())
    else:
        messagebox.showerror("Selecione todos os arquivos", "por favor, selecione um arquivo de entrada e uma pasta para salvar as planilhas")

root = Tk()

config.root = root

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

b_height = 0
b_width = 40

# F2
Label(f2, text='Isto pode demorar algumas horas').pack()
config.l_acao = Label(f2, text="acao")
config.l_plant = Label(f2, text="plant", height=0, width=40)

config.l_acao.pack()
config.l_plant.pack()

# F1
Button(f1, text="Selecionar entrada", command=lambda:getFile(), height=b_height, width=b_width).pack()
Button(f1, text="Selecionar saida", command=lambda:getFolder(), height=b_height, width=b_width).pack()
Button(f1, text="Ajuda", command=lambda:messagebox.showinfo("Title", info_str), height=b_height, width=b_width).pack()
Button(f1, text="Iniciar", command=lambda:start(f2), height=b_height, width=b_width).pack()



raise_frame(f1)
root.mainloop()