from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    random_letter = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    random_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    random_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = random_letter + random_number + random_symbol

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    password_entry.insert(END, password)
    print(f"Your password is {password}")
    # raise TypeError("me run hone hi ni dunga ")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    if '@' and '.com' not in email_data:
        messagebox.showerror(title="Error", message="Enter Correct Email")
        return
    password_data = password_entry.get()
    if website_data and email_data and password_data:
        answer = messagebox.askokcancel(title=f"{website_data}", message=f"These are the details.\nEmail: {email_data}\n"
                                                                         f"Password: {password_data}\nIs it okay to save?")
        if answer:
            new_data = {website_data:
                {
                    "email": email_data,
                    "password": password_data
                }
            }
            try:
                with open("data.json", 'r') as file:
                    # reading data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # updating the data
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
        else:
            password_entry.focus()
    else:
        print("Do not leave empty field Bitch.")
        messagebox.showerror(title="Error", message="You left one of the fields empty")


# -----------------search btn functionality---------------------------#
def search_data():
    website_data = website_entry.get().lower()
    if website_data:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                if website_data in data:
                    email = data[website_data]["email"]
                    password = data[website_data]["password"]
                    messagebox.showinfo(title=f"{website_data}", message=f"Email:{email}\n Password: {password}")
                else:
                    messagebox.showinfo(title="Text Message", message="The website you entered is not present.")
        except FileNotFoundError:
            messagebox.showinfo(title="Important", message="Make a file to search for it bro.")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200)
canvas.grid(column=1, row=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=33)
email_entry = Entry(width=52)
password_entry = Entry(width=33, show="*")
website_entry.focus()
# You can enter a default string by using argument string = "Your email address"
email_entry.insert(END, string="")
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
add_btn = Button(text="Add", width=44, command=add_data)
generate_btn = Button(text="Generate Password", command=random_pass_generator)
search_btn = Button(text="Search", width=13, command=search_data)
add_btn.grid(row=4, column=1, columnspan=2)
generate_btn.grid(row=3, column=2)
search_btn.grid(row=1, column=2)


window.mainloop()