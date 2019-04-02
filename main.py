from tkinter import *
import tkinter as tk
import mysql.connector

# import requests

HEIGHT = 700
WIDTH = 800
username_global = ""
text_msg = ''

account_number = ''
account_name = ''
account_status = ''
customer_name = ''
account_open_date = ''
account_balance = ''

f_name = ''
l_name = ''
account_name_file = ''
account_number_file = ''
status = ''
open_date = ''
amount_file = ''

home_customer_username = ''
home_account_number = ''
home_balance = ''

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		#Setup Menu
		# MainMenu(self)
		#Setup Frame
		global HEIGHT
		global WIDTH
		container = tk.Canvas(self)
		# container.pack()
		# container = Frame(self, height='700', width='800')
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Home, Account, Register):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()


class StartPage(Frame):


	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		base = Frame(self, bd=5)
		base.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

		frame = Frame(base, bd=5)
		frame.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor='n')

		user_name = Label(frame, text = 'Username :-', font=('Sans', '14'), bd=5)
		user_name.place(relx = 0.02, rely = 0.1, relwidth = 0.3, relheight = 0.1)

		pass_word = Label(frame, text = 'Password :-', font=('Sans', '14'), bd=5)
		pass_word.place(relx = 0.02, rely = 0.3, relwidth = 0.3, relheight = 0.1)

		# username = StringVar()
		# password = StringVar()

		username_entry = Entry(frame)
		username_entry.place(relx = 0.35, rely = 0.1, relwidth = 0.6, relheight = 0.1)

		password_entry = Entry(frame, show="*")
		password_entry.place(relx = 0.35, rely = 0.3, relwidth = 0.6, relheight = 0.1)

		# global username
		# username = self.username_entry.get()
		# print(username)
		# print('qwe')

		login = Button(frame, text="Login", font=('Sans', '12'), bd=3, command=lambda:user_login(username_entry.get(), password_entry.get(), controller))
		login.place(relx = 0.3, rely = 0.65, relwidth = 0.4, relheight = 0.1)

		global text_msg

		text_msg = Label(frame)
		text_msg.place(rely=0.5, relx=0.4)

		register = Button(frame, text="Register", font=('Sans', '12'), bd=3, command=lambda:controller.show_frame(Register))
		register.place(relx = 0.3, rely = 0.8, relwidth = 0.4, relheight = 0.1)

def user_login(username, password, controller):
	# print(username, password)
	global username_global
	username_global = username
	# username_global = self.username_entry.get()
	# print(username_global + ' gl')
	# self.username_entry.delete(0, END)
	# self.password_entry.delete(0, END)
	global text_msg
	mydb = mysql.connector.connect(host="remotemysql.com", user="HtVCfBRiAp", passwd="aahR8EPevy", database="HtVCfBRiAp")
	mycursor = mydb.cursor()
	query = "select * from login where username = '" + username + "'"	# and password = " + password + "'"
	mycursor.execute("select * from login where username = '" + username + "'")
	myresult = mycursor.fetchone()
	rows = mycursor.rowcount
	print(rows)
	if rows > 0 :
		user_pass = myresult[1]
		if user_pass == password:
			controller.show_frame(Home)
		else:
			text_msg.config(text="Invalid Password ", fg="red")
			# self.password_not_recognised()

	else:
		text_msg.config(text="User Not Found", fg="red")
		# self.user_not_found()
	mycursor.close()
	mydb.close()
	update(controller)


#-----------BOTO3--------------------------------
		# import boto3
		# s3_resource = boto3.resource('s3')
		# s3_resource.meta.client.upload_file(Filename='C:/Users/hash-include/Documents/GitHub/banking-system/index.py', Bucket='jigyasa-files', Key='index.py')
		#

