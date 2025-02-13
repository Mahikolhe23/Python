from tkinter import *
from tkinter import messagebox
import password_generator as pw
import json

# PASSWORD GENERATOR
def generate_password():
    password = pw.get_pass()
    password_entry.insert(0,password)

# SAVE PASSWORD  
def save():
    website = website_entry.get()
    email = email_entry.get() 
    password = password_entry.get()
    new_data = {
        website:{
            'email':email,
            'password':password,
        }
    }
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title='Oops',message='Please make sure any fields is empty.')
    else:
        try:
            with open('data.json','r') as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
                data = {}
        else:
            data.update(new_data)
            with open('data.json','w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
# SEARCH PASSOWRD
def search():
        try:
            with open('data.json','r') as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}
                    messagebox.showinfo(title='ERROR', message='No Data Found')
        except FileNotFoundError:
                data = {}
                messagebox.showinfo(title='ERROR', message='No Data File Found')
        else:
            website = website_entry.get()
            try:
                email = data[website]['email']
                password = data[website]['password']
            except KeyError:
                messagebox.showinfo(title='ERROR', message=f'No Details for the {website}')
            else:
                messagebox.showinfo(title=f'{website}',message=f'Email: {email}\nPassword:{password}')
                             
# UI SETUP
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height= 200)
lock_img = PhotoImage(file='lock.png')
canvas.create_image(100,100,image = lock_img)
canvas.grid(column=1, row=0)

website_lable = Label(text='Website:')
website_lable.grid(column=0,row=1)
email_lable = Label(text='Email/Username:')
email_lable.grid(column=0,row=2)
password_lable = Label(text='Password:')
password_lable.grid(column=0,row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'youremail@email.com')
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text='Generate Password',command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text='Add',width=35, command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button = Button(text='Search',command=search)
search_button.grid(row=1,column=2)

window.mainloop()
