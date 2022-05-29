# Attendace-Tracker-using-Face-recognition
This Web-app is part of Microsoft Engage Program 2022. This Web-app keeps track on the Attendance of users. This web-app is very easy to use and convenient. by face recognition and provides detailed analysis of attendance to the Host and Attendee respectively.

# 🖥Tech Stack:
 - Python - Developed using Python.</br>
 - Streamlit - Interface for App.</br>
 - Firebase - Authentication and Storage.</br>
 - Opencv - Face recognition.</br>
 - Streamlit_lottie - Animations in App.</br>
 - Yagmail - To send email.</br>
 - Csv - Attendance files.</br>
 
# 🎇Features:
  - Face Recognition - Provides more secure attendance tracking.</br>
  - Full Attendees List - Gives complete attendance list of all time.</br>
  - Daily Attendance List - Daily attendance list available to the Host.</br>
  - Email feature - Send complete Attendance List to Host via mail in csv format.</br>
  - Analysis Plots - Shows graph plot analysis for Attendee with number of attendance.</br>
  - Login/Signup(Profile) - Login/Signup for users.</br>
  - Single person info. - Able to show complete attendance details for specific user by his/her name.</br>
  - Filters - Different filters on attendees names, dates with plots changing according to them.</br>
  - Total attendance checking for attendee.</br>
  - Separate file record - Host can get different files in pc for each unique attendee with their full attendace history.</br>
 # 📱 Screenshots:
  ![image](https://user-images.githubusercontent.com/76273539/170877956-9af3d938-fc15-489f-81e4-3c07d0ffab31.png)
![Screenshot (33)](https://user-images.githubusercontent.com/76273539/170878187-7ec6b937-229e-4e4d-a34d-808ece71ed9e.png)
![Screenshot (34)](https://user-images.githubusercontent.com/76273539/170878197-0357de1c-696b-4ff3-992a-6559500d2f93.png)
![Screenshot (35)](https://user-images.githubusercontent.com/76273539/170878199-b6ba9ca5-66f3-4efe-9b3c-e6a1451b7345.png)
![Screenshot (36)](https://user-images.githubusercontent.com/76273539/170878201-cef6e214-d695-4aef-8903-576cbaeed7e6.png)
![Screenshot (37)](https://user-images.githubusercontent.com/76273539/170878202-5c669147-b7d2-4271-833e-29a9e2c60be8.png)

# ❓ How to use the app?
  - Fork the web-app and run it on your local-machine.</br>
  - Install all requirements.</br>
  - Connect app to your firebase account.</br>
  - Type - "streamlit run main.py" in your terminal.</br>
  - Create an account -> Register by providing all the required details asked.</br>
  - Signin to your account and go to home page and choose your role(Host/Attendee).</br>
  
# How it works?
  - After creating an account and signing in.</br>
  - User goes to home page and marks attendance if he is attendee.</br>
  - App recognises face of attendee and mark his name,date,time on csv file if he is in database otherwise an unknown mark is shown.</br>
  - If user is a host he got two choices-1) To get full attendance list till time via email. 2) To see only that day's attendance list.</br>
  - On Dashboard section host can choose specific filters to get plotted data of attenddance and can check attendance history for specific user.</br>
  - On Dashboard section of Attendee, attendee can see his/her total attendance till day and full list of his all attendances with time and date.</br>
  
