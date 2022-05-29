import streamlit as st
import pyrebase
import os
import mail
from pages import analysis


with open('Attendance.csv','r+') as f:
    
    f.writelines("Name,Date,Time")
    

def app():

    
    
    if st.button("Get complete attendance list via mail"):
        mail.app()
    
    if st.button("Todays attendance list"):
        analysis.date_attendance()
        
               
                
                
       
        
        
        
        