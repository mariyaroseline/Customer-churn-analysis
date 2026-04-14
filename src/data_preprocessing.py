import pandas as pd

def load_data(path):
    #Load dataset
    return pd.read_csv(r"data\Telco-Customer-Churn.csv")

def clean_data(df):
    #Handle missing values
    
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Drop missing values
    df.dropna(inplace=True)
    
    # Remove unnecessary column
    df.drop('customerID', axis=1, inplace=True)
    
    return df

def encode_data(df):
    #Encode categorical data
    
    # Convert target variable
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Convert categorical features
    df = pd.get_dummies(df, drop_first=True)
    
    return df

def preprocess(path):
    df = load_data(path)
    df = clean_data(df)
    df = encode_data(df)
    return df