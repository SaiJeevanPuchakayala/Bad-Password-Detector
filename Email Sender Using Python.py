import smtplib
senderemail = "#"                                     #Enter your gmail id here
recieveremail = "#"                                   #Enter reciever gmail id here
password = input(str("Please enter your password: ")) #Enter password of your gmail
SUBJECT = "#"                                         #Enter your email subject here
TEXT = "#"                                            #Enter the actual email content here
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)   #Enter your message here.
server = smtplib.SMTP('smtp.gmail.com',587)           #Here the SMTP server is established
server.starttls()                                     #Here the server is secured
server.login(senderemail,password)                    #Here your gmail login takes place
print("****************Login Successful*********************")
server.sendmail(senderemail,recieveremail,message)    #Here Email will be composed and sent to reciever gmail.
print("Message Sent Successfully to ",recieveremail)