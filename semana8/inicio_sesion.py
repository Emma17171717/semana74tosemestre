"""
1. crear clase
2. crear constructor
3. crear atributos
4. crear metodos de encapsulamiento (set-get)
5. metodos de responsabilidades (todas las demas)
***codigo principal***
6. llamado del objeto
7. llamado de metodos
8. retorno de almacenamiento de datos

debo usar lambda si voy a usar command con dos parentesis
"""
import tkinter as Ventana 

class Inicio_sesion:
    def __init__(self, dato_color):
        self.color = dato_color
        self.formulario = Ventana.Tk()
        self.formulario.geometry("600x600")
        self.formulario.title("Inicio de sesion")
        self.label_mensaje = ""

    def ejecutar_preguntas(self):
        label_usuario = Ventana.Label(self.formulario, text="USUARIO: ")
        label_usuario.pack()
        self.entry_usuario = Ventana.Entry(self.formulario)
        self.entry_usuario.pack()

        label_contra = Ventana.Label(self.formulario, text="CONTRASEÑA: ")
        label_contra.pack()
        self.entry_contra = Ventana.Entry(self.formulario, show="*")
        self.entry_contra.pack()

        self.label_mensaje = Ventana.Label(self.formulario, text="mensaje")
        self.label_mensaje.pack()

        boton_inicio = Ventana.Button(self.formulario , text="Inicio sesion", command= lambda:self.iniciar_sesion(self.label_mensaje))
        boton_inicio.pack()
        
        label_mensaje = Ventana.Label(self.formulario)
        label_mensaje.pack()
        return self.formulario

    def iniciar_sesion(self, obj_label_mensaje):
        usuario_guardado = self.entry_usuario.get()
        contra_guardada = self.entry_contra.get()
        
        print("Usuario guardado:", usuario_guardado)
        print("Contraseña guardada:", contra_guardada)

        obj_label_mensaje.config(text="El usuario inicio sesion...")