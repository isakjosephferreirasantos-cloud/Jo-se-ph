import tkinter as tk

FUNDO = "#0F172A"
TEXTO = "#38BDF8"


def abrir_tela(titulo, mensagem, cor_botao):
    tela = tk.Toplevel(janela)
    tela.title(titulo)
    tela.geometry("300x180")
    tela.configure(bg=FUNDO)

    tk.Label(
        tela,
        text=mensagem,
        bg=FUNDO,
        fg=TEXTO,
        font=("Arial", 14, "bold"),
    ).pack(pady=30)

    tk.Button(
        tela,
        text="Fechar",
        command=tela.destroy,
        bg=cor_botao,
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=16,
        pady=6,
    ).pack()


janela = tk.Tk()
janela.title("Telas coloridas")
janela.geometry("300x220")
janela.configure(bg=FUNDO)

tk.Label(
    janela,
    text="Escolha uma tela",
    bg=FUNDO,
    fg=TEXTO,
    font=("Arial", 14, "bold"),
).pack(pady=(28, 18))

tk.Button(
    janela,
    text="Abrir tela roxa",
    command=lambda: abrir_tela("Tela roxa", "Esta é a tela roxa!", "#8B5CF6"),
    bg="#8B5CF6",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    width=18,
    pady=6,
).pack(pady=6)

tk.Button(
    janela,
    text="Abrir tela azul",
    command=lambda: abrir_tela("Tela azul", "Esta é a tela azul!", "#0284C7"),
    bg="#0284C7",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    width=18,
    pady=6,
).pack(pady=6)

janela.mainloop()