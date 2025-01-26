import streamlit as st

# Define the color scheme
PRIMARY_COLOR = "#FFB4FF"
SECONDARY_COLOR = "#F7D9F4"
TERTIARY_COLOR = "#DCD8F3"
ACCENT_COLOR = "#C5C0F7"
HIGHLIGHT_COLOR = "#CE3971"

# Custom Streamlit style
st.markdown(
    f"""
    <style>
        /* Background for the entire app */
        .stApp {{
            background-color: {HIGHLIGHT_COLOR};
        }}
        
        /* Customize buttons */
        .stButton > button {{
            background-color: {PRIMARY_COLOR};
            color: black;
            border-radius: 8px;
            border: 2px solid {ACCENT_COLOR};
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
        }}
        
        /* Hover effect for buttons */
        .stButton > button:hover {{
            background-color: {ACCENT_COLOR};
            color: white;
        }}
        
        /* Text headers */
        h1 {{
            color: {HIGHLIGHT_COLOR};
            font-family: Arial, sans-serif;
        }}
        
        h2 {{
            color: {HIGHLIGHT_COLOR};
            font-family: Arial, sans-serif;
        }}
        
        /* Sliders */
        .stSlider {{
            background-color: {TERTIARY_COLOR};
            border-radius: 10px;
        }}
        
        /* Subheader and other texts */
        .stMarkdown p {{
            color: black;
            font-family: Arial, sans-serif;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.title("Financial Planning Calculator")

# Create the toggle for calculators
option = st.radio(
    "Select a Calculator",
    ("Retirement Savings", "Loan Repayment", "Investment Growth"),
    horizontal=True,
    index=0,
)

if option == "Retirement Savings":
    st.header("Retirement Savings Calculator")

    current_age = st.slider("Current Age:", 18, 65, 30)
    retirement_age = st.slider("Retirement Age:", 40, 70, 65)
    current_savings = st.number_input("Current Savings ($):", min_value=0.0, value=10000.0, step=1000.0)
    monthly_contribution = st.number_input("Monthly Contribution ($):", min_value=0.0, value=500.0, step=100.0)
    annual_return = st.slider("Expected Annual Return (%):", 0.0, 15.0, 5.0)

    years_to_retirement = retirement_age - current_age
    future_value = current_savings * (1 + annual_return / 100) ** years_to_retirement + \
                   monthly_contribution * (((1 + annual_return / 100) ** years_to_retirement - 1) / (annual_return / 100))

    st.subheader(f"Estimated Savings by Retirement: ${future_value:,.2f}")

elif option == "Loan Repayment":
    st.header("Loan Repayment Calculator")

    loan_amount = st.number_input("Loan Amount ($):", min_value=0.0, value=20000.0, step=1000.0)
    annual_interest = st.slider("Annual Interest Rate (%):", 0.0, 20.0, 5.0)
    loan_term = st.slider("Loan Term (Years):", 1, 30, 10)

    monthly_interest = annual_interest / 100 / 12
    num_payments = loan_term * 12
    if monthly_interest > 0:
        monthly_payment = loan_amount * (monthly_interest * (1 + monthly_interest) ** num_payments) / (
            (1 + monthly_interest) ** num_payments - 1)
    else:
        monthly_payment = loan_amount / num_payments

    st.subheader(f"Monthly Payment: ${monthly_payment:,.2f}")

elif option == "Investment Growth":
    st.header("Investment Growth Calculator")

    initial_investment = st.number_input("Initial Investment ($):", min_value=0.0, value=10000.0, step=1000.0)
    annual_contribution = st.number_input("Annual Contribution ($):", min_value=0.0, value=5000.0, step=500.0)
    annual_growth_rate = st.slider("Expected Annual Growth Rate (%):", 0.0, 20.0, 7.0)
    investment_period = st.slider("Investment Period (Years):", 1, 40, 20)

    future_value = initial_investment * (1 + annual_growth_rate / 100) ** investment_period + \
                   annual_contribution * (((1 + annual_growth_rate / 100) ** investment_period - 1) / (annual_growth_rate / 100))

    st.subheader(f"Estimated Investment Value: ${future_value:,.2f}")
