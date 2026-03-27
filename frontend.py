import streamlit as st
import requests

st.title("PLACEMENT PREDICTION >>")

cgpa =st.slider("CGPA",0.0,10.0,7.0)
aptitude=st.slider("Aptitude Score",0,100,70)
communication=st.slider("Communication",1,10,5)
project=st.slider("Project",0,5,2)

if st.button("Predict"):
    url ="https://placement-prediction-1-fsqk.onrender.com/predict"

    data={
        'cgpa':cgpa,
        'aptitude':aptitude,
        'communication':communication,
        'project':project,
        
    }

    response = requests.post(url,json=data)
    result = response.json()
    if result['prediction']==1:
        st.success("You will get placed")
        
    else:
        st.error("Not likely to be placed")
    
