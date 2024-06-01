import streamlit as st
import numpy as np
import pickle
import xgboost

st.title('Diabetes Prediction')

loaded_model = pickle.load(open('Diabetesmodel.pkl', 'rb'))

def Diabetes_Prediction(input_data):

    input_data_numpyarray = np.asarray(input_data)
    input_reshape = input_data_numpyarray.reshape(1,-1)

    prediction = loaded_model.predict(input_reshape)

    if (prediction[0]==0):
        st.write("Low risk in diabetes.")

    else:
        st.write("Aware! High risk in Diabetes!!")

def radio_button(radio):

    if radio == 'Yes':
        return 1
    else:
        return 0

def radio_button_sex(radio):

    if radio == 'Male':
        return 1
    else:
        return 0

def main():

    #st.write("Diabetes Prediction Model")

    #BP = st.number_input("Do you have High Blood Pressure?")
    #C = st.number_input("Do you have High Cholesteral?")

    yes_no = ['Yes', 'No']

    BP = st.radio("Do you have High Blood Pressure?", yes_no)
    C = st.radio("Do you have High Cholesterol?", yes_no)
    CC = st.radio("Do you have Cholesterol check in 5 years?", yes_no)
    BMI = st.number_input("What is your BMI?")
    Smoke = st.radio("Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no, 1 = yes", yes_no)
    Stroke = st.radio("(Ever told) you had a stroke", yes_no)
    CHD = st.radio("Coronary Heart Disease (CHD) or Myocardial Infarction (MI)", yes_no) 
    PhysAcctivity = st.radio("Physical activity in past 30 days - not including job", yes_no)
    Fruit = st.radio("Consume Fruit 1 or more per day ", yes_no)
    Veggies = st.radio("Consume Vegetables 1 or more per day", yes_no)
    HvyAlcoholConsump = st.radio("Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)", yes_no)
    AnyHealthcare = st.radio("Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.", yes_no)
    NoDocbcCost = st.radio("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", yes_no)
    GenHlth = st.slider("Would you say that in general your health is scale 1-5: 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor", 1, 5, 1)
    MentHlth = st.slider("Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? It is in days, scale will be between 0-30", 0, 30, 1)
    PhysHlth = st.slider("Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? It is in days, scale will be between 0-30", 0, 30, 1)
    DiffWalk = st.radio("Do you have serious difficulty walking or climbing stairs?", yes_no)
    Sex = st.radio("Sex", ['Female', 'Male'])
    Age = st.slider("13-level age category (_AGEG5YR see codebook21 linked above): scale 1-13: 1 = 18-24, 8 = 55-59, 13 = 80 or older", 1, 13, 1)
    Education = st.slider("Education level (EDUCA see codebook21 linked above): scale 1-6: 1 = Never attended school or only kindergarten 2 = Grades 1 through 8", 1, 8, 1)
    Income = st.slider("Income scale (INCOME3 see codebook21 linked above): scale 1-8: 1 = less than 10,000 5 = less than 35,000 11 = 200,000 or more", 1, 11, 1)
    
    #if BP == 'Yes':
    #    BP_ans = 1
    #else:
    #    BP_ans = 0
    

    diagnosis = ''

    if st.button('Predict'):
        diagnosis = Diabetes_Prediction([radio_button(BP),radio_button(C), radio_button(CC), BMI, 
                                        radio_button(Smoke), radio_button(Stroke), radio_button(CHD), radio_button(PhysAcctivity), 
                                        radio_button(Fruit), radio_button(Veggies), radio_button(HvyAlcoholConsump), radio_button(AnyHealthcare), radio_button(NoDocbcCost),
                                        GenHlth, MentHlth, PhysHlth, radio_button(DiffWalk), radio_button_sex(Sex), Age, Education, Income])

if __name__ == '__main__':
    main()