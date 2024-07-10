from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# CONSTANTS
FONT_NAME = ("Courier")

# ---------------------------- PASSWORD GENERATOR ------------------------------ #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    mypassword = "".join(password_list)
    # populate our generated password
    password.insert(0, mypassword)
    pyperclip.copy(mypassword)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    with open("Password-Manager/mypass.txt", 'a') as file_txt:
        email_data = email.get()
        website_data = website.get()
        password_data = password.get()
        
        if len(password_data) == 0 or len(website_data) == 0:
                messagebox.showinfo(title ="Oops", message="Please don't leave any fields empty")
        else:
            # Message box/Popup
            confirm = messagebox.askokcancel(title=website_data, message=f"These are the details you entered for {website_data}:\n Email:{email_data}\n Password:{password_data}\n Is it okay to save? ")
            
            if confirm:
                file_txt.write(f"{email_data} | {website_data} | {password_data} \n")
                # delete populated data
                website.delete(0, END)
                password.delete(0, END)

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
website = Entry(width=20)
website.grid(column=1, row= 1)

email = Entry(width=37)
email.insert(0, "ni@gmail.com")
email.grid(column=1, row= 2, columnspan=2)

password = Entry(width=20)
password.grid(column=1, row= 3)

# Buttons
search_password = Button(text="Search")
search_password.grid(column=2, row= 3)

generate_password = Button(text="Generate Password", command=generate_pass)
generate_password.grid(column=2, row= 3)

add_btn = Button(text="Add", width=36 , command=save_pass)
add_btn.grid(column=1, row= 4, columnspan=2)

window.mainloop()