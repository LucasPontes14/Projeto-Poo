from tkinter import messagebox

def aviso(resposta, aviso_true, aviso_false):
    if resposta:
        messagebox.showinfo("Operação realizada com sucesso!", aviso_true)
    else:
        messagebox.showerror("Ops! Algo de errado aconteceu, tente novamente!", aviso_false)

