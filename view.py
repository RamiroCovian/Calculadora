from tkinter import *
from funciones_calc import FunctionButton


class Ventana:
    def __init__(self, window):
        self.main = window

        self.main.title("Calculadora")
        self.main.geometry("+480+180")
        self.main.iconbitmap("calc.ico")

        self.main.columnconfigure(0, weight=1)
        self.main.columnconfigure(1, weight=1)

        self.main.rowconfigure(0, weight=1)
        self.main.rowconfigure(1, weight=1)
        self.main.rowconfigure(2, weight=1)
        self.main.rowconfigure(3, weight=1)
        self.main.rowconfigure(4, weight=1)
        self.main.rowconfigure(5, weight=1)
        self.main.rowconfigure(6, weight=1)

        label_title = Label(self.main, text="Calculadora", font="arial 25")

        label_value1 = Label(self.main, text="VALOR 1", font="arial 12")
        label_value2 = Label(self.main, text="VALOR 2", font="arial 12")

        e_value1 = Entry(self.main)
        e_value2 = Entry(self.main)

        label_result = Label(self.main)
        label_result.grid(row=7, column=0, columnspan=2)

        button_summation = Button(
            self.main,
            text="Suma",
            bg="black",
            fg="white",
            font="arial 12",
            width=20,
            command=lambda: FunctionButton.summation(
                self, e_value1, e_value2, label_result
            ),
        )
        button_subtraction = Button(
            self.main,
            text="Resta",
            bg="black",
            fg="white",
            font="arial 12",
            width=20,
            command=lambda: FunctionButton.subtraction(
                self, e_value1, e_value2, label_result
            ),
        )
        button_multiply = Button(
            self.main,
            text="Multiplica",
            bg="black",
            fg="white",
            font="arial 12",
            width=20,
            command=lambda: FunctionButton.multiply(
                self, e_value1, e_value2, label_result
            ),
        )
        button_division = Button(
            self.main,
            text="Divide",
            bg="black",
            fg="white",
            font="arial 12",
            width=20,
            command=lambda: FunctionButton.division(
                self, e_value1, e_value2, label_result
            ),
        )

        label_title.grid(row=0, column=0, columnspan=2, pady=8)

        label_value1.grid(row=1, column=0, pady=5)
        label_value2.grid(row=2, column=0)

        e_value1.grid(row=1, column=1, padx=8)
        e_value2.grid(row=2, column=1, padx=8)

        button_summation.grid(row=3, column=0, pady=5, columnspan=2)
        button_subtraction.grid(row=4, column=0, pady=5, columnspan=2)
        button_multiply.grid(row=5, column=0, pady=5, columnspan=2)
        button_division.grid(row=6, column=0, pady=5, columnspan=2)
