import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.write("""
# Simple Stock Price App
         
Shown are the stock **closing price** and **volume** of NVIDIA!
             
""")

# Define the ticker symbol
tickerSymbol = 'NVDA'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2022-01-01', end=datetime.now().strftime('%Y-%m-%d'))
# Open High Low Close Volume Dividends Stock Splits

# Calculate moving averages
tickerDF['50_MA'] = tickerDF['Close'].rolling(window=50).mean()
tickerDF['200_MA'] = tickerDF['Close'].rolling(window=200).mean()

# Check for current trend
last_close = tickerDF['Close'].iloc[-1]
last_50_ma = tickerDF['50_MA'].iloc[-1]
last_200_ma = tickerDF['200_MA'].iloc[-1]

# Determine recommendation and prediction
if last_close > last_50_ma > last_200_ma:
    recommendation = "**Buy your stock today!**"
    prediction = None
elif last_50_ma > last_200_ma:
    recommendation = "Wait for a dip, then buy."
    # Predict when to check back
    next_dip_date = datetime.now() + timedelta(days=7)
    prediction = f"Check back around {next_dip_date.strftime('%Y-%m-%d')} for a potential buying opportunity."
else:
    recommendation = "Wait for a clearer trend."
    # Predict when to check back
    next_trend_date = datetime.now() + timedelta(weeks=2)
    prediction = f"Check back around {next_trend_date.strftime('%Y-%m-%d')} for a clearer trend."

st.write("### Recommendation:", recommendation)
if prediction:
    st.write("### Prediction:", prediction)

st.write("""
## Stock Price Chart Explanation:

This chart displays the historical closing prices of NVIDIA stock over the selected time period. 

- **Closing Price**: The blue line shows the daily closing prices of NVIDIA stock. It represents the price at which the stock traded at the end of each trading day.

Users can analyze the stock's performance by observing trends, crossovers between moving averages, and overall volatility.

""")


st.write("""
## Stock Price Chart
""")

st.line_chart(tickerDF.Close)

st.write("""
## Volume Price Chart
""")
st.line_chart(tickerDF.Volume)

