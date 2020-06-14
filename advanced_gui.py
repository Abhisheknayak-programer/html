import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter
from tkinter import messagebox as m_box

win=tk.Tk()
win.title("sradhanjali modified".upper())


# # creating notebook in your gui

nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.pack(expand=True,fill="both")
nb.add(page1,text="DREAM PAGE >>")
nb.add(page2,text="DETAILS PAGE >>")
nb.grid(row=7,column=0)

# creating label frame over win 

label_frame=ttk.LabelFrame(win,text="FILL UP YOUR DETAILS:")
label_frame.grid(row=0,column=0,padx=400)

label_frame2=ttk.LabelFrame(win,text="dream page is starting enter your dreams accordingly".upper())
label_frame2.grid(row=0,column=0)

# creating background 
win.configure(background="#7fff00")



# labels creation
name_label=ttk.Label(label_frame,text="ENTER YOUR NAME :",font=20)
name_label.grid(row=0,column=0,sticky=tk.W,padx=20,pady=20)


age_label=ttk.Label(label_frame,text="ENTER YOUR AGE :",font=20)
age_label.grid(row=1,column=0,sticky=tk.W,padx=20,pady=20)

email_label=ttk.Label(label_frame,text="ENTER YOUR EMAIL ADDRESS :",font=20)
email_label.grid(row=2,column=0,sticky=tk.W,padx=20,pady=20)

# entry boxes
name_entry_box_var=tk.StringVar()
name_entry_box=ttk.Entry(label_frame,width=30,textvariable=name_entry_box_var)
name_entry_box.grid(row=0,column=1,padx=20,pady=20)

age_entry_box_var=tk.StringVar()
age_entry_box=ttk.Entry(label_frame,width=30,textvariable=age_entry_box_var)
age_entry_box.grid(row=1,column=1,padx=20,pady=20)

email_entry_box_var=tk.StringVar()
email_entry_box=ttk.Entry(label_frame,width=30,textvariable=email_entry_box_var)
email_entry_box.grid(row=2,column=1,padx=20,pady=20)

#creating combo box

gender_label=ttk.Label(label_frame,text="select your gender".upper(),font=15)
gender_label.grid(row=3,column=0,padx=20,pady=20)
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(label_frame,width=28,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("male".upper(),"female".upper(),"other".upper())
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1,padx=2,pady=20)

# Creating radio buttons 
radio_btn_label=ttk.Label(label_frame,text="selct your type".upper(),font=15)
radio_btn_label.grid(row=4,column=0)

user_type=tk.StringVar()
radio_btn_1=ttk.Radiobutton(label_frame,text="friend".upper(),value="friend".upper(),variable=user_type)
radio_btn_1.grid(row=4,column=1,padx=20,pady=20)

radio_btn_2=ttk.Radiobutton(label_frame,text="teacher".upper().upper(),value="teacher".upper(),variable=user_type)
radio_btn_2.grid(row=4,column=2,padx=20,pady=20)

radio_btn_3=ttk.Radiobutton(label_frame,text="family members".upper().upper(),value="family members".upper(),variable=user_type)
radio_btn_3.grid(row=4,column=3,padx=20,pady=20,sticky=tk.W)



# creating check btn 
check_button_var=tk.IntVar()
check_button=ttk.Checkbutton(label_frame,text="would you agree our terms and conditions of the application".upper(),variable=check_button_var)
check_button.grid(row=5,columnspan=5,sticky=tk.W)

# submit button 

def submit():
    pass
    # m_box.showwarning("help me dude","have you checked it")
    # if True:
    #     print(" hi sir")
    
    
submit_button=ttk.Button(label_frame,text="submit".upper(),command=submit)
submit_button.grid(row=6,column=1,padx=10,pady=20)



# # creating  horixontal menu bars 


# def func():
#     print("func is called so your details is saved!")
# menubar=tk.Menu(win)
# menubar.add_command(label="save".upper(),command=func)
# menubar.add_command(label="cut".upper(),command=func)
# menubar.add_command(label="paste".upper(),command=func)
# menubar.add_command(label="quit".upper(),command=func)
# menubar.add_command(label="modify details".upper(),command=func)

# win.config(menu=menubar)







# creating dropdown menubar 


def function2():                             #creating func for the work of menus
    print("working sir!!")

main_menu=tk.Menu(win)             # declaration of a menu which hold all menus


#                              MENU 1


file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="new file".upper(),command=function2)
file_menu.add_command(label="copy file".upper(),command=function2)
file_menu.add_command(label="end file".upper(),command=function2)
file_menu.add_separator()    # for creating a separation between them 
file_menu.add_command(label="developer abhishek nayak".upper(),command=function2)


main_menu.add_cascade(label="file".upper(),menu=file_menu)


#           MENU 2


editmenu=tk.Menu(main_menu,tearoff=0)          # tearoff to remove the lines
editmenu.add_command(label="undo".upper(),command=function2)
editmenu.add_command(label="redo".upper(),command=function2)
editmenu.add_command(label="do it once".upper(),command=function2)

main_menu.add_cascade(label="edit".upper(),menu=editmenu)

win.config(menu=main_menu)                               # for ending menu bar





# dream page setups


win.mainloop()