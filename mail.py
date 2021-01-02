import os
import smtplib

#Only works on Max's PC due to environment variables. Otherwise my password would be public.
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

with smtplib.SMTP('smtp.gmail.com', 587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.ehlo()

    smpt.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #Subject line for the email
    subject = "Here are your Solution Challenge team suggestions!"
    #Body message for the email
    body = "hi"

    msg = f"Subject: {subject}\n\n{body}"
    
    #Email addres from which it is sent from, and sent to
    smpt.sendmail(EMAIL_ADDRESS, "maxmuoto@gmail.com", msg)