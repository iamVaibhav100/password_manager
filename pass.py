from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 

FONT = ('Courier', 15, 'bold')


#---------------- SAVE PASSWORDS -----------#

def save_pass():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()

	is_ok = messagebox.askokcancel(title='confirm', message=
		f"website : {website} \nEmail : {email} \nPassword : {password}")

	if is_ok:
		with open('data.txt', "a") as pass_data:
			pass_data.write(f"{website} | {email} | {password}\n")

		website_entry.delete(0,END)
		password_entry.delete(0,END)

		

	

#---------------- UI SETUP -----------------#

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50, bg='white')

canvas = Canvas(width=400,height=400, highlightthickness=0)
logo = ImageTk.PhotoImage(Image.open('my-pass.png'))
canvas.create_image(200,200, image=logo)
canvas.grid(column=1,row=1)

# LABELS

website_label = Label(text='Website :',bg='white', font=FONT)
website_label.grid(column=0,row=2)

email_label = Label(text='Email :',bg='white', font=FONT)
email_label.grid(column=0,row=3)

password_label = Label(text='Password :',bg='white', font=FONT)
password_label.grid(column=0,row=4)

# ENTRIES

website_entry = Entry(width=61)
website_entry.grid(column=1,row=2,columnspan=2)
website_entry.focus()

email_entry = Entry(width=61)
email_entry.grid(column=1,row=3,columnspan=2)
email_entry.insert(0, 'vaibhav@gmail.com')

password_entry = Entry(width=33)
password_entry.grid(column=1,row=4)

# BUTTONS

generate_pass = Button(text='Generate Password',font=('Courier', 11, 'bold'))
generate_pass.grid(column=2,row=4)

add_button = Button(text='Add',command=save_pass, width=21,font=('Courier', 11, 'bold'))
add_button.grid(column=1,row=5)


window.mainloop()