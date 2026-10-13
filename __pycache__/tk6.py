import tkinter as tk

janela = tk.Tk()
janela.title("minha primeira tela")
janela.geometry("300x200")
janela.configure(bg='#0F172A')

label = tk.Label(
    janela,
    text="Olá, Mundo!",
    bg="#F6F6FC",
    fg='#000000',
    font=("arial", 14, "bold")
)
btn = tk.Button(
    janela,
    text="clique aqui!",
    bg="#0C0CF3",
    fg='#000000',
    font=("arial", 12, "bold")
)
label.pack(pady=50)
btn.pack(pady=10)

janela.mainloop()