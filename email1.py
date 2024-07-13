import smtplib
sender_email=input("enter sender email")
receiver_email=input("enter receiever mail")
subject=input("enter subject")
message=input("enter message")
text=f"subject:{subject}\n\n{message}"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,"kplj ufip eakk ulvr")
server.sendmail(sender_email,receiver_email,text)
print("email has been sent to")