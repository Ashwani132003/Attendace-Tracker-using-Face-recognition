import yagmail 
import os
import streamlit as st
import datetime

def app():
    date = datetime.date.today().strftime("%B %d, %Y")
    # path = 'Attendance.csv'
    # os.chdir(path)
    # files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    # newest = files[-1]
    # filename = newest
    sub = "Attendance Report for " + str(date)
    # mail information

    sender_mail = "siwachashwani0103@gmail.com"
    receiver_mail = "siwachsahab1@gmail.com"
    filename='Attendance.csv'
    # sent the mail
    yag = yagmail.SMTP(sender_mail, "siwach$132003")
    yag.send(
        to=receiver_mail,
        subject=sub, # email subject
        contents=["Attendance List for today"],  # email body
        attachments= filename  # file attached
    )
    st.write("Email Sent!")