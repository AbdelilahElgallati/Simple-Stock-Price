import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Stock Price Analysis App
         
Shown are the stock **closing** price and **volume** of Google!         
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data of this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# open high low close volume dividends stock splits
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)