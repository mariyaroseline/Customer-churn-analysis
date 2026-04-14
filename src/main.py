from src.data_preprocessing import preprocess
from src.train_model import train, save_model
from src.store_mysql import store_data    

# Run preprocessing
df = preprocess(r"data\Telco-Customer-Churn.csv")

# Store preprocessed data in MySQL
store_data(df)

# Train model
model = train(df)

# Save model
save_model(model)
