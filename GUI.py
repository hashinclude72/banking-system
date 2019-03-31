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

		for F in (StartPage, PageOne):
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

		password = Label(frame, text = 'Password :-', font=('Sans', '14', 'bold'), bd=10, bg='#413f63')
		password.place(relx = 0.02, rely = 0.4, relwidth = 0.3, relheight = 0.1)

		username = StringVar()
		password = StringVar()

		username_entry = Entry(frame, textvariable = username)
		username_entry.place(relx = 0.35, rely = 0.2, relwidth = 0.6, relheight = 0.1)

		password_entry = Entry(frame, textvariable = password)
		password_entry.place(relx = 0.35, rely = 0.4, relwidth = 0.6, relheight = 0.1)

		login = Button(frame, text="Login", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		login.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.1)

		register = Button(frame, text="Register", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
		register.place(relx = 0.3, rely = 0.8, relwidth = 0.4, relheight = 0.1)




class PageOne(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# MENU FRAME----------------------------------------------------------------------------------------------------
		frame = Frame(self, bg='black', bd=5)
		frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

		home = Button(frame, text="HOME", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
		home.place(relx=0, relheight=1, relwidth=0.2)

		button = Button(frame, text="Accounts", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda: get_weather(entry.get()))
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



root = App()
root.geometry('700x700')
root.mainloop()
