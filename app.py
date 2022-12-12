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


#pass mrxabd690@gmail.com