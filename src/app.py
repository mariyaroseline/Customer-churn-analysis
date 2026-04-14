import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(page_title="Churn Dashboard", layout="wide")

# Custom CSS 
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Load Model
model = pickle.load(open("models/model.pkl", "rb"))

# Header
st.title("Customer Churn Prediction Dashboard")
st.markdown("### Analyze customer behavior & predict churn risk")

# Sidebar Input
st.sidebar.header("Customer Input")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1000.0)

contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("Internet", ["DSL", "Fiber optic", "No"])

# Prepare Data
data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total]
})

data["Contract_One year"] = 1 if contract == "One year" else 0
data["Contract_Two year"] = 1 if contract == "Two year" else 0
data["InternetService_Fiber optic"] = 1 if internet == "Fiber optic" else 0
data["InternetService_No"] = 1 if internet == "No" else 0

for col in model.feature_names_in_:
    if col not in data:
        data[col] = 0

data = data[model.feature_names_in_]

# Predict
col1, col2, col3 = st.columns(3)

if st.button("Predict Churn"):

    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    # KPI Cards
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Churn Probability</h3>
            <h2>{prob:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Tenure</h3>
            <h2>{tenure} Months</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Monthly Charges</h3>
            <h2>{monthly}</h2>
        </div>
        """, unsafe_allow_html=True)

    # Result Message
    st.markdown("---")

    if pred == 1:
        st.error("High Risk: Customer likely to churn")
    else:
        st.success("Low Risk: Customer likely to stay")

    # Insights
    st.markdown("### Business Insights")

    if prob > 0.7:
        st.warning("High churn risk due to short tenure or high charges.")
    elif prob > 0.4:
        st.info("Moderate risk. Customer engagement recommended.")
    else:
        st.success("Customer is stable with low churn risk.")

# Footer
st.markdown("---")
st.caption("Built with Machine Learning | Logistic Regression")