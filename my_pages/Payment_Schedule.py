import streamlit as st
import pandas as pd



def show():
   
   col1,col2,col3 = st.columns([3,5,1])
   with col2:
    st.title("📊 Payment Schedule")
    st.caption("Detailed monthly repayment breakdown.")
    
    st.write("")
    st.write("")
    

    if "df" not in st.session_state:
      st.warning("Go to Home page first.")
      return
    df=st.session_state["df"]
  
   st.dataframe(
    df,
    use_container_width=True,
    height=600)