#----------------BOTO-------------------------------
# 		import boto
# 		import boto.s3.connection
# 		access_key = 'AKIAJMI2PGLHYSBHUL7A'
# 		secret_key = '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'
#
# 		conn = boto.connect_s3(
# 		        aws_access_key_id = access_key,
# 		        aws_secret_access_key = secret_key,
# 		        # host = 'objects.dreamhost.com',
# 		        # #is_secure=False,               # uncomment if you are not using ssl
# 		        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
# 		        )
# #---------LISTING OWNED BUCKETS-------------------
# 		for bucket in conn.get_all_buckets():
# 			print ("%s \t %s" %(bucket.name, bucket.creation_date))
#
# # ------------LISTING A BUCKET’S CONTENT--------------
# 			for key in bucket.list():
# 				print ("%s \t %s \t %s" %(key.name, key.size, key.last_modified))



	# def password_not_recognised(self):
	#     global password_not_recog_screen
	#     password_not_recog_screen = Toplevel(root)
	#     password_not_recog_screen.title("Success")
	#     password_not_recog_screen.geometry("150x100")
	#     Label(password_not_recog_screen, text="Invalid Password ").pack()
	#     Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()
	#
	# def user_not_found(self):
	#     global user_not_found_screen
	#     user_not_found_screen = Toplevel(root)
	#     user_not_found_screen.title("Success")
	#     user_not_found_screen.geometry("150x100")
	#     Label(user_not_found_screen, text="User Not Found").pack()
	#     Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()
	#
	# def delete_password_not_recognised(self):
	#     password_not_recog_screen.destroy()
	#
	#
	# def delete_user_not_found_screen(self):
	#     user_not_found_screen.destroy()


class Home(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# MENU FRAME----------------------------------------------------------------------------------------------------
		base = Frame(self, bd=5)
		base.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

		frame = Frame(base, bd=5)
		frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

		home = Button(frame, text="Home", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(Home))
		home.place(relx=0, relheight=1, relwidth=0.2)

		button = Button(frame, text="Accounts", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(Account))
		button.place(relx=0.2, relheight=1, relwidth=0.2)

		home = Button(frame, text="Fund \nTransfer", font=('Sans', '15'), bd=5)
		home.place(relx=0.4, relheight=1, relwidth=0.2)

		home = Button(frame, text="Services", font=('Sans', '15'), bd=5)
		home.place(relx=0.6, relheight=1, relwidth=0.2)

		home = Button(frame, text="Logout", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(StartPage))
		home.place(relx=0.8, relheight=1, relwidth=0.2)
		# MENU FRAME END----------------------------------------------------------------------------------------------------


		# BODY FRAME--------------------------------------------------------------------------------------------------------
		lower_frame = Frame(base, bd=5)
		lower_frame.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.75, anchor='n')

		account_summary = Button(lower_frame, text="Account Summary", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(Account))
		account_summary.place(relx=0, rely=0, relheight=0.15, relwidth=0.5)

		fund_transfer = Button(lower_frame, text="Fund Transfer", font=('Sans', '15'), bd=5)
		fund_transfer.place(relx=0.5, rely=0, relheight=0.15, relwidth=0.5)

		mini_statement = Button(lower_frame, text="Mini Statement", font=('Sans', '15'), bd=5)
		mini_statement.place(relx=0, rely=0.15, relheight=0.15, relwidth=0.5)

		mini_pdf = Button(lower_frame, text="Download Mini\nStatement as PDF", font=('Sans', '15'), bd=5)
		mini_pdf.place(relx=0.5, rely=0.15, relheight=0.15, relwidth=0.5)

		user_name = Label(lower_frame, text = 'Hello welcome to INTRIGIN Banking.', font=('Sans', '14'), bd=5)
		user_name.place(relx = 0, rely = 0.35, relheight=0.1)

		global home_customer_username
		global home_account_number
		global home_balance

		home_customer_username = Label(lower_frame, text = 'Account Number :-', font=('Sans', '14'), bd=5)
		home_customer_username.place(relx = 0, rely = 0.45, relheight=0.1)

		home_account_number = Label(lower_frame, text = 'Account Summary :-', font=('Sans', '14'), bd=5)
		home_account_number.place(relx = 0, rely = 0.55, relheight=0.1)

		home_balance = Label(lower_frame, text = 'Account Summary :-', font=('Sans', '14'), bd=5)
		home_balance.place(relx = 0, rely = 0.65, relheight=0.1)
		# BODY FRAME END----------------------------------------------------------------------------------------------------


