import streamlit as st


st.title("Acc Student Info Form")
st.markdown("[Google](https://www.google.com)")

name = st.text_input("Enter Name :")
course = st.selectbox("Enter Course:", ("BCA", "BBA", "B.Tech", "B.Com"))
rno = st.selectbox("Enter Roll No:", (111, 112, 113, 114, 115, 116, 117, 118, 119, 120))
div = st.selectbox("Enter division:", ("A", "B"))
mname = st.text_input("Enter Mother Name")
fname = st.text_input("Enter Father Name")
bname = st.text_input("Enter Brother's Name")
adr = st.text_input("Enter Email")
living = st.selectbox("Enter Living:", ("Sojitra, Anand", "Anand, Sojitra", "Karamsad, Anand"))
spuid = st.selectbox("Enter spu id :", (2023010853, 2023010854, 2023010855, 2023010856, 2023010857))
classdata = st.selectbox("Enter Your Class/College :", (1, 2, 3, 4, 5, "College"))

button = st.button("Submit Form")

if button:
    # f-string નો ઉપયોગ કરીને ડેટા ડિસ્પ્લે
    st.markdown(f"""
    Course : {course}  
    Name : {name}  
    Roll No : {rno}  
    Division : {div}  
    Mother Name : {mname}  
    Father Name : {fname}  
    Brother Name : {bname}  
    Address/Email : {adr}  
    Living : {living}  
    SPU ID : {spuid}  
    Class : {classdata}
    """) 
    