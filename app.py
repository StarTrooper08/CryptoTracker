#import libs

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

crypto_mapping = {"Bitcoin":"BTC-USD","Ethereum":"ETH-USD"}


#streamlit app title

st.title("Crypto Tracker")
st.image("header.png", width=900)

#sidebar
crypto_option = st.sidebar.selectbox(
    "Which Crypto currency do you want to visualize?",("Bitcoin","Ethereum")
)

#start and end date for tracking value
start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(month=1))
end_date = st.sidebar.date_input("End Date", date.today())


data_interval = st.sidebar.selectbox(

"Data Interval",
{
    "1m",
    "2m",
    "5m",
    "15m",
    "30m",
    "60m",
    "90m",
    "1h",
    "1d",
    "5d",
    "1wk",
    "1mo",
    "3mo",
},

)

symbol_crypto = crypto_mapping[crypto_option]

data_crypto = yf.Ticker(symbol_crypto)

value_selector = st.sidebar.selectbox(
    "Value Selector", ("Open","High","Low","Close","Volume")
)

if st.sidebar.button("Generate"):
    crypto_hist = data_crypto.history(
        start=start_date, end=end_date, interval=data_interval
    )

    fig = px.line(crypto_hist,
    x = crypto_hist.index,y=value_selector,
    labels={"x":"Date"})
    st.plotly_chart(fig)