from tkinter import *
import math

window = Tk()
window.title("Miles to Kilometer Converter")




miles_input = Entry()
miles_input.grid(column=1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_table = Label(text="0")
kilometer_result_table.grid(column=1, row=1)

kilometer_table = Label(text="KM")
kilometer_table.grid(column=2, row=1)

def converter_func():
    the_miles = miles_input.get()
    result = int(the_miles) * 1.609344

    kilometer_result_table["text"] = math.ceil(result)

calculation_button = Button(text="Calculate",command=converter_func)
calculation_button.grid(column=1, row=2)







window.mainloop()