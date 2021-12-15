from tkinter import *
root= Tk()
root.title ("Calculadora")

#Creamos una variable global
i= 0

#Funciones. Le damos la variable global a la funcion y hacemos que i se incremente en 1. La variable global nos permite que aparezcan en el orden que queremos los numeros.
def click (valor):
    global i
    entrada.insert(i, valor)
    i+= 1

#Boton de borrar
def borrar():
    entrada.delete(0, END)
    i=0

#Funciones de las operaciones. El metodo eval nos permite ahorrar codigo, no va a ser necesario crear una funcion para cada operacion.

def operaciones():
    operacion= entrada.get()
    resultado= eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    i=0




#Entrada

entrada= Entry (root, font= ("Curier 20"))  
entrada.grid (row= 0, column= 0, columnspan=4, padx= 5, pady= 5)

#Botones

boton1= Button(root, text="1", width= 5, height=2, command=lambda:click(1))
boton2= Button(root, text="2", width= 5, height=2, command=lambda:click(2))
boton3= Button(root, text="3", width= 5, height=2, command=lambda:click(3))
boton4= Button(root, text="4", width= 5, height=2, command=lambda:click(4))
boton5= Button(root, text="5", width= 5, height=2, command=lambda:click(5))
boton6= Button(root, text="6", width= 5, height=2, command=lambda:click(6))
boton7= Button(root, text="7", width= 5, height=2, command=lambda:click(7))
boton8= Button(root, text="8", width= 5, height=2, command=lambda:click(8))
boton9= Button(root, text="9", width= 5, height=2, command=lambda:click(9))
boton0= Button(root, text="0", width= 13, height=2, command=lambda:click(0))

boton_borrar= Button(root, text="DEL", width= 5, height=2, command=lambda:borrar())
boton_parentesis1= Button(root, text="(", width= 5, height=2, command=lambda:click("("))
boton_parentesis2= Button(root, text=")", width= 5, height=2, command=lambda:click(")"))
boton_punto= Button(root, text=".", width= 5, height=2, command=lambda:click("."))

botonmult= Button(root, text="*", width= 5, height=2, command=lambda:click("*"))
botondiv= Button(root, text="/", width= 5, height=2, command=lambda:click("/"))
botonsum= Button(root, text="+", width= 5, height=2, command=lambda:click("+"))
botonrest= Button(root, text="-", width= 5, height=2, command=lambda:click("-"))
botonigual= Button(root, text="=", width= 5, height=2, command=lambda:operaciones())


#Colocar Botones
boton_borrar.grid (row=1, column= 0, padx=5, pady=5)
boton_parentesis1.grid (row=1, column= 1, padx=5, pady=5)
boton_parentesis2.grid (row=1, column= 2, padx=5, pady=5)
botondiv.grid (row=1, column= 3, padx=5, pady=5)

boton7.grid (row=2, column=0, padx=5, pady=5)
boton8.grid (row=2, column=1, padx=5, pady=5)
boton9.grid (row=2, column=2, padx=5, pady=5)
botonmult.grid (row=2, column=3, padx=5, pady=5)

boton4.grid (row=3, column=0, padx=5, pady=5)
boton5.grid (row=3, column=1, padx=5, pady=5)
boton6.grid (row=3, column=2, padx=5, pady=5)
botonsum.grid (row=3, column=3, padx=5, pady=5)

boton1.grid (row=4, column=0, padx=5, pady=5)
boton2.grid (row=4, column=1, padx=5, pady=5)
boton3.grid (row=4, column=2, padx=5, pady=5)
botonrest.grid (row=4, column=3, padx=5, pady=5)

boton0.grid (row=5, column=0, padx=5, pady=5, columnspan=2)
boton_punto.grid (row=5, column=2, padx=5, pady=5)
botonigual.grid (row=5, column=3, padx=5, pady=5)








root.mainloop()
