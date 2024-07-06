from tkinter import *

window = Tk()
window.title("Mile to Km Converter 😀😊 ")
window.minsize(width=400, height=150)
window.configure(background="white")
window.config(padx=20, pady=40)

# Components

# widgets
miles = Entry(width=10)
miles.configure(background="white")
miles.focus()
miles.grid(column=2, row=1)

km_result_label = Label(text = 0,font=("Raleway" ,15))
km_result_label.configure(background="white")
km_result_label.grid(column=2, row=2)

def calculate():
    miles_data = float(miles.get())
    km = miles_data * 1.60934
    km_result_label.config(text=f"{km:.2f}")
    
    
# Labels - displays text/image
miles_label = Label(text="Miles", font=("Raleway" ,15))
miles_label.configure(background="white")
miles_label.grid(column=3, row=1)

# is equal t0
is_equal_label = Label(text ="is equal to", font=("Raleway" ,15))
is_equal_label.configure(background="white")
is_equal_label.grid(column=1, row=2)

# kilometre
km_label = Label(text ="Km", font=("Raleway" ,15))
km_label.configure(background="white")
km_label.grid(column=3, row=2)


# change text
# label["text"] = "New Text"

#Button
button = Button(text="Calculate", font=("Raleway" ,18), command= calculate)
button.configure(background="white", border=1)
button.grid(column=2, row=3)

# keep it open
window.mainloop()