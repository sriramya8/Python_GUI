import tkinter
from tkinter import messagebox
import pyperclip
import json
window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=tkinter.Canvas(width=200,height=200)
photo_img=tkinter.PhotoImage(file="logo.png")
img=canvas.create_image(100,100,image=photo_img)
canvas.grid(row=0,column=1)
def gen_pass():

    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.delete(0,tkinter.END)
    pass_entry.insert(0,password)
def writeusrdata():
    pass_ok=True
    dict_data={web_entry.get().title():{"email":usr_entry.get(),"password":pass_entry.get()}}
    if(len(pass_entry.get())==0 or len(web_entry.get())==0):
        pass_ok = False
        messagebox.showinfo(title="Oops! ",message="Please enter password and website details to save data")

    else:
        is_ok=messagebox.askokcancel(title="Data Entered by user",message=f"website:{web_entry.get()} \n username/email: {usr_entry.get()} \n password: {pass_entry.get()}")
        if(is_ok and pass_ok):
            try:
                with open("data.json" ,mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json",mode="w") as file:
                    json.dump(dict_data,file,indent=4)
            else:
                data.update(dict_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0,tkinter.END)
                pass_entry.delete(0,tkinter.END)
                web_entry.focus()
def search_web():
    if(len(web_entry.get())==0):
        messagebox.showinfo("Oops!","Please enter website to Search!")
    else:
        try:
            with open("data.json",mode="r") as file:
                data=json.load(file)
        except:
            messagebox.showinfo("Oops!","You haven't saved any data yet!")
        else:
            inp=(web_entry.get()).title()
            if(data.get(inp)==None):
                messagebox.showinfo("Website not found"," Please check spelling")
            else:
                messagebox.showinfo("Data",f"email: {data.get(inp).get('email')} \n password: {data.get(inp).get('password')}")
web_lab=tkinter.Label(text="Website")
web_lab.grid(row=1,column=0)
web_entry=tkinter.Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
search_button=tkinter.Button(text="Search",width=10,command=search_web)
search_button.grid(row=1,column=3)
usr_label=tkinter.Label(text="Email/Username")
usr_label.grid(row=2,column=0)
usr_entry=tkinter.Entry(width=35)
usr_entry.grid(row=2,column=1,columnspan=2)
usr_entry.insert(0,"sriramyanemani8@gmail.com")
pass_label=tkinter.Label(text="Password")
pass_label.grid(row=3,column=0)
pass_entry=tkinter.Entry(width=20)
pass_entry.grid(row=3,column=1)
gp_button=tkinter.Button(text="Generate Password",width=14,command=gen_pass)
gp_button.grid(row=3,column=2)
add_button=tkinter.Button(text="Add",width=36,command=writeusrdata)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()