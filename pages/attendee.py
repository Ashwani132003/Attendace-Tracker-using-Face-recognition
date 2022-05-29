from multiprocessing.connection import wait
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
from datetime import datetime
from streamlit_lottie import st_lottie
import firebase_config
from datetime import date


def app(): 
    
    
    st.subheader("Check on Start camera to mark your attendance!!")
    camrun=st.checkbox("Start Camera")
    stframe = st.image([])
    
    if camrun:

        path='classimg'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)


        for cl in (myList):
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
            # print(classNames)
        
        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        
        def markAttendance(name):
            with open('Attendance.csv','r+') as f:
                myDataList = f.readlines()[1:]
                print(myDataList)
                nameList = []
                today = date.today()
                date_ = today.strftime("%d/%m/%Y")
                
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                    nameList.append(",")
                    nameList.append(entry[1])
                    # print(nameList)
                checklist=[]
                checklist.append(name)
                checklist.append(",")
                checklist.append(date_)
                # print(checklist)
                    
                if checklist not in nameList  :
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'{name},{date_},{dtString}'+'\n')
                    
                    

        
        encodeListKnown = findEncodings(images)
        print('Encoding Complete')
        
        cap = cv2.VideoCapture(0)
        
        
        
        def recognise():
            success, img = cap.read()
            #img = captureScreen()
            # time.sleep(5)
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            
            count1=0
            count2=0
        
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
            stframe.image(img)
            
            
            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                #print(faceDis)
                matchIndex = np.argmin(faceDis)
        
                stframe.image(img)

        
        
                if faceDis[matchIndex]< 0.50:
                    name = classNames[matchIndex].upper()
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    markAttendance(name)
           
                else:
                    name = 'Unknown'
                    #print(name)
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                
                if name !="Unknown":    
                    st.success("Attendance marked!!")
                    
            st.write("Uncheck start camera to stop camera!")
            stframe.image(img)

        recognise()
        cap.release()


        