from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    
    email_data = email.get()
    website_data = website.get()
    password_data = password.get()
    new_data = {
        website_data :{
            "email": email_data,
            "password" : password_data
        } 
    }
    
    if len(password_data) == 0 or len(website_data) == 0:
            messagebox.showinfo(title ="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("mypass.json") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("mypass.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            # Saving updated data
            with open("mypass.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:        
            # delete populated data
            website.delete(0, END)
            password.delete(0, END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_data = website.get()
    # if i cant use if/else use try/except
    try:
        with open("mypass.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message= "No Data File Found.")
    else:
        if website_data in data:
            email = data[website_data].get("email")
            password = data[website_data].get("password")
            if email and password:
                messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showerror(title="Oops", message= "No details for the website exists.")
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_image = PhotoImage(file = "logo.png") 
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
website = Entry(width=22)
website.grid(column=1, row= 1)

email = Entry(width=41)
email.insert(0, "n@gmail.com")
email.grid(column=1, row= 2, columnspan=2)

password = Entry(width=22)
password.grid(column=1, row= 3)

# Buttons
search_password = Button(text="Search", bg="blue", width=15 ,command=find_password)
search_password.grid(column=2, row=1)

generate_password = Button(text="Generate Password", command=generate_pass)
generate_password.grid(column=2, row= 3)

add_btn = Button(text="Add", width=38 , command=save_pass)
add_btn.grid(column=1, row= 4, columnspan=2)

window.mainloop()