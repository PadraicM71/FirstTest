import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

print(smtp_object.ehlo())

smtp_object.starttls()


# For hidden passwords
import getpass

# result = getpass.getpass("Type something here and it will be hidden: ")
# print(result)



email = "sba20311@student.cct.ie" #input("Enter your email: ")
password = "zoigqtyouzjduljf" #input("Enter your password: ")
smtp_object.login(email,password)
icloud = "padraic.moran@icloud.com"

# # from_address = getpass.getpass("Enter your email: ")
# # to_address = getpass.getpass("Enter the email of the recipient: ")
# subject = input("Enter the subject line: ")
# message = input("Type out the message you want to send: ")
# msg = "Subject: " + subject + '\n' + message
# smtp_object.sendmail(email,icloud,msg)
# # smtp_object.sendmail(from_address,to_address,msg)
# # Enter your email: ········
# # Enter the email of the recipient: ········
# # Enter the subject line: This is a test
# # Type out the message you want to send: Here is the message.

# # above works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

user = email #input("Enter your email: ")

# Remember , you may need an app password if you are a gmail user
# password = getpass.getpass("Enter your password: ")

M.login(user,password)

print(M.list())

# Connect to your inbox
print(M.select("inbox"))

print(M.select("inbox"))

typ, data = M.search(None,'SUBJECT "Security alert"')

print(data)
