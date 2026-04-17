import tkinter as tk
app = tk.Tk()
def clicakar():
    print("Clicou no botão")
app.title("Olá Mundo")
app.geometry("300x300")
Label = tk.Label(app, text="Bem Vindo ao Tkinter")
Label.pack(pady=20)
Button = tk.Button(app, text="Clique aqui", command=clicakar)
Button.pack(pady=10)
app.mainloop()
