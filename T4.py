#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
pickle_in=open("heart_d.pkl","rb")
model=pickle.load(pickle_in)


# In[3]:


from PIL import Image


# In[4]:


import numpy as np
import pandas as pd
import streamlit as stm


# In[5]:


def welcome():
    return "Welcome All"


# In[6]:


def gender(s):
    if type(s)==str:
        s=s.title()
    if s=="Male" or s==1:
        return 1
    if s=="Female" or s==0:
        return 0


# In[7]:


def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal):
    result=model.predict([[age,gender(sex),cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal]])
    return result


# In[8]:


def disease(result):
    if result==1:
        return "postive"
    return "negative"


# In[9]:


def main():
    stm.title("Heart Disease Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Predictor ML App</h2>
    </div>
    """
    stm.markdown(html_temp,unsafe_allow_html=True)
    age=stm.text_input("age","Type Here")
    sex=stm.text_input("sex","Type Here")
    cp=stm.text_input("cp","Type Here")
    trestbps=stm.text_input("trestbps","Type Here")
    chol=stm.text_input("chol","Type Here")
    fbs=stm.text_input("fbs","Type Here")
    restecg=stm.text_input("restecg","Type Here")
    thalang=stm.text_input("thalang","Type Here")
    exang=stm.text_input("exang","Type Here")
    oldpeak=stm.text_input("oldpeak","Type Here")
    slope=stm.text_input("slope","Type Here")
    ca=stm.text_input("ca","Type Here")
    thal=stm.text_input("thal","Type Here")
    result=""
    if stm.button("Predict"):
        result=prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal)
        result=disease(result)
    stm.success("Result is "+str(result))
    if stm.button("About"):
        stm.text("Lets Learn")
        stm.text("Built with Streamlit")


# In[10]:


if __name__=="__main__":
    main()


