import tkinter as tk
import os
from tkinter import ttk


win=tk.Tk()

win.configure(background="#00ff00")


labels=["what is your name :","what is your age :","gender:","country :","state:","residential address :","city:"]

for i in range(len(labels)):
    current_label="label"+str(i)
    current_label=ttk.Label(win,text=labels[i])
    current_label.grid(row=i,column=0,sticky=tk.W)
    current_label.configure(background="#ffff4d")

# entryboxes

user_info={
    "name":tk.StringVar(),
    "age":tk.StringVar(),
    "gender":tk.StringVar(),
    "country":tk.StringVar(),
    "state":tk.StringVar(),
    "residential address":tk.StringVar(),
    "city":tk.StringVar()
}
counter=0
for i in user_info:
    entry_box="entry_box"+(i)
    entry_box=tk.Entry(win,width=16,textvariable=user_info[i])
    entry_box.grid(row=counter,column=1)
    entry_box.configure(background="violet")
    counter =counter+1


# submit button creations
def action():
    name=user_info['name'].get()
    age=user_info['age'].get()
    gender=user_info['gender'].get()
    country=user_info['country'].get()
    state=user_info['state'].get()
    address=user_info['residential address'].get()
    city=user_info['city'].get()
    print(f"{name}\n{age}\n{gender}\n{country}\n{state}\n{address}\n{city}")

    # creating and storing the datas in the  file
    with open("file1.txt","w",newline="") as f:
        f.write(f"{name}\n{age}\n{gender}\n{country}\n{state}\n{address}\n{city}")

submit_button=tk.Button(win,text="submit",command=action)
submit_button.grid(column=0,row=len(labels)+1)

win.mainloop()