import tkinter as tk

import requests

HEIGHT = 700
WIDTH = 800

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)


# MENU FRAME----------------------------------------------------------------------------------------------------
frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.15, anchor='n')

home = tk.Button(frame, text="HOME", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
home.place(relx=0, relheight=1, relwidth=0.2)

button = tk.Button(frame, text="Accounts", font=('Sans', '15', 'bold'), bd=10, bg='#413f63', command=lambda: get_weather(entry.get()))
button.place(relx=0.2, relheight=1, relwidth=0.2)

home = tk.Button(frame, text="Fund \nTransfer", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
home.place(relx=0.4, relheight=1, relwidth=0.2)

home = tk.Button(frame, text="Services", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
home.place(relx=0.6, relheight=1, relwidth=0.2)

home = tk.Button(frame, text="Logout", font=('Sans', '15', 'bold'), bd=10, bg='#413f63')
home.place(relx=0.8, relheight=1, relwidth=0.2)
# MENU FRAME END----------------------------------------------------------------------------------------------------


# BODY FRAME--------------------------------------------------------------------------------------------------------
lower_frame = tk.Frame(root, bg='black', bd=10)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.75, anchor='n')

account_summary = tk.Button(lower_frame, text="Account Summary", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
account_summary.place(relx=0, rely=0, relheight=0.15, relwidth=0.5)

fund_transfer = tk.Button(lower_frame, text="Fund Transfer", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
fund_transfer.place(relx=0.5, rely=0, relheight=0.15, relwidth=0.5)

mini_statement = tk.Button(lower_frame, text="Mini Statement", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
mini_statement.place(relx=0, rely=0.15, relheight=0.15, relwidth=0.5)

mini_pdf = tk.Button(lower_frame, text="Download Mini\nStatement as PDF", font=('Sans', '15', 'bold'), bd=5, bg='#413f63')
mini_pdf.place(relx=0.5, rely=0.15, relheight=0.15, relwidth=0.5)

# label = tk.Label(lower_frame)
# label.place(relwidth=1, relheight=1)
# BODY FRAME END----------------------------------------------------------------------------------------------------












root.mainloop()
