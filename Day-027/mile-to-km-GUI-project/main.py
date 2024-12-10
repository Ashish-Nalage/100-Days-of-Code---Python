from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(column=1,row=0)


def calculate():
    miles = entry.get()
    result = round(float(miles) * 1.60934, 2)
    km_result_lable.config(text=result)


# Labels
is_equal_lable = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_lable.grid(column=0, row=1)
is_equal_lable.config(padx=5, pady=5)

miles_lable = Label(text="Miles", font=("Arial", 10, "normal"))
miles_lable .grid(column=2, row=0)
miles_lable.config(padx=5,pady=5)

km_result_lable = Label(text="0", font=("Arial", 10, "normal"))
km_result_lable.grid(column=1, row=1)
km_result_lable.config(padx=5, pady=5)

km_lable = Label(text="Km", font=("Arial", 10, "normal"))
km_lable.grid(column=2, row=1)
km_lable.config(padx=5, pady=5)

# Button
button = Button(text="Calculate",font=("Arial", 10, "normal"), command=calculate)
button.grid(column=1, row=2)




window.mainloop()