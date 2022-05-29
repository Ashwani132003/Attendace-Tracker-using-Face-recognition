
import streamlit as st
from streamlit_option_menu import option_menu

from pages import home, dashboard, login

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Navigation',
                options=['Home','Dashboard','Login'],
                icons=['house','book','envelope'],
                menu_icon='cast',
                default_index=0,
                
                
                )


        
        if app == "Home":
            home.app()
        if app == "Dashboard":
            dashboard.app()
        if app == "Login":
            login.app()        
            
          
             
    run()            
            