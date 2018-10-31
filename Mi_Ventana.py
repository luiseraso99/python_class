#Importar librerias para GUI
from tkinter import *
import tkinter
#################################################
# crear ventana
root = tkinter.Tk ()
root.geometry("400x400") #WxH
root.title("Mi Calculadora")
root.resizable(FALSE,FALSE)
root.configure (background= "#110F0F")
#################################################

display=Entry(root,font=('arial',20,'bold'),width=25,bd=1,insertwidth=10,bg="#3498DB",justify="right").place(x=10,y=60)
boton1=Button(root,text="1",width=7,height=3).place(x=10,y=100)
                            
