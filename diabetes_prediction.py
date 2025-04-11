import streamlit as st
import pandas as pd
import pickle
import numpy as np

pickle_in = open('modelpickle.pkl', 'rb')
load_pk= pickle.load(pickle_in)

def app():
    st.title("Diabetes prediction")
    st.sidebar.title("Input Features")

    preg=st.sidebar.slider("Pregnancies",0.0,20.0,3.0)
    glu=st.sidebar.slider("Glucose",40.0,200.0,3.0)
    blood=st.sidebar.slider("BloodPressure",40.0,150.0,3.0)
    skt=st.sidebar.slider("SkinThickness",10.0,50.0,3.0)
    insu=st.sidebar.slider("Insulin",0.0,150.0,3.0)
    bmi=st.sidebar.slider("BMI",10.0,60.0,3.0)
    pedig=st.sidebar.slider("DiabetesPedigreeFunction",0.0,3.0,3.0)
    age=st.sidebar.slider("Age",20.0,80.0,3.0)

    # make prediction:
    input_data=[preg,glu,blood,skt,insu,bmi,pedig,age]
    input_data_np_array=np.asarray(input_data)
    reshape_data=input_data_np_array.reshape(1,-1)
    prediction=load_pk.predict(reshape_data)

    print(prediction)

    if (prediction[0]==1):
        st.warning("You are a diabetic patient")
    else:
        st.success("You are in good shape donot worry no diabetes in your body")



if __name__=="__main__":
    app()