class Account(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# MENU FRAME----------------------------------------------------------------------------------------------------
		base = Frame(self, bd=5)
		base.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

		frame = Frame(base, bd=5)
		frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

		home = Button(frame, text="Home", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(Home))
		home.place(relx=0, relheight=1, relwidth=0.2)

		button = Button(frame, text="Accounts", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(Account))
		button.place(relx=0.2, relheight=1, relwidth=0.2)

		home = Button(frame, text="Fund \nTransfer", font=('Sans', '15'), bd=5)
		home.place(relx=0.4, relheight=1, relwidth=0.2)

		home = Button(frame, text="Services", font=('Sans', '15'), bd=5)
		home.place(relx=0.6, relheight=1, relwidth=0.2)

		home = Button(frame, text="Logout", font=('Sans', '15'), bd=5, command=lambda:controller.show_frame(StartPage))
		home.place(relx=0.8, relheight=1, relwidth=0.2)
		# MENU FRAME END----------------------------------------------------------------------------------------------------


		# BODY FRAME--------------------------------------------------------------------------------------------------------
		lower_frame = Frame(base, bd=5)
		lower_frame.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.75, anchor='n')


		global username_global
		global account_number
		global account_name
		global account_status
		global customer_name
		global account_open_date
		global account_balance

		account_number = Label(lower_frame, text = 'Account Number :- '  , font=('Sans', '14'), bd=5)
		account_number.place(relx = 0.025, rely = 0, relheight = 0.166)

		account_name = Label(lower_frame, text = 'Account Name :- '  , font=('Sans', '14'), bd=5)
		account_name.place(relx = 0.025, rely = 0.17, relheight = 0.166)

		account_status = Label(lower_frame, text = 'Account Status :- '   , font=('Sans', '14'), bd=5)
		account_status.place(relx = 0.025, rely = 0.34, relheight = 0.166)

		customer_name = Label(lower_frame, text = 'Customer Name :- '  , font=('Sans', '14'), bd=5)
		customer_name.place(relx = 0.025, rely = 0.51, relheight = 0.166)

		account_open_date = Label(lower_frame, text = 'Account Open Date :- '  , font=('Sans', '14'), bd=5)
		account_open_date.place(relx = 0.025, rely = 0.68, relheight = 0.166)

		account_balance = Label(lower_frame, text = 'Account Balance :- '  , font=('Sans', '14'), bd=5)
		account_balance.place(relx = 0.025, rely = 0.85, relheight = 0.166)
		# BODY FRAME END----------------------------------------------------------------------------------------------------

def update(controller):
	global username_global
	global account_number
	global account_name
	global account_status
	global customer_name
	global account_open_date
	global account_balance

	global home_customer_username
	global home_account_number
	global home_balance

	global f_name
	global l_name
	global account_name_file
	global account_number_file
	global status
	global open_date
	global amount_file



	account_number.config(text='Account Number :- ' + username_global)

	import xml.etree.ElementTree as ET
	path = "users/" + username_global +"/details.xml"
	tree = ET.parse(path)
	root = tree.getroot()

	user_data = []
	for elem in root:
		# for subelem in elem:
		user_data.append(elem.text)
	username_global, f_name, l_name, account_name_file, account_number_file, status, open_date = user_data
	print(user_data)

	account_number.config(text='Account Number :- ' + account_number_file)
	account_name.config(text='Account Name :- ' + account_name_file)
	account_status.config(text='Account Status :- ' + status)
	customer_name.config(text='Customer Name :- ' + f_name + " " + l_name)
	account_open_date.config(text='Account Open Date :- ' + open_date)

	path = "users/" + username_global +"/amount.xml"
	tree = ET.parse(path)
	root = tree.getroot()
	amount_file = root[0].text
	print(amount_file)
	account_balance.config(text='Account Balance :- ' + amount_file)

	home_customer_username.config(text = f_name + ' ' + l_name)
	home_account_number.config(text='Account Number :- ' + account_number_file)
	home_balance.config(text='Account Balance :- ' + amount_file)




