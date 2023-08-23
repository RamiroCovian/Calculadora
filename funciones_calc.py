# Funciones de la calculadora
from tkinter import messagebox


def sumar(e_valor1, e_valor2, label_resultado):
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()

        if valor1 == "" or valor2 == "":
            label_resultado["text"] = "Faltan valores para sumar!"
            messagebox.showwarning("Error", "Faltan valores para sumar")
        else:
            resultado = float(valor1) + float(valor2)
            label_resultado["text"] = resultado
    except:
        messagebox.showerror("Error nivel dos", "Error, valores no validos")


def resta(e_valor1, e_valor2, label_resultado):
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()

        if valor1 == "" or valor2 == "":
            label_resultado["text"] = "Faltan valores para restar!"
            messagebox.showwarning("Error", "Faltan valores para restar")
        else:
            resultado = float(valor1) - float(valor2)
            label_resultado["text"] = resultado
    except:
        messagebox.showerror("Error nivel dos", "Error, valores no validos")


def multi(e_valor1, e_valor2, label_resultado):
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()

        if valor1 == "" or valor2 == "":
            label_resultado["text"] = "Faltan valores para multiplicar!"
            messagebox.showwarning("Error", "Faltan valores para multiplicar")
        else:
            resultado = float(valor1) * float(valor2)
            label_resultado["text"] = resultado
    except:
        messagebox.showerror("Error nivel dos", "Error, valores no validos")


def divi(e_valor1, e_valor2, label_resultado):
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()

        if valor1 == "" or valor2 == "":
            label_resultado["text"] = "Faltan valores para dividir!"
            messagebox.showwarning("Error", "Faltan valores para dividir")
        else:
            resultado = float(valor1) / float(valor2)
            label_resultado["text"] = resultado
    except:
        messagebox.showerror("Error nivel dos", "Error, valores no validos")
