# Funciones de la calculadora
from tkinter import messagebox


class FunctionButton:
    def __init__(self):
        pass

    def summation(self, e_value1, e_value2, label_result):
        try:
            value1 = e_value1.get()
            value2 = e_value2.get()

            if value1 == "" or value2 == "":
                label_result["text"] = "Faltan valores para sumar!"
                messagebox.showwarning("Error", "Faltan valores para sumar")
            else:
                result = float(value1) + float(value2)
                label_result["text"] = result
        except:
            messagebox.showerror("Error nivel dos", "Error, valores no validos")

    def subtraction(self, e_value1, e_value2, label_result):
        try:
            value1 = e_value1.get()
            value2 = e_value2.get()

            if value1 == "" or value2 == "":
                label_result["text"] = "Faltan valores para restar!"
                messagebox.showwarning("Error", "Faltan valores para restar")
            else:
                result = float(value1) - float(value2)
                label_result["text"] = result
        except:
            messagebox.showerror("Error nivel dos", "Error, valores no validos")

    def multiply(self, e_value1, e_value2, label_result):
        try:
            value1 = e_value1.get()
            value2 = e_value2.get()

            if value1 == "" or value2 == "":
                label_result["text"] = "Faltan valores para multiplicar!"
                messagebox.showwarning("Error", "Faltan valores para multiplicar")
            else:
                result = float(value1) * float(value2)
                label_result["text"] = result
        except:
            messagebox.showerror("Error nivel dos", "Error, valores no validos")

    def division(self, e_value1, e_value2, label_result):
        try:
            value1 = e_value1.get()
            value2 = e_value2.get()

            if value1 == "" or value2 == "":
                label_result["text"] = "Faltan valores para dividir!"
                messagebox.showwarning("Error", "Faltan valores para dividir")
            else:
                result = float(value1) / float(value2)
                label_result["text"] = result
        except:
            messagebox.showerror("Error nivel dos", "Error, valores no validos")
