import pickle
import json
import streamlit as st

model=pickle.load(open('model.pkl','rb'))

st.title('IoT Web App')

humidity=st.number_input('Enter Humidity')
temperature=st.number_input('Enter Temperature')

if st.button('Predict Result'):
    data=model.predict([[humidity,temperature]])
    st.success(data[0])

