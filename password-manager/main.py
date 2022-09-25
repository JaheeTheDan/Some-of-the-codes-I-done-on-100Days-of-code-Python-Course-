'''A password manager, which save login info for each websites added,
and aslo generate a  random password when needed.
And can receive the login info from a json file'''
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button , END
from tkinter import messagebox
import random
import json
import pyperclip

#Default email that is shown at start up of program
DEFAULT_EMAIL = 'rememberme@password.com'

def password_generator():
    '''Generate a new password with random characters'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    password += [random.choice(letters) for _ in range(random.randint(6, 10))]
    password += [random.choice(numbers) for _ in range(random.randint(4, 8))]
    password += [random.choice(symbols) for _ in range(random.randint(2, 6))]

    random.shuffle(password)

    password_entry.delete(0, END)
    password_entry.insert(0,''.join(password))
    pyperclip.copy(''.join(password))


def save():
    '''Save login info to data.json'''
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
            'email': email,
            'password': password
        }

    }
    #Check if there any empty field and tell user if there any
    info_len =(len(website),len(email),len(password))
    if info_len.count(0)>=2:
        messagebox.showwarning(title='Invalid Info', message='There are emtpy fields')
    elif info_len.count(0)>=1:
        messagebox.showwarning(title='Invalid Info', message='There is a emtpy field')
    else:
        to_save = messagebox.askokcancel(title=website,
                                        message=f'This are the details enterd for {website}'
                                                f'\nEmail: {email}\nPassword: {password}'
                                                f'\nIs it okay to save?')
        #Message box with the info shown ask the user to confirm.
        if to_save:
            try: #Check if data.json exist and if not, one is created
                with open('data.json','r',encoding='utf-8') as data_file:
                    old_data = json.load(data_file)
                    old_data.update(new_data)

            except FileNotFoundError:
                with open('data.json', 'w', encoding='utf-8') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                with open('data.json', 'w', encoding='utf-8') as data_file:
                    json.dump(old_data, data_file, indent=4)

            #Reset the entry boxes with their default values
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            email_entry.insert(0, DEFAULT_EMAIL)
            password_entry.delete(0,END)

def search():
    '''Search in data.json for info that go with the website.
    And info is not found, an error is shown telling the user info not found'''
    website = website_entry.get().strip()

    # Check if the data file exist and if not, an error is shown
    try:
        with open('data.json', 'r', encoding='utf-8') as data_file:
            data_file = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Not Fonund', message='Data file not found')
    else:
        if website in data_file.keys():
            email = data_file[website]['email']
            password = data_file[website]['password']
            messagebox.showinfo(title=website, message=f'Here is the login info'
                                                    f'\nEmail/Username: {email}'
                                                    f'\nPassword: {password}')
        else:
            messagebox.showerror(title='Not Fonund',
                                message=f'Info for website \'{website}\' is not found.')

#Window
window = Tk()
window.title ('Password Manager')
window.configure(padx=30, pady=30)

canvas = Canvas(width=180, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(90, 100, image=image)
canvas.grid(column=1, row=0)

#label
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

#entry
website_entry = Entry(width=29)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=47)
email_entry.insert(0, DEFAULT_EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)

#button
search_button = Button(text='Search',command=search, relief='flat', width=14)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password',command=password_generator, relief='flat')
generate_button.grid(column=2, row=3 )

add_button = Button(text='Add',command=save, width=40)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
