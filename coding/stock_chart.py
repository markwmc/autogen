# filename: stock_chart.py
import pandas as pd
import matplotlib.pyplot as plt

# Read stock price data for NVDA and Tesla
nvda_url = "https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1609459200&period2=1640995199&interval=1d&events=history&includeAdjustedClose=true"
tesla_url = "https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1609459200&period2=1640995199&interval=1d&events=history&includeAdjustedClose=true"

nvda_df = pd.read_csv(nvda_url, index_col='Date', parse_dates=True, usecols=['Date', 'Close'])
tesla_df = pd.read_csv(tesla_url, index_col='Date', parse_dates=True, usecols=['Date', 'Close'])

# Plotting the chart
plt.figure(figsize=(12, 6))

plt.plot(nvda_df.index, nvda_df['Close'], label='NVDA')
plt.plot(tesla_df.index, tesla_df['Close'], label='TESLA')

plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('NVDA and TESLA Stock Price Change YTD')
plt.legend()

plt.show()