from Roman2Integer import Roman2Integer
from tkinter import *

window = Tk()
window.title("Roman Numeral Converter")
window.geometry("500x700")
window.resizable(width=False, height=False)
FONT1 = ("Verdena", 16, "bold")


#title label
spacer0 = Label(window, text="")
spacer0.pack()
title_label = Label(text="Roman Numeral Converter", font=("Verdena", 28, "bold"))
title_label.config(pady=5, padx=5, bg="red", fg="white")
title_label.pack()

#space between label and user input33333
spacer1 = Label(window, text="")
spacer1.pack()
spacer2 = Label(window, text="")
spacer2.pack()
spacer3 = Label(window, text="")
spacer3.pack()

#user input and its title
explanation_label = Label(text="Enter Roman Numeral")
explanation_label.config(padx=5, pady=5, font=("Verdena", 18, "bold"))
explanation_label.pack()
user_entry = Entry()
user_entry.config(width=30, justify="center", font=("Verdena", 18, "bold"))
user_entry.pack()


#buttons
def result():
    instance_object = Roman2Integer(r=user_entry.get().upper())
    user_entry.delete(0, END)
    user_entry.insert(0, instance_object.roman_to_integer())


convert_button = Button(text="CONVERT", font=FONT1, command=result, bg="white", fg="red")
convert_button.pack(padx=20, pady=20)


def clear():
    explanation_label.config(text="Enter Roman Numeral")
    user_entry.delete(0, END)



clear_button = Button(text="CLEAR", font=FONT1, command=clear, bg="white", fg="green")
clear_button.pack()


info_label = Label(text="-----------------------------------------------------------\n"
                        "COMMON ROMAN NUMERALS\n"
                        "-----------------------------------------------------------"
                        "\nI\t   1"
                        "\nV\t   5"
                        "\nX\t  10"
                        "\nL\t  50"
                        "\nC\t 100"
                        "\nD\t 500"
                        "\nM\t1000", font=FONT1, bg="light blue")
info_label.pack(pady=40)



window.mainloop()