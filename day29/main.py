from tkinter import *
from tkinter import messagebox
import password_generator as pw
import pyperclip

# PASSWORD GENERATOR
def generate_password():
    password = pw.get_pass()
    password_entry.insert(0,password)
    pyperclip.copy(password)

# SAVE PASSWORD  
def save():
    website = website_enrty.get()
    emaail = email_entry.get() 
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title='Oops',message='Please make sure any fields is empty.')
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered:\nEmail:{emaail}'
                                                        f'\nPassword: {password} \n Is it ok to save?')
        if is_ok:
            with open('data.txt','a') as data_file:
                data_file.write(f'{website} | {emaail} | {password}\n')
                website_enrty.delete(0, END)
                password_entry.delete(0, END)
    
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
website_enrty = Entry(width=35)
website_enrty.grid(row=1,column=1,columnspan=2)
website_enrty.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'youremail@email.com')
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text='Generate Password',command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text='Add',width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
