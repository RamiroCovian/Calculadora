from tkinter import *
from funciones_calc import sumar, resta, multi, divi


ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+480+180")
ventana.iconbitmap("calc.ico")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)


label_titulo = Label(ventana, text="Calculadora", font="arial 25")

label_valor1 = Label(ventana, text="VALOR 1", font="arial 12")
label_valor2 = Label(ventana, text="VALOR 2", font="arial 12")

e_valor1 = Entry(ventana)
e_valor2 = Entry(ventana)

label_resultado = Label(ventana)
label_resultado.grid(row=7, column=0, columnspan=2)

button_suma = Button(
    ventana,
    text="Suma",
    bg="black",
    fg="white",
    font="arial 12",
    width=20,
    command=lambda: sumar(e_valor1, e_valor2, label_resultado),
)
button_resta = Button(
    ventana,
    text="Resta",
    bg="black",
    fg="white",
    font="arial 12",
    width=20,
    command=lambda: resta(e_valor1, e_valor2, label_resultado),
)
button_multi = Button(
    ventana,
    text="Multiplica",
    bg="black",
    fg="white",
    font="arial 12",
    width=20,
    command=lambda: multi(e_valor1, e_valor2, label_resultado),
)
button_div = Button(
    ventana,
    text="Divide",
    bg="black",
    fg="white",
    font="arial 12",
    width=20,
    command=lambda: divi(e_valor1, e_valor2, label_resultado),
)

label_titulo.grid(row=0, column=0, columnspan=2, pady=8)

label_valor1.grid(row=1, column=0, pady=5)
label_valor2.grid(row=2, column=0)

e_valor1.grid(row=1, column=1, padx=8)
e_valor2.grid(row=2, column=1, padx=8)

button_suma.grid(row=3, column=0, pady=5, columnspan=2)
button_resta.grid(row=4, column=0, pady=5, columnspan=2)
button_multi.grid(row=5, column=0, pady=5, columnspan=2)
button_div.grid(row=6, column=0, pady=5, columnspan=2)


ventana.mainloop()
