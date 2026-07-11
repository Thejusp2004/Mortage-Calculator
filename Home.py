import streamlit as st
import pandas as pd
import math
from my_pages import Analytics,Payment_Schedule 


st.set_page_config(
    page_title="Mortgage Calculator",
    page_icon="🏦",
    layout="wide"
)

page = st.sidebar.radio("Navigation", ["🏠 Home", "📊 Payment Schedule", "📈 Analytics"]
)

def show():
    col1,col2,col3 = st.columns([2,5,1])
    with col2:
       st.title("🏦 Mortgage Repayment Calculator")
       st.caption("Plan your home loan repayments intelligently.")
    st.write("")

    st.subheader("Input Data")
    st.write("")
    
    col1,col2,col3,col4 = st.columns(4)
    home_value = col1.number_input("Home Value", min_value=0,value = 500000)
    deposit = col2.number_input("Deposit",min_value=0,value=100000)
    interest_rate = col3.number_input("Interest rate ( in % )",min_value=0.0,value=5.5)
    loan_term=col4.number_input("Loan Term (in years)",min_value=1,value=30)

    loan_amount = home_value - deposit
    monthly_interest_rate=(interest_rate/100)/12

    if monthly_interest_rate == 0:
      monthly_payment = loan_amount / number_of_payments
    else:
      number_of_payments = loan_term * 12
      monthly_payment = (loan_amount * (
                     (monthly_interest_rate * ((1 + monthly_interest_rate) ** number_of_payments))
                     / (((1 + monthly_interest_rate) ** number_of_payments)- 1)))

    total_payments = monthly_payment * number_of_payments
    total_interest = total_payments - loan_amount

    st.write("")
    st.divider()
    st.subheader("Repayments")
    st.write("")
    col1,col2,col3 = st.columns(3)

    col1.metric(label="Monthly Repayments",value=f"Rs {monthly_payment:,.2f}")
    col2.metric(label="Total Repayments",value=f"Rs {total_payments:,.2f}")
    col3.metric(label="Total Interest",value=f"Rs {total_interest:,.2f}")

    schedule = []
    remaining_balance = loan_amount

    for i in range(1, number_of_payments + 1):
       if monthly_interest_rate == 0:
        interest_payment = 0
        principal_payment = monthly_payment
       else:
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment

    remaining_balance -= principal_payment
    year = math.ceil(i / 12)

    schedule.append(
      [i,monthly_payment,principal_payment,
      interest_payment,remaining_balance,year])

    df = pd.DataFrame(schedule,
                    columns=["Month","Payment","Principal","Interest","Remaining Balance","Year"])

    st.session_state["df"]=df
    
if page == "🏠 Home":
  show()
elif page == "📊 Payment Schedule":
  Payment_Schedule.show()
elif page == "📈 Analytics":
  Analytics.show()
