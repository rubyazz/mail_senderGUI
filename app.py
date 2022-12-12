import tkinter
import customtkinter

from tkinter import *
from customtkinter import *

import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x550")
app.title("Spam sender")



app.logo_label = customtkinter.CTkLabel(master=app, text="Welcome to Spam sender", font=customtkinter.CTkFont(size=20, weight="bold"))
app.logo_label.pack()


def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


app.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=app, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
app.appearance_mode_optionemenu.pack()


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)




entry_1 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="login")
entry_1.pack(pady=20, padx=30)


entry_2 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="password")
entry_2.pack()


entry_3 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="URL")
entry_3.pack(pady=20, padx=30)



entry_4 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="For Whom")
entry_4.pack()


entry_5 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="Topic")
entry_5.pack(pady=20, padx=30)



text_1 = customtkinter.CTkEntry(master=frame_1,placeholder_text="message", width=200, height=70)
text_1.pack(pady=10, padx=10)



entry_6 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="amount of msg")
entry_6.pack(pady=20, padx=30)



def send_mail():
	login = entry_1.get()#input('enter a mail: ') 
	password = entry_2.get()#input('enter a password: ')
	url = entry_3.get()#input('URL: ')
	toaddr = entry_4.get()#input('To Whom: ')
	topic = entry_5.get()#input('topic: ')
	message = text_1.get()#input('Enter a message: ')
	num = entry_6.get()#int(input( 'Amount of msg: ' ))

	for value in range( int(num) ):
		msg = MIMEMultipart()

		msg[ 'Subject' ] = topic
		msg[ 'From' ] = login
		body = message
		msg.attach(MIMEText(body, 'plain'))


		server = root.SMTP_SSL( url, 465 )
		server.login( login, password )
		server.sendmail( login, toaddr, msg.as_string())

		value += 1

		print( 'Sent: ' + str( value ) )


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=frame_1, text="Send", command=send_mail)
#button.place(relx=0.5, rely=0.5)
button.pack()

app.mainloop()








