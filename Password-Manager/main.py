from tkinter import *

# CONSTANTS
FONT_NAME = ("Courier")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    with open("Password-Manager/mypass.txt", 'a') as file_txt:
        email_data = email.get()
        website_data = website.get()
        password_data = password.get()
        if email_data and website_data and password_data:
            credentials = f"{email_data} | {website_data} | {password_data} \n"
            
            # delete populated data
            website.delete(0, END)
            password.delete(0, END)
            
            # Append data
            file_txt.write(credentials)

        else:
            error_label = Label(text="All fields must be filled.")
            error_label.grid(row=6)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_image = PhotoImage(file = "Password-Manager/logo.png") 
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website: ",font=(FONT_NAME))
website_label.focus()
website_label.grid(column=0, row= 1)

email_label = Label(text="Email/Username:", font=(FONT_NAME))
email_label.grid(column=0, row= 2)

password_label = Label(text="Password:", font=(FONT_NAME))
password_label.grid(column=0, row= 3)

# entries
website = Entry(width=37)
website.grid(column=1, columnspan=2, row= 1)

email = Entry(width=37)
email.insert(0, "ni@gmail.com")
email.grid(column=1, row= 2, columnspan=2)

password = Entry(width=20)
password.grid(column=1, row= 3)

# Buttons
generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row= 3)

add_btn = Button(text="Add", width=36 , command=save_pass)
add_btn.grid(column=1, row= 4, columnspan=2)

window.mainloop()