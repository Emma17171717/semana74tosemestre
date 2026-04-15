import tkinter as Ventana 
from tkinter import ttk # es pal combobox

class Formulario:
    def __init__(self):
        self.formulario = None
        self.entry_nombre = None
        self.entry_pass = None
        self.combo_doc = None

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk() 
        self.formulario.title("Registro de usuario")
        self.formulario.geometry("500x700")
        self.formulario.config(bg="beige", cursor="hand2") 
        return self.formulario 
    
    def iniciar_preguntas(self):
        Ventana.Label(self.formulario, text="DATOS DE ACCESO", bg="yellow", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

        Ventana.Label(self.formulario, text="Digite el nombre del cliente:", bg="yellow", fg="black").pack()
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.config(bg="light yellow")
        self.entry_nombre.pack(pady=20)

        Ventana.Label(self.formulario, text="Digite el apellido:", bg="yellow", fg="black").pack()
        self.entry_apellido = Ventana.Entry(self.formulario)
        self.entry_apellido.config(bg="light yellow")
        self.entry_apellido.pack(pady=20)

        Ventana.Label(self.formulario, text="Digite su contraseña:", bg="yellow", fg="black").pack()
        self.entry_pass = Ventana.Entry(self.formulario, show="*")
        self.entry_pass.config(bg="light yellow")
        self.entry_pass.pack(pady=20)

        Ventana.Label(self.formulario, text="Tipo de documento:", bg="yellow", fg="black").pack()
        self.combo_doc = ttk.Combobox(self.formulario, values=["Cédula", "Tarjeta de Identidad", "Pasaporte"])
        self.combo_doc.pack(pady=20)

        Ventana.Label(self.formulario, text="Digite su cédula:", bg="yellow", fg="black").pack()
        self.entry_cedula = Ventana.Entry(self.formulario)
        self.entry_cedula.config(bg="light yellow")
        self.entry_cedula.pack(pady=20)

        boton_enviar = Ventana.Button(self.formulario, text="Enviar Registro", command=self.hacer_clic)
        boton_enviar.configure(bg="light yellow")
        boton_enviar.pack(pady=30)

    def hacer_clic(self):
        self.formulario.destroy()

        self.formulario2 = Ventana.Tk()
        self.formulario2.title("Datos Personales")
        self.formulario2.geometry("500x700")
        self.formulario2.config(bg="beige")

        Ventana.Label(self.formulario2, text="Genero:", bg="yellow").pack()

        self.genero = Ventana.StringVar() #el stringvar sirve con radiobuttom, es lo mismo a decir self.genero = "", t guarda
        radio1 = Ventana.Radiobutton(self.formulario2, text="Masculino", variable=self.genero, value="Masculino", bg="beige")
        radio1.pack()
        radio2 = Ventana.Radiobutton(self.formulario2, text="Femenino", variable=self.genero, value="Femenino", bg="beige")
        radio2.pack()
        radio3 = Ventana.Radiobutton(self.formulario2, text="Otro", variable=self.genero, value="Otro", bg="beige")
        radio3.pack()

        Ventana.Label(self.formulario2, text="Fecha de nacimiento:", bg="yellow").pack()
        self.entry_fecha = Ventana.Entry(self.formulario2)
        self.entry_fecha.pack(pady=20)

        boton_final = Ventana.Button(self.formulario2, text="Hecho", command=self.finalizar)
        boton_final.pack(pady=30)

        self.formulario2.mainloop()

    def finalizar(self):
        print("La sesion ha sido guardada con exito")
        self.formulario2.destroy()