class Register(Frame):


	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		base = Frame(self, bd=5)
		base.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

		frame = Frame(base, bd=5)
		frame.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor='n')

		user_name = Label(frame, text = 'Username :-', font=('Sans', '14'), bd=5)
		user_name.place(relx = 0.02, rely = 0, relwidth = 0.3, relheight = 0.1)

		first_name = Label(frame, text = 'Firstname :-', font=('Sans', '14'), bd=5)
		first_name.place(relx = 0.02, rely = 0.15, relwidth = 0.3, relheight = 0.1)

		last_name = Label(frame, text = 'Lastname :-', font=('Sans', '14'), bd=5)
		last_name.place(relx = 0.02, rely = 0.3, relwidth = 0.3, relheight = 0.1)

		pass_word = Label(frame, text = 'Password :-', font=('Sans', '14'), bd=5)
		pass_word.place(relx = 0.02, rely = 0.45, relwidth = 0.3, relheight = 0.1)

		# username = StringVar()
		# password = StringVar()
		# firstname = StringVar()
		# lastname = StringVar()

		self.username_entry = Entry(frame, textvariable = '')
		self.username_entry.place(relx = 0.35, rely = 0, relwidth = 0.6, relheight = 0.1)

		self.firstname_entry = Entry(frame, textvariable = '')
		self.firstname_entry.place(relx = 0.35, rely = 0.15, relwidth = 0.6, relheight = 0.1)

		self.lastname_entry = Entry(frame, textvariable = '')
		self.lastname_entry.place(relx = 0.35, rely = 0.3, relwidth = 0.6, relheight = 0.1)

		self.password_entry = Entry(frame, textvariable = '', show="*")
		self.password_entry.place(relx = 0.35, rely = 0.45, relwidth = 0.6, relheight = 0.1)


		self.text_msg = Label(frame)
		self.text_msg.place(rely=0.65, relx=0.35)

		register = Button(frame, text="Register", font=('Sans', '12'), bd=3, command=lambda:self.user_register(self.username_entry.get(), self.password_entry.get(), self.firstname_entry.get(), self.lastname_entry.get(), controller))
		register.place(relx = 0.3, rely = 0.8, relwidth = 0.4, relheight = 0.1)


	def user_register(self, username, password, firstname, lastname, controller):
		print(username, password, firstname, lastname)
		# self.username_entry.delete(0, END)
	    # self.password_entry.delete(0, END)
		if username and password and firstname and lastname:
			mydb = mysql.connector.connect(host="remotemysql.com", user="HtVCfBRiAp", passwd="aahR8EPevy", database="HtVCfBRiAp")
			mycursor = mydb.cursor()
			query = "INSERT INTO login(username, password, firstname, lastname) VALUES ('" + username + "', '" + password + "', '" + firstname + "', '" + lastname + "')"
			try:
				mycursor.execute(query)
				mydb.commit()

				import xml.etree.ElementTree as ET
				import string
				import random
				from datetime import date
				import os
				size=4
				chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
				acc_name = ''.join(random.choice(chars) for _ in range(size))
				# create the file structure
				data = ET.Element('data')
				user_name = ET.SubElement(data, 'username')
				first_name = ET.SubElement(data, 'firstname')
				last_name = ET.SubElement(data, 'lastname')
				account_name = ET.SubElement(data, 'account_name')
				account_number = ET.SubElement(data, 'account_number')
				status = ET.SubElement(data, 'status')
				open_date = ET.SubElement(data, 'open_date')
				user_name.text = username
				first_name.text = firstname
				last_name.text = lastname
				account_name.text = username + acc_name
				account_number.text = str(''.join(random.choice(string.digits) for _ in range(10)))
				status.text = 'Active'
				open_date.text = str(date.today())

				# create a new XML file with the results
				mydata = ET.tostring(data).decode()

				#-----------File handling------------------------
				path = "users/" + username
				try:
					os.mkdir(path)
				except OSError:
					print ("Creation of the directory %s failed" % path)
				else:
					print ("Successfully created the directory %s " % path)
				path = "users/" + username +"/details.xml"
				print(path)
				myfile = open(path, "w")
				myfile.write(mydata)
				#-----------------------------------------------

				data = ET.Element('data')
				amount = ET.SubElement(data, 'amount')
				amount.text = str(0.00)

				mydata = ET.tostring(data).decode()
				path = "users/" + username+"/amount.xml"
				print(path)
				myfile = open(path, "w")
				myfile.write(mydata)
				#------------------------------------------------------


				controller.show_frame(StartPage)
			except:
				self.text_msg.config(text="User Already Exists.", fg="red")
				mydb.rollback()
			mycursor.close()
			mydb.close()
		else:
			self.text_msg.config(text="All Fields are Mandatory.", fg="red")


root = App()
root.geometry('700x500')
root.title('INTRIGIN Banking')
root.resizable(0, 0)
root.mainloop()
