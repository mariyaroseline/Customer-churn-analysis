Telecom Customer Churn Analysis and Prediction

Overview  
This project analyzes and predicts customer churn in a telecom company using data analytics, machine learning, and interactive visualization. It combines exploratory data analysis, predictive modeling, and dashboarding to provide actionable insights for improving customer retention.

Business Problem  
Customer churn leads to significant revenue loss in the telecom industry. Identifying customers who are likely to churn and understanding the factors influencing their behavior enables organizations to take proactive retention measures.

Objectives  
- Perform exploratory data analysis to identify churn patterns  
- Build a machine learning model to predict customer churn  
- Identify key factors influencing churn  
- Develop an interactive dashboard for business insights  
- Create a Streamlit application for real-time predictions

Methodology  

1. Data Collection  
Customer dataset including demographics, usage patterns, and churn status  

2. Data Preprocessing  
- Handled missing values  
- Encoded categorical variables  

3. Data Storage  
- Stored processed data in MySQL database  

4. Exploratory Data Analysis (EDA)  
- Analyzed churn distribution  
- Identified customer behavior patterns  

5. Statistical Analysis  
- Evaluated correlation between features and churn  

6. Data Visualization  
- Created bar charts and plots for churn vs features  

7. Feature Selection  
- Selected important features influencing churn  

8. Model Building  
- Applied Logistic Regression using Scikit-learn  

9. Prediction  
- Predicted customer churn (Yes/No)  

10. Insights  
- Derived key factors responsible for customer churn   

Tools and Technologies  
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- SQL (MySQL)  
- Power BI  
- Streamlit  

Project Structure  

Customer-Churn-Analysis/
data/  
notebooks/  
sql/  
src/  
models/  
dashboard/  
requirements.txt  
README.md  

Machine Learning Model  
A classification model was built using Scikit-learn to predict whether a customer is likely to churn.  
- Data preprocessing and feature engineering were applied  
- Model training and evaluation were performed  
- The trained model is saved as a pickle file for reuse  

Streamlit Application  
A Streamlit web application was developed to provide an interactive interface where users can input customer details and get real-time churn predictions.

To run the app:  
streamlit run src/app.py  

Key Insights  
- The overall churn rate is 27 percent, indicating moderate customer attrition  
- Customers with month-to-month contracts have the highest churn risk  
- Customers with low tenure are more likely to churn  
- Fiber optic service users show higher churn compared to DSL users  

Dashboard Description  
The Power BI dashboard provides:  
- KPI metrics (total customers, churned customers, churn rate)  
- Customer distribution and segmentation analysis  
- Churn trends based on tenure and monthly charges  
- Churn drivers analysis using Power BI Decomposition Tree (AI-based visual)  
- Business insights for decision-making  

How to Run the Project  

1. Clone the repository  
2. Install dependencies:  
   pip install -r requirements.txt  
3. Run Python scripts from the src folder  
4. Launch Streamlit app:  
   streamlit run src/app.py  
5. Open the Power BI dashboard file (.pbix) in Power BI Desktop  

Future Enhancements  
- Improve model accuracy using advanced algorithms  
- Deploy the application on cloud platforms  
- Integrate real-time data sources  
- Enhance UI/UX of the Streamlit app  

Author  
Mariya Roseline A
