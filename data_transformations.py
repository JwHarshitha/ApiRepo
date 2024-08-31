from app_requests import get_request
from DBConnectors import DBConnectors
import pandas as pd
from pandas import json_normalize
from sqlalchemy.exc import SQLAlchemyError

def create_df(url):
    try:
        data=get_request(url)
        df= json_normalize(data, sep='_')
        df.to_csv('raw_data.csv', index=False)
        return df
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def data_cleaning(df):
    try:
        df.fillna(value={'roi_times':0,'roi_currency':'N/A','roi_percentage':0},inplace=True)
        df[['current_price', 'market_cap', 'circulating_supply', 'total_supply']] = df[['current_price', 'market_cap', 'circulating_supply', 'total_supply']].apply(lambda x: x.astype(float).round(2))
        df[['roi_times', 'roi_percentage']] = df[['roi_times', 'roi_percentage']].apply(lambda x: x.astype(float))
        # Standardize string formats (e.g., converting all strings to lowercase)
        df['name'] = df['name'].str.title()
        df['symbol'] = df['symbol'].str.upper()
        # Drop duplicate rows if there are any
        df.drop_duplicates(inplace=True)
        date_columns = ['ath_date', 'atl_date', 'last_updated']
        df[date_columns] = df[date_columns].apply(lambda x: pd.to_datetime(x))
        df_cleaned = df.dropna(axis=1, how='all')
        # pd.set_option('display.max_columns', None)
        # print(df_cleaned.head(3))
        return df_cleaned
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def load_to_csv(df_cleaned):
    try:
        df_cleaned.to_csv('cleaned_data.csv', index=False)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def load_to_mysql(df_cleaned,table_name='CoinsData'):
    try:
        new_engine=DBConnectors()
        engine=new_engine.create_mysql_engine()
        df_cleaned.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data successfully written to table '{table_name}' in MySQL database.")
    except SQLAlchemyError as e:
        print(f"An error occurred while writing to the MySQL database: {str(e)}")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__=='__main__':
    df=create_df(url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    # df=create_df(url=' https://jsonplaceholder.typicode.com/users')
    load_to_mysql(df, "CoinsData_raw")
    df_cleaned=data_cleaning(df)
    print(df_cleaned.columns)
    load_to_mysql(df_cleaned,"CoinsData_transformed")
    # data_cleaning(df)