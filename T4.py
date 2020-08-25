{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "pickle_in=open(\"heart_d.pkl\",\"rb\")\n",
    "model=pickle.load(pickle_in)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import streamlit as stm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return \"Welcome All\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gender(s):\n",
    "    s=s.title()\n",
    "    if s==\"Male\":\n",
    "        return 1\n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal):\n",
    "    result=model.predict([[age,gender(sex),cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal]])\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1], dtype=int64)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prediction(38,\"male\",2,156,220,1,0,1,1.4,2,3,2,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def disease(result):\n",
    "    if result==1:\n",
    "        return \"postive\"\n",
    "    return \"negative\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    stm.title(\"Heart Disease Predictor\")\n",
    "    html_temp=\"\"\"\n",
    "    <div style=\"background-color:blue;padding:10px\">\n",
    "    <h2 style=\"color:black;text-align:center;\">Heart Disease Predictor ML App</h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    stm.markdown(html_temp,unsafe_allow_html=True)\n",
    "    age=stm.text_input(\"age\",\"Type Here\")\n",
    "    sex=stm.text_input(\"sex\",\"Type Here\")\n",
    "    cp=stm.text_input(\"cp\",\"Type Here\")\n",
    "    trestbps=stm.text_input(\"trestbps\",\"Type Here\")\n",
    "    chol=stm.text_input(\"chol\",\"Type Here\")\n",
    "    fbs=stm.text_input(\"fbs\",\"Type Here\")\n",
    "    restecg=stm.text_input(\"restecg\",\"Type Here\")\n",
    "    thalang=stm.text_input(\"thalang\",\"Type Here\")\n",
    "    exang=stm.text_input(\"exang\",\"Type Here\")\n",
    "    oldpeak=stm.text_input(\"oldpeak\",\"Type Here\")\n",
    "    slope=stm.text_input(\"slope\",\"Type Here\")\n",
    "    ca=stm.text_input(\"ca\",\"Type Here\")\n",
    "    thal=stm.text_input(\"thal\",\"Type Here\")\n",
    "    result=\"\"\n",
    "    if stm.button(\"Predict\"):\n",
    "        result=prediction(age,gender(sex),cp,trestbps,chol,fbs,restecg,thalang,exang,oldpeak,slope,ca,thal)\n",
    "        result=disease(result)\n",
    "        stm.success(\"Result is\",str(result))\n",
    "    if stm.button(\"About\"):\n",
    "        stm.text(\"Lets Learn\")\n",
    "        stm.text(\"Built with Streamlit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__==\"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3rc1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
