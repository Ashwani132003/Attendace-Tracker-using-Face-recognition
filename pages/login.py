from pages import home,attendee,host
import pyrebase
import streamlit as st
from datetime import datetime
import firebase_config

# Configuration key

def app():
  

    # Firebase Authentication
    
    firebase = firebase_config.fire() 
    auth = firebase.auth()

    #   Database

    db = firebase.database()
    storage = firebase.storage()

    st.title("Attendance Tracker")

    # Authentication

    choice = st.selectbox('login/Signup',['Login','Sign up'])
    email = st.text_input('Please enter your email address')
    password = st.text_input('Please enter your password',type='password')

    if choice == 'Sign up':
        handle = st.text_input("Please input your app handle name",value='Default')
        submit = st.button('Create my account')
    
        if submit:
            user = auth.create_user_with_email_and_password(email,password)
            st.success('Your account is created successfully!')
            st.balloons()
        
            #Signin
            user = auth.sign_in_with_email_and_password(email,password)
            db.child(user['localId']).child("Handle").set(handle)
            db.child(user['localId']).child("Id").set(user['localId'])
            st.title('Welcome' + handle +'your account is')
            st.info('Login via drop down selection')
            

    if choice == 'Login':
        login = st.checkbox('Login')
        if login:
            user = auth.sign_in_with_email_and_password(email, password) 
            st.info('Welcome  , You are logged in. Please select your role on Home Page')
            
            
  
                
              
                
                    
    
      




# import pickle
# from pathlib import Path
# from pages import home 
# import streamlit as st
# import streamlit_authenticator as st_auth

# def app():
#     names = ["Peter Parker", "Rishav"]
#     usernames = ["pparker","rrishav"]
#     password = ["abc123","def456"]


#     hashed_passwords = st_auth.Hasher(password).generate()

#     file_path = Path(__file__).parent / "hashed_pw.pkl"
#     with file_path.open("wb") as file:
#         pickle.dump(hashed_passwords, file)
        
#     authenticator = st_auth.Authenticate(names,usernames,hashed_passwords,
#         'some_cookie_name','some_signature_key',cookie_expiry_days=30)
        
#     name, authentication_status, username = authenticator.login('Login','main')    
        
        
#     # if authentication_status:
#     #     authenticator.logout('Logout', 'main')
#     #     st.write('Welcome *%s*' % (name))
#     #     st.title('Some content')
#     # elif authentication_status == False:
#     #     st.error('Username/password is incorrect')
#     # elif authentication_status == None:
#     #     st.warning('Please enter your username and password')   
        
        
#     if st.session_state['authentication_status']:
#         authenticator.logout('Logout', 'main')
#         st.write('Welcome *%s*' % (st.session_state['name']))
#         st.title('Some content')
#         home.app()
        
#     elif st.session_state['authentication_status'] == False:
#         st.error('Username/password is incorrect')
#     elif st.session_state['authentication_status'] == None:
#         st.warning('Please enter your username and password')     