import streamlit as st
import joblib
st.title("**_Startup Profit Predictor_**")
hide_st_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer{visibility:hidden;}
    header {visibility:hidden;}
    </style>
    """
st.markdown(hide_st_style,unsafe_allow_html=True)
RDS=st.number_input("Enter R&D Spend")
AS=st.number_input("Enter Administration Spend")
MS=st.number_input("Enter Marketing Spend")
re_model=joblib.load("startup_prediction")
op=re_model.predict([[RDS,AS,MS]])
if st.button('predict'):
    st.title(op[0])
