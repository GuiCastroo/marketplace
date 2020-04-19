import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import HTTPStatus
import os


class SendEmailHTML:
    def __init__(self, from_email, html, subject):
        self.my_email = os.environ['EMAIL']
        self.from_email = from_email
        self.html = html
        self.subject = subject
        self._email =  os.environ['EMAIL']
        self._password = os.environ['EMAIL_PASSWORD']

    def __configure_message(self):
        message = MIMEMultipart('alternative')
        message['To'] = self.my_email
        message['From'] = self.from_email
        message['Subject'] = self.subject
        message.attach(MIMEText(self.html, 'html'))
        return message

    @classmethod
    def __configure_access(cls):
        email = smtplib.SMTP('smtp.gmail.com', 587)
        email.ehlo()
        email.starttls()
        return email

    def send_email(self):
        try:
            access = self.__configure_access()
            message = self.__configure_message()
            access.login(self._email, self._password)
            access.sendmail(self.my_email, self.from_email, message.as_string())
            access.quit()
            return 'Email seeding success', HTTPStatus.CREATED
        except Exception as e:
            print(e)
            return f'Failure to send email,', HTTPStatus.BAD_REQUEST
