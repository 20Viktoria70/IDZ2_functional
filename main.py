import streamlit as st
import plotly.express as px

from data import load_data, log_returns, normalize

st.set_page_config(page_title="Financial Time Series", layout="wide")

st.title("📈 Financial Time Series Analysis")

df = load_data()

st.subheader("Raw market data")
st.dataframe(df.head())

st.subheader("Descriptive statistics")
st.dataframe(df.describe().T)

returns = log_returns(df)

st.subheader("Log returns")
st.dataframe(returns.head())

fig = px.line(returns, title="Log Returns")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Normalized log returns")
st.dataframe(normalize(returns).head())
