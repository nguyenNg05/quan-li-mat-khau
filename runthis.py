from tkinter import *
from tkinter import messagebox
f = open('packages/key.txt','r')
key = f.readlines()

access = key[0] 

class popupWindow(object):
	
	attempts = 0

	def __init__(self,master):
		top = self.top = Toplevel(master)
		top.title("Nhập mật khẩu")
		top.geometry("250x100")
		top.iconbitmap("logo/lg_128.ico")
		top.resizable(width=False,height=False)
		self.f = Frame(top)
		self.l = Label(top,text="Nhập mật khẩu",font=("Time New Roman",15))
		self.l.pack()
		self.e = Entry(top,font=("Time New Roman",15),show="•")
		self.e.pack()
		self.b = Button(top,text="Xác nhận",font=("Time New Roman",15),pady=30,command=self.cleanup)
		self.b.pack(pady=10)

	def cleanup(self):
		self.value = self.e.get()
		

		if self.value == access:
			self.top.destroy()
			root.deiconify()
		else:
			self.attempts += 1
			if self.attempts == 5:
				root.quit()
			self.e.delete(0,END)
			messagebox.showerror("Mật khẩu sai",f"Mật khẩu sai còn {5 - self.attempts} lần thử")


class change_access_window(object):
	def __init__(self,master):
		new_top =self.new_top = Toplevel(master)
	
		self.new_top.title("Đổi mật khẩu chính")
		self.new_top.iconbitmap("logo/lg_128.ico")
		self.new_top.geometry("250x250")
	
		self.new_top.resizable(width=False,height=False)
	
		self.new_top_frame = Frame(new_top)
	
		self.new_top_frame.pack()
	
		self.change_access_label = Label(self.new_top_frame,text="Nhập mật khẩu mới",font=("Time New Roman",15))
	
		self.change_access_label.pack(pady=5)
	
		self.change_access_entry = Entry(self.new_top_frame,font=("Time New Roman",12),show="•")
	
		self.change_access_entry.pack(pady=5)
	
		self.re_change_access_label = Label(self.new_top_frame,text="Nhập lại",font=("Time New Roman",15))
	
		self.re_change_access_label.pack(pady=5)
	
		self.re_change_access_entry = Entry(self.new_top_frame,font=("Time New Roman",12),show="•")
	
		self.re_change_access_entry.pack(pady=5)
	
		self.new_access_submit_button = Button(self.new_top_frame,text="Xác nhận",font=("Time New Roman",15),command=self.submit_change)

		self.new_access_submit_button.pack(pady=5)

	def submit_change(self):
		new_access = self.change_access_entry.get()
		re_new_access = self.re_change_access_entry.get()

		if new_access == re_new_access:
			f = open('packages/key.txt','w').close()
			f = open('packages/key.txt','w')
			f.write(new_access)
			messagebox.showinfo('Thành công','Đã đổi mật khẩu thành công')
			self.new_top.destroy()
		else:
			messagebox.showwarning('Lỗi','Mật khẩu không khớp')
			self.re_change_access_entry.delete(0,END)



class Add_acc(object):
	def __init__(self,master,n,e,u,p):
		self.name = n
		self.email = e
		self.username = u
		self.password = p
		self.master = root

	def save(self):
		f = open('packages/data.txt','a')
		n = self.name
		e = self.email
		u = self.username
		p = self.password

		encodeN = ""
		encodeE = ""
		encodeU = ""
		encodeP = ""

		for letter in n:
			if letter == " ":
				encodeN += " "
			else:
				encodeN += chr(ord(letter) + 5)

		for letter in e:
			if letter == " ":
				encodeE += " "
			else:
				encodeE += chr(ord(letter) + 5)

		for letter in u:
			if letter == " ":
				encodeU += " "
			else:
				encodeU += chr(ord(letter) + 5)

		
		for letter in p:
			if letter == " ":
				encodeP += " "
			else:
				encodeP += chr(ord(letter) + 5)

		f.write(f"{encodeN},{encodeE},{encodeU},{encodeP},\n")
		f.close()

