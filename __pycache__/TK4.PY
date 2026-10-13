import tkinter as tk
from pathlib import Path
from PIL import ImageTk, Image

app = tk.Tk()
app.title("exibindo imagem")
app.geometry("400x400")

img_pil = Image.open(Path(__file__).with_name("logo.jpg"))
img_pil = img_pil.resize((150, 150))

icone_tk = ImageTk.PhotoImage(img_pil)

app.mainloop()