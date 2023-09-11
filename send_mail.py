import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='b9bd2b2883a05e'
    password='649276423f441a'
    message=f"<h3>New feedback submission</h3><ul><li>Customer:{customer}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul>"
    sender_email='example1@gmail.com'
    receiver_email='example2@gmail.com'
    msg=MIMEText(message,'html')
    msg['Subject']='Storilabs Feedback'
    msg['from']=sender_email
    msg['To']=receiver_email
    
    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        
   
