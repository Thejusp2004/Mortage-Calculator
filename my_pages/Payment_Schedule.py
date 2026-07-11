import streamlit as st
import pandas as pd



def show():
   
   col1,col2,col3 = st.columns([3,5,2])
   with col2:
    st.title("📊 Payment Schedule")
    st.caption("Detailed monthly repayment breakdown.")

    st.write("")
    st.write("")
    

    if "df" not in st.session_state:
      st.warning("Go to Home page first.")
      return
    df=st.session_state["df"]
   csv = df.to_csv(index=False)
   with col3:
     st.download_button(
        label="⬇️ Export Schedule",
        data=csv,
        file_name="payment_schedule.csv",
        mime="text/csv"
    )
   st.dataframe(
    df,
    use_container_width=True,
    height=600)
   csv = df.to_csv(index=False)
