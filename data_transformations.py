from app_requests import get_request
from DBConnectors import DBConnectors
import pandas as pd
from pandas import json_normalize
from sqlalchemy import create_engine

def create_df(url):
    data=get_request(url)
    df= json_normalize(data, sep='_')
    return df

def data_cleaning(df):
    df.fillna(value={'roi_times':0,'roi_currency':'N/A','roi_percentage':0},inplace=True)
    df['current_price']=df['current_price'].astype(float).round(2)
    df['market_data_market_cap'] = df['market_cap'].astype(float).round(2)
    df['market_data_circulating_supply'] = df['circulating_supply'].astype(float).round(2)
    df['market_data_total_supply'] = df['total_supply'].astype(float).round(2)
    df['roi_times'] = df['roi_times'].astype(float)
    df['roi_percentage'] = df['roi_percentage'].astype(float)
    # Standardize string formats (e.g., converting all strings to lowercase)
    df['name'] = df['name'].str.title()
    df['symbol'] = df['symbol'].str.upper()
    # Drop duplicate rows if there are any
    df.drop_duplicates(inplace=True)
    df.rename(columns={
        'market_data_market_cap': 'market_cap',
        'market_data_market_cap_rank': 'market_cap_rank',
        'market_data_circulating_supply': 'circulating_supply',
        'market_data_total_supply': 'total_supply'
    }, inplace=True)
    df['ath_date'] = pd.to_datetime(df['ath_date'])
    df['atl_date'] = pd.to_datetime(df['atl_date'])
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df_cleaned = df.dropna(axis=1, how='all')
    pd.set_option('display.max_columns', None)
    df_cleaned.to_csv('cleaned_data.csv', index=False)
    # print(df_cleaned.head(3))
    return df_cleaned

def load_to_mysql(df_cleaned):
    new_engine=DBConnectors()
    engine=new_engine.create_mysql_engine()
    table_name='CoinsData'
    df_cleaned.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Data successfully written to table '{table_name}' in MySQL database.")

if __name__=='__main__':
    df=create_df(url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    # df=create_df(url=' https://jsonplaceholder.typicode.com/users')
    # df_cleaned=data_cleaning(df)
    # load_to_mysql(df_cleaned)
    data_cleaning(df)