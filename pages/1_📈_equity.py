import streamlit as st
from datetime import date
import numpy as np
import pandas as pd
from jugaad_data.nse import bhavcopy_save, stock_df

st.set_page_config(page_title="Equity", page_icon="📈")

st.markdown("# Equities")
st.sidebar.header("Equity")

# bhavcopy_save(date(2020,1,1), "./")

bhavcopy_df = pd.read_csv("cm01Jan2020bhav.csv")
ticker = bhavcopy_df[bhavcopy_df['SERIES']=='EQ']['SYMBOL']

selected_ticker = st.multiselect("Please Select the Tickers", ticker)

start_date = st.date_input("Pick a Start Date")
end_date = st.date_input("Pick End Date", date.today())

df = stock_df(symbol=selected_ticker, from_date=start_date, to_date=end_date, series='EQ')

# st.write(df.head())

st.line_chart(df, x='DATE', y='CLOSE')