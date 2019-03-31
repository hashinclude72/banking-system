from tkinter import *
import tkinter as tk
# import requests

HEIGHT = 700
WIDTH = 800

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

		for F in (StartPage, Home, Account):
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

		frame = Frame(self, bg='black', bd=5)
		frame.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor='n')

		user_name = Label(frame, text = 'Username :-', font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		user_name.place(relx = 0.02, rely = 0.2, relwidth = 0.3, relheight = 0.1)

		pass_word = Label(frame, text = 'Password :-', font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		pass_word.place(relx = 0.02, rely = 0.4, relwidth = 0.3, relheight = 0.1)

		username = StringVar()
		password = StringVar()

		username_entry = Entry(frame, textvariable = username)
		username_entry.place(relx = 0.35, rely = 0.2, relwidth = 0.6, relheight = 0.1)

		password_entry = Entry(frame, textvariable = password)
		password_entry.place(relx = 0.35, rely = 0.4, relwidth = 0.6, relheight = 0.1)

		login = Button(frame, text="Login", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		login.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.1)

		register = Button(frame, text="Register", font=('Sans', '15', 'bold'), bd=5, bg='#413f63', command=lambda:controller.show_frame(Account))
		register.place(relx = 0.3, rely = 0.8, relwidth = 0.4, relheight = 0.1)




class Home(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# MENU FRAME----------------------------------------------------------------------------------------------------
		frame = Frame(self, bg='black', bd=5)
		frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

		home = Button(frame, text="HOME", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda:controller.show_frame(Home))
		home.place(relx=0, relheight=1, relwidth=0.2)

		button = Button(frame, text="Accounts", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda:controller.show_frame(Account))
		button.place(relx=0.2, relheight=1, relwidth=0.2)

		home = Button(frame, text="Fund \nTransfer", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.4, relheight=1, relwidth=0.2)

		home = Button(frame, text="Services", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.6, relheight=1, relwidth=0.2)

		home = Button(frame, text="Logout", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.8, relheight=1, relwidth=0.2)
		# MENU FRAME END----------------------------------------------------------------------------------------------------


		# BODY FRAME--------------------------------------------------------------------------------------------------------
		lower_frame = Frame(self, bg='black', bd=10)
		lower_frame.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.75, anchor='n')

		account_summary = Button(lower_frame, text="Account Summary", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		account_summary.place(relx=0, rely=0, relheight=0.15, relwidth=0.5)

		fund_transfer = Button(lower_frame, text="Fund Transfer", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		fund_transfer.place(relx=0.5, rely=0, relheight=0.15, relwidth=0.5)

		mini_statement = Button(lower_frame, text="Mini Statement", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		mini_statement.place(relx=0, rely=0.15, relheight=0.15, relwidth=0.5)

		mini_pdf = Button(lower_frame, text="Download Mini\nStatement as PDF", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		mini_pdf.place(relx=0.5, rely=0.15, relheight=0.15, relwidth=0.5)
		# BODY FRAME END----------------------------------------------------------------------------------------------------


class Account(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# MENU FRAME----------------------------------------------------------------------------------------------------
		frame = Frame(self, bg='black', bd=5)
		frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

		home = Button(frame, text="HOME", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda:controller.show_frame(Home))
		home.place(relx=0, relheight=1, relwidth=0.2)

		button = Button(frame, text="Accounts", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda:controller.show_frame(Account))
		button.place(relx=0.2, relheight=1, relwidth=0.2)

		home = Button(frame, text="Fund \nTransfer", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.4, relheight=1, relwidth=0.2)

		home = Button(frame, text="Services", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.6, relheight=1, relwidth=0.2)

		home = Button(frame, text="Logout", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0.8, relheight=1, relwidth=0.2)
		# MENU FRAME END----------------------------------------------------------------------------------------------------


		# BODY FRAME--------------------------------------------------------------------------------------------------------
		lower_frame = Frame(self, bg='black', bd=10)
		lower_frame.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.75, anchor='n')

		accountno = '789456123'

		account_number = Label(lower_frame, text = 'Account Number :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		account_number.place(relx = 0.025, rely = 0, relwidth = 0.95, relheight = 0.166)

		account_name = Label(lower_frame, text = 'Account Name :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		account_name.place(relx = 0.025, rely = 0.17, relwidth = 0.95, relheight = 0.166)

		account_status = Label(lower_frame, text = 'Account Status :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		account_status.place(relx = 0.025, rely = 0.34, relwidth = 0.95, relheight = 0.166)

		customer_name = Label(lower_frame, text = 'Customer Name :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		customer_name.place(relx = 0.025, rely = 0.51, relwidth = 0.95, relheight = 0.166)

		account_open_date = Label(lower_frame, text = 'Account Open Date :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		account_open_date.place(relx = 0.025, rely = 0.68, relwidth = 0.95, relheight = 0.166)

		account_balance = Label(lower_frame, text = 'Account Balance :- ' + accountno , font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		account_balance.place(relx = 0.025, rely = 0.85, relwidth = 0.95, relheight = 0.166)
		# BODY FRAME END----------------------------------------------------------------------------------------------------



root = App()
root.geometry('700x700')
root.mainloop()
