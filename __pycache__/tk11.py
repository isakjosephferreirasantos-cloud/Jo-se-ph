import tkinter as tk
from tkinter import messagebox

app= tk.Tk()
app.title("mensagem de alerta")
app.geometry("250x100")

def mostra_mensagem():
    receber_mensagem = messagebox.askyesno(
        "Confirmação",
        "Você quer receber a mensagem?"
    )

    if receber_mensagem:
        messagebox.showinfo(
            "aviso",
            "operacao realizada"
        )
btn = tk.Button(app, text="clique aqui", command=mostra_mensagem)
btn.pack(pady=20)

app.mainloop()