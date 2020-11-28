import smtplib
to = input("Enter receipient mail id\n")
body = input("Message\n")
def sendemail(to,body):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enggdeepmoy@gmail.com','deepmoy31')
    server.sendmail('enggdeepmoy@gmail.com',to,body)
    server.close
sendemail(to,body)