class Display_acc(object):
	def __init__(self,master,n,e,u,p,i):
		self.password = p
		self.name = n
		self.email = e
		self.username = u
		self.root = master
		self.i = i

		decodeN = ""
		decodeE = ""
		decodeU = ""
		decodeP = ""

		for letter in self.name:
			if letter == " ":
				decodeN += " "
			else:
				decodeN += chr(ord(letter) - 5)

		for letter in self.email:
			if letter == " ":
				decodeE += " "
			else:
				decodeE += chr(ord(letter) - 5)
		
		for letter in self.username:
			if letter == " ":
				decodeU += " "
			else:
				decodeU += chr(ord(letter) - 5)
		
		for letter in self.password:
			if letter == " ":
				decodeP += " "
			else:
				decodeP += chr(ord(letter) - 5)


		self.label_name = Label(main_frame,text=decodeN,font=("Time New Roman",14))
		self.label_email = Label(main_frame,text=decodeE,font=("Time New Roman",14))
		self.label_username = Label(main_frame,text=decodeU,font=("Time New Roman",14))
		self.label_password = Label(main_frame,text=decodeP,font=("Time New Roman",14))
		self.delete_button = Button(main_frame,text="X",font=("Time New Roman",14),fg="red",command=self.delete)

	def display(self):
		self.label_name.grid(row=7 + self.i,)
		self.label_email.grid(row=7 + self.i,column=1)
		self.label_username.grid(row=7 + self.i,column=2)
		self.label_password.grid(row=7 + self.i,column=3,sticky=E)
		self.delete_button.grid(row=7 + self.i,column=4,sticky=E)

	def delete(self):
		position = self.i
		print(position)
		answer = messagebox.askquestion("Chắc không ?","Bạn có chắc chắn xóa không ?")

		if answer == "yes":
			f = open("package/packages/data.txt","r")
			lines = f.readlines()
			f.close()
			lines.remove(lines[position])
			f = open('packages/data.txt','w').close()
			f = open('packages/data.txt','w')
			for line in lines:
				f.write(line)

			

			self.label_name.grid_forget()
			self.label_email.grid_forget()
			self.label_username.grid_forget()
			self.label_password.grid_forget()
			self.delete_button.grid_forget()
		else:
			pass


	def __str__(self):
		decodeN = ""
		for letter in self.name:
			if letter == " ":
				decodeN += " "
			else:
				decodeN += chr(ord(letter) - 5)
		return str(decodeN)
		
			



def read_files():
	f = open('packages/data.txt','r')
	count = 0

	for line in f:
		acc_list = line.split(',')
		d_a = Display_acc(root,acc_list[0],acc_list[1],acc_list[2],acc_list[3],count)
		d_a.display()
		count += 1
	f.close()

    



def submit():
	
	n = name_entry.get()
	e = email_entry.get()
	u = username_entry.get()
	p = password_entry.get()
	add_a = Add_acc(root,n,e,u,p)
	add_a.save()
	name_entry.delete(0,END)
	email_entry.delete(0,END)
	username_entry.delete(0,END)
	password_entry.delete(0,END)
	print(n,e,u,p)
	read_files()
	messagebox.showinfo('Thành công','Đã thêm thành công 1 tài khoản\n tên: {} \n email: {} \n username: {} \n password: {}'.format(n,e,u,p))

def change_access():
	change_access_window(root)



root = Tk()
root.title("Kho lưu mật khẩu")
root.iconbitmap("logo/lg_128.ico")
root.withdraw()
popupWindow(root)



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

submit_button = Button(main_frame,text="Thêm tài khoản",font=("Time New Roman",20),command=submit)
change_password_button = Button(main_frame,text="Đổi mật khẩu chính",font=("Time New Roman",20),command=change_access)

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

submit_button.grid(row=5,columnspan=2,pady=10)
change_password_button.grid(row=5,columnspan=2,pady=10,padx=10,column=2)

name_label_2.grid(row=6)
username_label_2.grid(row=6,column=2)
email_label_2.grid(row=6,column=1,sticky=W,padx=50)
password_label_2.grid(row=6,column=3,padx=50)

read_files()
root.mainloop()