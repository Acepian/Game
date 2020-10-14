import os
import pandas_datareader as pdr

df = pdr.get_data_tiingo('AAPL', api_key=os.getenv('TIINGO_API_KEY'))

print(df.head())


