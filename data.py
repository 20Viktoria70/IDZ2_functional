import yfinance as yf
import pandas as pd
import numpy as np

def load_data(start="2015-01-01", end="2025-04-13"):
    tickers = {
        'IBM': 'IBM',
        'S&P500': '^GSPC',
        'Dow30': '^DJI',
        'Gold': 'GC=F',
        'CrudeOil': 'CL=F'
    }

    df = pd.DataFrame()

    for name, ticker in tickers.items():
        data = yf.download(ticker, start=start, end=end, progress=False)
        df[name] = data['Close']

    return df.dropna()


def log_returns(df: pd.DataFrame) -> pd.DataFrame:
    return np.log(df / df.shift(1)).dropna()


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    return (df - df.min()) / (df.max() - df.min())
