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
    email = email
    from_emails = input(' Sender email: ') # The person you want to send it as
    name = input(' Sender name: ') # The sender emails name
    password = password
    recipient = input(' Recipient email: ') # The person you're sending the email to
    lines()

    subject = input(' Email subject: ') # Subject of the message
    print('(Type \'END\' on a new line to complete message)')
    print(' Enter message: ')
    # As long as the input of the user is not 'END', then add the words into a .txt file that 
    # is going to be sent to the recipient
    while True:
        words = input(' > ')
        if words == 'END':
            break
        elif '' in words:
            with open('text_s.txt', 'a') as f:
              # Add the words to the .txt tile
                f.write(words)
                f.write('\n')
        with open('text_s.txt', 'r') as r:
            msg7 = r.read()
            # Open the file with 'r' so that it's readable
    # Put the r.read() in message so it sends in plaintext
    message = (f"""{msg7}
    """)

    msg = MIMEMultipart()
    msg['Name'] = name
    msg['From'] = name + '<' + from_emails + '>'
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message)) # Configure msg
    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587) # The SMTP server and the port number
    server.starttls() # Start transport layer security
    try:
      # Try to login and send the email
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(from_emails, recipient, text)
        server.quit() # Quit the server
        os.remove('text_s.txt') # Delete the .txt file
        print('\n')
        print(' Email successfully sent')
        total = 100 # Maximum of 100 emails to be sent
        if os.path.exists('messages_sent.txt'): # If this file exists, then adda number to the file
            with open('messages_sent.txt', 'r') as f:
                times_sent = int(f.read())
        else:
            times_sent = 0
        times_sent += 1 # This will raise the count of the number in the file
        print('\n You sent ' + str(times_sent) + ' message(s). [' + str(total - times_sent) + ' emails left]')
        with open('messages_sent.txt', 'w') as f:
            f.write(str(times_sent))
            # Now it will actually raise it up
    except Exception as e:
      # Print the error if the email fails to send properly
        print('\n')
        print(e)
        time.sleep(0.75)
    
    def resend():
      # Ask the user if they want to send another email
        email_resend = input(' Would you like to send another email? [y/n]\n > ')
        if email_resend == 'y':
            main()
        elif email_resend == 'n':
            time.sleep(0.5)
            leave = input('Press [Enter] to exit...')
            sys.exit() # Leave the program
        else:
            resend()
    resend()
main()
