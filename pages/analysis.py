import streamlit as st
import pandas as pd
import plotly.express as px
import splited

# Reading csv file
df_new = pd.read_csv("Attendance.csv")
new = pd.ExcelWriter('Attendance.xlsx')
df_new.to_excel(new, index=False)
from datetime import date

# saving xlsx file
new.save()    
st.markdown("---")
df = pd.read_excel(new, engine='openpyxl') 

def date_attendance():
    today = date.today()
    date_ = today.strftime("%d/%m/%Y")
  
    st.dataframe(df[df['Date'] == date_])
    
    

def analysis():

    
       
 
    name1=st.text_input(label="Search by name")
    if name1:
        st.dataframe(df[df['Name'] == name1])
        
    if st.button("Download separate attendance files for each attendee "):
        splited.split()
            
    st.sidebar.header("Please filter here:")
    name = st.sidebar.multiselect(
    "Select the attendee name:",
    options=df["Name"].unique(),
    default=df["Name"].unique(),
        
    )
        
    Dat = st.sidebar.multiselect(
        "Select the Date:",
        options=df["Date"].unique(),
        default=df["Date"].unique(),
            
     )
    
  
    df_selection = df.query(
    "Name == @name & Date==@Dat"
    
    )
    st.dataframe(df_selection)
    
    att_by_name = df_selection.groupby("Name").count()
    fig_att = px.bar(
        att_by_name,
        y=att_by_name.index,
        x="Time",
        title="<br>Attendance by name</br>",
        color_discrete_sequence=["#0083B8"]*len(att_by_name),
        template="plotly_white",
    )    
    
    fig_att.update_layout(
        xaxis=dict(showgrid=False),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(tickmode="linear")),
    )
    
    st.plotly_chart(fig_att)
    
    
    
    
    st.markdown('---')                     
    

def attendee():
    
    st.subheader("Enter your name to see your attendance Analysis!")
    name1=st.text_input(label="Enter name")
    if name1:
        if st.button("Total Attendance:"):
            c=len(df[df['Name'] == name1])
            st.success("Total number attendance of "+ str(name1) +" is: " +str(c)  )   
    
        if st.button("Click to see your full attendance list "):
        
            df_output= df[df['Name'].str.contains(name1)]
            st.dataframe(df_output)
        
    