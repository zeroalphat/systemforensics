import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def send_mail(send_from, send_to, subject, text, files, isTls=False):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    #part.set_payload(open("test.txt", "r").read())
    part.set_payload(read_local_file(files))

    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename='+files.split('/')[-1])
    msg.attach(part)

    #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    # SSL connection only working on Python 3+
    smtp = smtplib.SMTP(host="localhost", port=1025)
    if isTls:
        smtp.starttls()
    # smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


def read_local_file(filename):
    with open(filename, "r") as lines:
        return lines.read()


send_from = input('Enter from_mail_address: ')
send_to = input('Enter to_mail_address: ')
subject = input('Enter subject: ')
text = input('Enter main text: ')
filename = input('Enter attached file name: ')

#send_mail('hoge@gmail.com', 'alisa@hoge.com', 'test', 'hoge hoge', 'test.txt')
send_mail(send_from, send_to, subject, text, filename)
print('mail send success')
