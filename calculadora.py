# -*- coding: utf-8 -*-

from tkinter import * # se importa la libreria TKINTER para interfas grafica
import parser # se importa para poder usarla en la funcion "calcular"para realizar las operaciones aritmeticas

root = Tk()
root.title("calculadora") # se asigna nombre a la ventana
display = Entry(root)
display.grid(row=1, columnspan=6,sticky=W+E)#barra donde se muestran los datos 

indice = 0 # variable que hace que los numeros ingresados se posicionen uno delante de otro, si no fuera asi los numeros se remplazarian y no se juntarian

#funcion para posicionar los numeros uno al lado del otro al momento de seleccionarlos.
def get_number (n):
    global indice
    display.insert(indice, n)
    indice+= 1
#_______________________________________________
#funcion para poner los operadores en la pantalla y ademas esta creado para los operadores que usan mas de 1 espacio(indice)

def get_operador(operator):
    global indice
    operator_length = len(operator)
    display.insert(indice, operator)
    indice += operator_length
#___________________________________________
#funcion para limpiar la pantalla al apretar el boton AC
def clean_display():
    display.delete(0, END)
#____________________________________________

# funcion para borrar un valor dentro de la pagina del boton (<=)
def undo ():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clean_display()
        display.insert(0,display_new_state)
    else: 
        clean_display()
        display.insert(0, 'error')
#___________________________________________________

#funcion para poder calcular las operaciones aritmeticas ne un plano generico y no solo por simbolo individual.

def calcular():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clean_display()
        display.insert(0, result)
    except expression as identifier:
        clean_display()
        display.insert(0, 'error')
#____________________________________________________      
        
#botones numericos
Button(root, text= "1",command=lambda:get_number(1)).grid(row =2, column=0,sticky=W+E)
Button(root, text= "2",command=lambda:get_number(2)).grid(row =2, column=1,sticky=W+E)
Button(root, text= "3",command=lambda:get_number(3)).grid(row =2, column=2,sticky=W+E)

Button(root, text= "4",command=lambda:get_number(4)).grid(row =3, column=0,sticky=W+E)
Button(root, text= "5",command=lambda:get_number(5)).grid(row =3, column=1,sticky=W+E)
Button(root, text= "6",command=lambda:get_number(6)).grid(row =3, column=2,sticky=W+E)

Button(root, text= "7",command=lambda:get_number(7)).grid(row =4, column=0,sticky=W+E)
Button(root, text= "8",command=lambda:get_number(8)).grid(row =4, column=1,sticky=W+E)
Button(root, text= "9",command=lambda:get_number(9)).grid(row =4, column=2,sticky=W+E)

#botones de accion
Button(root, text= "AC",command=lambda:clean_display() ).grid(row =5, column=0,sticky=W+E)#limpiar pantalla
Button(root, text= "0",command=lambda:get_number(0)).grid(row =5, column=1,sticky=W+E)
Button(root, text= "%",command = lambda:get_operador("%")).grid(row =5, column=2,sticky=W+E)

#botones operaciones aritmeticas
Button(root, text= "+",command = lambda:get_operador("+")).grid(row =2, column=3,sticky=W+E)
Button(root, text= "-",command = lambda:get_operador("-")).grid(row =3, column=3,sticky=W+E)
Button(root, text= "*",command = lambda:get_operador("*")).grid(row =4, column=3,sticky=W+E)
Button(root, text= "/",command = lambda:get_operador("/")).grid(row =5, column=3,sticky=W+E)

#botones otras acciones
Button(root, text= "<=",command = lambda:undo()).grid(row =2, column=4,sticky=W+E,columnspan = 2)
Button(root, text= "exp",command = lambda:get_operador("**")).grid(row =3, column=4,sticky=W+E)
Button(root, text= "^2",command = lambda:get_operador("**2")).grid(row =3, column=5,sticky=W+E)
Button(root, text= "(",command = lambda:get_operador("(")).grid(row =4, column=4,sticky=W+E)
Button(root, text= ")",command = lambda:get_operador(")")).grid(row =4, column=5,sticky=W+E)
Button(root, text= "=",command = lambda:calcular()).grid(row =5, column=4,sticky=W+E,columnspan = 2)

root.mainloop()