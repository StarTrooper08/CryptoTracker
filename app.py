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

#sidebar
crypto_option = st.sidebar.selectbox(
    "Which Crypto currency do you want to visualize?",("Bitcoin","Ethereum")
)

#start and end date for tracking value
start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(month=1))
end_date = st.sidebar.date_input("End Date", date.today())
