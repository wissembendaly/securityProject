from email.message import EmailMessage
import smtplib
import random


class Emailsender:
    def __init__(self):
        self.s = smtplib.SMTP("smtp.gmail.com", 587)

    password = "ramziwissem"
    emailadress = "projetsecurite2022@gmail.com"

    def emailsender(self,emailreceiver:str,validationcode:str):
        # message to be sent
        subject = "Connect the project"
        
        body = """Hi,
            Welcome to our project. We’re thrilled to see you here!
            We’re confident that our app be helpful.
            your validation code is: %s
            please insert the validation code to finish your registration
                
                Take care!""" % (validationcode)
        
        message = EmailMessage()
        message.set_content(body)
        message['Subject'] = subject
        self.s.send_message(self.emailadress, emailreceiver, message)
        print("Email send to " + emailreceiver)
        
    def generaterandomnumber(self):
        number = random.randit(1111,9999)
        print(number)
        return number

    def login(self):
        self.s.ehlo()
        self.s.starttls() # for security
        self.s.ehlo()
        # Authentication
        self.s.login(self.emailadress, self.password)
        print("login")
        self.s.quit()
        print("sent")

    def sendemail(self,email:str,validationcode):
        self.login()
        self.emailsender(email,validationcode)
