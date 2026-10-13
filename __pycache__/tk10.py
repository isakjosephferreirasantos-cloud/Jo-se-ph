from pathlib import Path
import tkinter as tk

def mostrar_mensagem():
    label.config(text="Você clicou no botão!")


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
    font=("arial", 12, "bold"),
    command=mostrar_mensagem
)

arquivo_texto = Path(__file__).resolve().parent.parent / "arquivo_texto.txt"
with arquivo_texto.open('r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

label.pack(pady=50)
btn.pack(pady=10)

janela.mainloop()