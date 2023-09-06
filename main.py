from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    pw = ''.join(password_list)
    pw_input.delete(0, END)
    pw_input.insert(0, pw)
    pyperclip.copy(pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    username = username_input.get()
    password = pw_input.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # Check for empty fields
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showwarning(title="Empty fields!", message="Fields cannot be empty!")
    else:
        # Ask user to confirm
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Username: {username} \n"
                                                      f"Passsword: {password} \n"
                                                      f"Ready to save?")

        # Save data
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:

                    # Read from json file
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # Write to json file
                    json.dump(new_data, data_file, indent=4)

            else:
                # Update json data (within program, not on file)
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Write to json file
                    json.dump(data, data_file, indent=4)

            finally:
                website_input.delete(0, END)
                pw_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)


# Website Entry
website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

# Username Entry
username_input = Entry()
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(END, "contact@chamathcodes.com")

# PW Entry
pw_input = Entry()
pw_input.grid(column=1, row=3, sticky="EW")

# PW Generator Button
pw_generate = Button(text="Generate Password", bg="white", command=generate_pw)
pw_generate.grid(column=2, row=3, sticky="EW")

# Add Button
add_btn = Button(text="Add", bg="white", command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
