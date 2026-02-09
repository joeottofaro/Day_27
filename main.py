from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    converted_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)

# Entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

converted_label = Label(text="0")
converted_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
