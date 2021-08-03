from tkinter import *



root = Tk()

main_frame = Frame(root)
main_frame.pack()

entity_label = Label(main_frame,text="Thêm Tài khoản",font=("Time New Roman",18))
name_label = Label(main_frame,text="Tên:",font=("Time New Roman",18))
email_label = Label(main_frame,text="Email:",font=("Time New Roman",18))
username_label = Label(main_frame,text="Username:",font=("Time New Roman",18))
password_label = Label(main_frame,text="Password:",font=("Time New Roman",18))

name_entry = Entry(main_frame,font=("Time New Roman",15),width=30)
email_entry = Entry(main_frame,font=("Time New Roman",15),width=30)
username_entry = Entry(main_frame,font=("Time New Roman",15),width=30)
password_entry = Entry(main_frame,font=("Time New Roman",15),show="•",width=30)

submit_button = Button(main_frame,text="Xác nhận",font=("Time New Roman",20))

name_label_2 = Label(main_frame,text="Tên:",font=("Time New Roman",15))
username_label_2 = Label(main_frame,text="Username:",font=("Time New Roman",15))
email_label_2 = Label(main_frame,text="Email:",font=("Time New Roman",15))
password_label_2 = Label(main_frame,text="Password:",font=("Time New Roman",15))


entity_label.grid(row=0,columnspan=4)
name_label.grid(row=1,sticky=E,padx=3)
email_label.grid(row=2,sticky=E,padx=3)
username_label.grid(row=3,sticky=E,padx=3)
password_label.grid(row=4,sticky=E,padx=3)

name_entry.grid(row=1,column=1,sticky=W,pady=3,padx=10,columnspan=4)
email_entry.grid(row=2,column=1,sticky=W,pady=3,padx=10,columnspan=4)
username_entry.grid(row=3,column=1,sticky=W,pady=3,padx=10,columnspan=4)
password_entry.grid(row=4,column=1,sticky=W,pady=3,padx=10,columnspan=4)

submit_button.grid(row=5,columnspan=4,pady=10)

name_label_2.grid(row=6)
username_label_2.grid(row=6,column=1)
email_label_2.grid(row=6,column=2,sticky=W,padx=50)
password_label_2.grid(row=6,column=3,padx=50)

root.mainloop()