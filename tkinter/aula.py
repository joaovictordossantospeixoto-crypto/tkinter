import tkinter as tk
app = tk.Tk()
def clicakar():
    print("Clicou no botão")
app.title("Olá Mundo")
app.geometry("400x300")
app.configure(bg="#FF0000")
app.resizable(True,False)
Label = tk.Label(app,
                 border="5",
                 background="#745757",
                 foreground="#000000",
                 text="Bem Vindo ao Tkinter")
Label.pack(pady=20)
Button = tk.Button(app,background="#86C3FF", text="Clique aqui", command=clicakar)
Button.pack(pady=10)

app.mainloop()