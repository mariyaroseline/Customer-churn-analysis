from sqlalchemy import create_engine

def store_data(df):
    #Store data in MySQL
    
    engine = create_engine("mysql+pymysql://root:yourpassword@localhost/churn_db")
    
    df.to_sql("churn_table", con=engine, if_exists="replace", index=False)
    
    