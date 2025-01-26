import streamlit as st
import numpy as np

# Set up the main page
st.title("Financial Planning Calculator")
st.sidebar.title("Choose Calculator")

# Sidebar navigation
calculator = st.sidebar.radio(
    "Select a Calculator:",
    ("Retirement Savings", "Loan Repayment", "Investment Growth")
)

# 1. Retirement Savings Calculator
if calculator == "Retirement Savings":
    st.header("Retirement Savings Calculator")
    
    # Input fields
    current_age = st.number_input("Current Age", min_value=18, max_value=80, value=30, step=1)
    retirement_age = st.number_input("Desired Retirement Age", min_value=30, max_value=80, value=65, step=1)
    current_savings = st.number_input("Current Savings ($)", min_value=0, value=0, step=1000)
    monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, value=500, step=100)
    annual_return_rate = st.number_input("Expected Annual Return Rate (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
    
    if st.button("Calculate Retirement Savings"):
        years_to_retirement = retirement_age - current_age
        future_savings = current_savings
        for _ in range(years_to_retirement * 12):
            future_savings += monthly_contribution
            future_savings *= (1 + annual_return_rate / 100 / 12)
        st.success(f"Estimated Savings at Retirement: ${future_savings:,.2f}")

# 2. Loan Repayment Calculator
elif calculator == "Loan Repayment":
    st.header("Loan Repayment Calculator")
    
    # Input fields
    loan_amount = st.number_input("Loan Amount ($)", min_value=1000, value=10000, step=1000)
    annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, max_value=50.0, value=5.0, step=0.1)
    loan_term_years = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=5, step=1)
    
    if st.button("Calculate Monthly Payment"):
        monthly_interest_rate = annual_interest_rate / 100 / 12
        num_payments = loan_term_years * 12
        monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_payments)
        st.success(f"Your Monthly Payment: ${monthly_payment:,.2f}")
        total_payment = monthly_payment * num_payments
        st.info(f"Total Amount Paid Over the Loan Term: ${total_payment:,.2f}")

# 3. Investment Growth Calculator
elif calculator == "Investment Growth":
    st.header("Investment Growth Calculator")
    
    # Input fields
    initial_investment = st.number_input("Initial Investment ($)", min_value=0, value=1000, step=100)
    monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, value=200, step=50)
    annual_return_rate = st.number_input("Expected Annual Return Rate (%)", min_value=0.0, max_value=20.0, value=8.0, step=0.1)
    investment_period_years = st.number_input("Investment Period (Years)", min_value=1, max_value=50, value=20, step=1)
    
    if st.button("Calculate Investment Growth"):
        total_investment = initial_investment
        for _ in range(investment_period_years * 12):
            total_investment += monthly_contribution
            total_investment *= (1 + annual_return_rate / 100 / 12)
        st.success(f"Future Value of Investment: ${total_investment:,.2f}")

# Footer
st.sidebar.write("Financial calculators to help you plan for your future.")
