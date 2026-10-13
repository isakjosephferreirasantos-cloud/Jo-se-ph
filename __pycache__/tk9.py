import tkinter as tk

def mudar_texto(event):
    label.config(text="mensagem alterada!")

janela = tk.Tk()
janela.title("evento enter")
janela.geometry("350x180")
janela.configure(bg='#0F172A')

label = tk.Label(
    janela,
    text="Pressione ENTER para mudar",
    bg='#0F172A', fg='#38BDF8',
    font=("arial", 12, "bold")
)
label.pack(pady=50)

janela.bind('return', mudar_texto)

janela.mainloop()