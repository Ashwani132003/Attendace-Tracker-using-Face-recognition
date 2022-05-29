import streamlit as st
from pages import analysis
import pandas as pd
import plotly.express as px
import time

    

                    
def app():

    role=st.selectbox('Please select your role',('Host','Attendee'),key="role")
    if  role== 'Host':
        st.header('Analysis')
        analysis.analysis()
 
                           
            
    else:
        analysis.attendee()
        
        
        
        