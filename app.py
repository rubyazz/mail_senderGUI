
"""
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_mail():
	login = input('Enter ur mail: ')
	password = input('enter a password: ')
	url = input('URL: ')
	toaddr = input('To Whom: ')
	topic = input('Topic:')
	message = input('Enter a message: ')
	num = int(input( 'Amount of msg: ' ))

	for value in range( num ):
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


def main():
	send_mail()

if __name__ == '__main__':
	main()


"""

import tkinter
import customtkinter

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

entry_3 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="toaddr")
entry_3.pack(pady=20, padx=30)

entry_4 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="topic")
entry_4.pack()

entry_5 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="URL")
entry_5.pack(pady=20, padx=30)


text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "Message\n\n\n\n")


entry_6 = customtkinter.CTkEntry(master=frame_1,width=200, placeholder_text="amount of msg")
entry_6.pack(pady=20, padx=30)

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=frame_1, text="Send", command=button_function)
#button.place(relx=0.5, rely=0.5)
button.pack()

app.mainloop()








