
import streamlit as st
from pages import login,host,attendee
import json
import requests
from streamlit_lottie import st_lottie





def app():
    
    
    st.title("Welcome to Attendance Tracker")
    
    def load_lottieurl(url: str):
        r= requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_1pxqjqps.json")
    st_lottie(lottie_hello,key="hello", height="150px", width="150px")
    
    
    role=st.selectbox('Please select your role',('Host','Attendee'),key="role")
    
    if role== 'Host':
        host.app()
    
    if role == 'Attendee':
        lottie_face = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_2szpas4y.json")
        st_lottie(lottie_face,key="face", height="150px", width="150px")
        
        attendee.app()