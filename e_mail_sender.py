import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  
sender_email = "pcnotifier20@gmail.com"
password = "pc2020iu"



context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    sender_email = "pcnotifier20@gmail.com"
    receiver_email = "your_email@address.com" # Enter your e-mail address here
    message = "Subject: Run Completed! \nDear PhysiCell user,\n\nYour simulation has been completed succesfully.\nHave a nice day! \n\n---PhysiCell Notifier---"
    server.sendmail(sender_email, receiver_email, message)
    
except Exception as e:
    print(e)
finally:
    server.quit()