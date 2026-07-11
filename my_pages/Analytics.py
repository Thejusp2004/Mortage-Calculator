import streamlit as st
import pandas as pd

def show():
  col1,col2,col3 = st.columns([3,5,1])
  with col2:
    st.title("📈 Loan Analytics")
    st.caption("Visualize repayment trends and remaining loan balance.")
   
    
  if "df" not in st.session_state:
       st.warning("Go to Home page first.")
       return
  
  df=st.session_state["df"]
  payments_df = df[["Year","Remaining Balance"]].groupby("Year").min()
  st.write("")
  st.write("")

  st.subheader("Remaining Balance Trend")
  st.write("")
  st.line_chart(payments_df)
  st.write("")
  st.write("")
  st.subheader("Yearly Comparison")
  st.write("")
  st.bar_chart(payments_df)
