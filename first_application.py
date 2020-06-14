import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter

win=tk.Tk()

##       background colour
win.configure(background="#00ff00")

##app title

win.title("sradhanjali".upper())

# create labels
name_label=ttk.Label(win,text="ENTER YOUR NAME :")
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="ENTER YOUR AGE:")
age_label.grid(row=1,column=0,sticky=tk.W)
age_label.configure(foreground="Red")
age_label.configure(background="#d9b3ff")

email_label=ttk.Label(win,text="ENTER YOUR EMAIL ADDRESS:")
email_label.grid(row=2,column=0,sticky=tk.W)
email_label.configure(foreground="Red")
email_label.configure(background="#99e6ff")

gender_label=ttk.Label(win,text="SELECT YOUR GENDER:")
gender_label.grid(row=3,column=0,sticky=tk.W)
gender_label.configure(foreground="Red")
gender_label.configure(background="#ffff4d")

user_type_label=ttk.Label(win,text="SELECT TYPE:")
user_type_label.grid(row=4,column=0,sticky=tk.W)
user_type_label.configure(foreground="Red")
user_type_label.configure(background="#ffccdd")

# creating entryboxes
name_var=tk.StringVar()
name_entry_box=ttk.Entry(win,width=15,textvariable=name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

age_var=tk.StringVar()
age_entry_box=ttk.Entry(win,width=15,textvariable=age_var)
age_entry_box.grid(row=1,column=1)


email_var=tk.StringVar()
email_entry_box=ttk.Entry(win,width=15,textvariable=email_var)
email_entry_box.grid(row=2,column=1)



# create combo_box
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=12,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("male","female","other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)



# creating radio_buttons
usertype=tk.StringVar()

radio_button_1=ttk.Radiobutton(win,text="student",value="student",variable=usertype)
radio_button_1.grid(row=4,column=1)

radio_button_2=ttk.Radiobutton(win,text="teacher",value="teacher",variable=usertype)
radio_button_2.grid(row=4,column=2)


radio_button_3=ttk.Radiobutton(win,text="parent",value="parent",variable=usertype)
radio_button_3.grid(row=4,column=3)


radio_button_4=ttk.Radiobutton(win,text="higher authority",value="higher authority",variable=usertype)
radio_button_4.grid(row=4,column=4)


# creating check button
check_button_var=tk.IntVar()
check_button=ttk.Checkbutton(win,text="would you agree our terms and conditions of the application".upper(),variable=check_button_var)
check_button.grid(row=5,columnspan=5,sticky=tk.W)


# # # create submit button and also writing code to simple txt file


# def action():
#     user_name=name_var.get()
#     user_age=age_var.get()
#     user_email=email_var.get()
#     print(f"{user_name} is now {user_age} old. and mail id is {user_email}")
#     user_gender=gender_var.get()
#     user_type=usertype.get()
#     if check_button_var.get() == 0:
#         agree="NO"
#     else:
#         agree="YES"
#     print(f" {user_type} is {user_gender} and entered  {agree} to our agree satement")

#     with open("file.txt","a") as f:
#         f.write(f"hi {user_name} your email:-{user_email} your age:-{user_age} and your gender is {user_gender} and of type {user_type} and has entered  {agree} to our provided statement\n")

#     name_entry_box.delete(0,tk.END)
#     age_entry_box.delete(0,tk.END)
#     email_entry_box.delete(0,tk.END)

#     submit_button.configure(foreground="Red")


###creating a function so that it can be readable in the csv file foramt 

def action():
    user_name=name_var.get()
    user_age=age_var.get()
    user_email=email_var.get()
    user_gender=gender_var.get()
    user_type=usertype.get()
    if check_button_var.get() == 0:
        agree="NO"
    else:
        agree="YES"

    # creating csv files

    with open("file.csv","a",newline="") as f:
        dict_writer=DictWriter(f,fieldnames=["user name","user age","user email","user gender","user type","agree"])
        if os.stat("file.csv").st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            "user name":user_name,
            "user age":user_age,
            "user email":user_email,
            "user gender":user_gender,
            "user type":user_type,
            "agree":agree
            })
    name_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
    submit_button.configure(foreground="Red")

submit_button=tk.Button(win,text="submit",command=action)
submit_button.grid(row=6,column=2)

win.mainloop()


