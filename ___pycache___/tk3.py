import tkinter as tk

def mostrar_tela3():
    frame_tela2.pack_forget()
    frame_tela1.pack_forget()
    frame_tela3.pack(fill="both",expand=True)
    
def mostrar_tela2():
    frame_tela1.pack_forget()
    frame_tela3.pack_forget()
    frame_tela2.pack(fill="both",expand=True)

def mostrar_tela1():
    frame_tela2.pack_forget()
    frame_tela3.pack_forget()
    frame_tela1.pack(fill="both", expand=True)

app = tk.Tk(); app.title("aplicacao multi-telas"); app.geometry("300x200")

frame_tela1 = tk.Frame(app)
tk.Label(frame_tela1,text="tela_1", font=("arial", 14)).pack(pady=20)
tk.Button(frame_tela1,text="ir para tela_2", command=mostrar_tela2).pack(pady=10)

frame_tela2 = tk.Frame(app)
tk.Label(frame_tela2,text="tela_2", font=("arial", 14)).pack(pady=20)
tk.Button(frame_tela2,text="ir para tela_3", command=mostrar_tela3).pack(pady=10)

frame_tela3 = tk.Frame(app)
tk.Label(frame_tela3,text="tela_3", font=("arial", 14)).pack(pady=20)
tk.Button(frame_tela3,text="ir para tela_1", command=mostrar_tela1).pack(pady=10)

frame_tela1.pack(fill="both", expand=True); app.mainloop()
