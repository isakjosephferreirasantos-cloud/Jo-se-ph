import tkinter as tk
def somar():

    try:
        n1 =float(entry1.get())
        n2 =float(entry2.get())
        lbl_res.config(text=f"resultado:{n1+n2}!")

    except ValueError:
        lbl_res.config(text="digite valores válidos!")

app=tk.Tk()
app.title("calculadora de soma")
app.geometry("300x220")

entry1=tk.Entry(app); entry1.pack(pady=5)
entry2=tk.Entry(app); entry2.pack(pady=5)
btn=tk.Button(app,text="+",command=somar); btn.pack(pady=5)
lbl_res= tk.Label(app, text="resultado"); lbl_res.pack(pady=10)


app.mainloop()