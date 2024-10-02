import streamlit as st
st.title("Welcome to Louie's BMI Calculator")
st.text("Body mass index (BMI) is a measure of body fat based on height \nand weight that applies to adult men and women.")

#take weight input in kgs
weight = st.number_input("Enter your weight (in kg)")

#TAKE HEIGHT INPUT
# RADIO BUTTON TO CHOOSE HEIGHT FORMAT
status = st.radio("select your height format: ",('cms','meters','feet'))

if (status == 'cms'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value for height")

elif (status == 'meters'):
    #take height in meters
    height = st.number_input('Meters')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value for height")

else:
    height = st.number_input('Feet')

    try:
        bmi = weight / (((height / 3.28))**2)
    except:
        st.text("Enter some value for height")

if (st.button('calculate BMI')):
    # print the BMI INDEX
    st.text("Your BMI index is {}.".format(bmi))

# give the interpretation of BMI index

    if(bmi < 16):

        st.error("You are Extremely Underweight")

    elif(bmi >= 16 and bmi < 18.5):

        st.warning("You are Underweight")

    elif(bmi >= 18.5 and bmi < 25):

        st.success("Healthy")

    elif(bmi >= 25 and bmi < 30):

        st.warning("Overweight")

    elif(bmi >= 30):

        st.error("Extremely Overweight")

st.text("for more information about overweight click the link below")
st.link_button("Does Your BMI Really Matter? Is It Useful Or Useless?", "https://youtu.be/JJf9BzIf1oo?si=8QH0IVCckogeR4eV")