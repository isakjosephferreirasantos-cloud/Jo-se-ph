import tkinter as tk


def main():
    janela = tk.Tk()
    janela.title("Minha Aplicação")
    janela.geometry("400x300")
    janela.configure(bg="black")

    label = tk.Label(
        janela,
        text="Olá, mundo!",
        fg="blue",
        bg="black",
        font=("Arial", 16, "bold"),
    )
    label.pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    main()
