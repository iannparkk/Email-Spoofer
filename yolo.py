import sys
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def lines():
    print('------------------------')

def main():
    lines()
    print(' EMAIL SPOOFER')
    lines()
    email = 'icwtr.g0d@gmail.com'
    from_emails = input(' Sender email: ')
    name = input(' Sender name: ')
    password = '9JhWmHSvRIG5FDs0'
    recipient = input(' Recipient email: ')
    lines()

    subject = input(' Email subject: ')
    print(' Enter message: ')
    while True:
        words = input(' > ')
        if words == 'END':
            break
        elif '' in words:
            with open('text_s.txt', 'a') as f:
                f.write(words)
                f.write('\n')
        with open('text_s.txt', 'r') as r:
            msg7 = r.read()
    message = (f"""{msg7}
    """)

    msg = MIMEMultipart()
    msg['Name'] = name
    msg['From'] = name + '<' + from_emails + '>'
    msg['To'] = recipient
    msg['Subject'] = subject
    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    server.starttls()
    try:
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(from_emails, recipient, str(message))
        server.quit()
        print('\n')
        print(' Email successfully sent')
        total = 100
        if os.path.exists('messages_sent.txt'):
            with open('messages_sent.txt', 'r') as f:
                times_sent = int(f.read())
        else:
            times_sent = 0
        times_sent += 1
        print('\n You sent ' + str(times_sent) + ' message(s). [' + str(total - times_sent) + ' emails left]')
        with open('messages_sent.txt', 'w') as f:
            f.write(str(times_sent))
    except Exception as e:
        print('\n')
        print(e)
        time.sleep(0.75)
    
    def resend():
        email_resend = input(' Would you like to send another email? [y/n]\n > ')
        if email_resend == 'y':
            main()
        elif email_resend == 'n':
            time.sleep(0.5)
            leave = input('Press [Enter] to exit...')
            sys.exit()
        else:
            resend()
    resend()
main()
