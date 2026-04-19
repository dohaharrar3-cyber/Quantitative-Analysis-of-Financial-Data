import yfinance as yf 
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
tickers=["JPM","AAPL","MSFT"]
data=yf.download(tickers,start="2022-01-01",end="2024-01-01",group_by="tickers")
all_data=[]
for date in data.index:
    for ticker in tickers : 
        all_data.append({"Date":date , 
                         "Ticker":ticker , 
                         "Close":data[ticker]["Close"].loc[date]
                        })
df=pd.DataFrame(all_data)
print(df.head())        
