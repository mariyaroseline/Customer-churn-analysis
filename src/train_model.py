from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

def train(df):
    #Feature selection
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    #Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    #Apply Logistic Regression
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)
    
    #Prediction
    y_pred = model.predict(X_test)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    
    return model

def save_model(model):
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)