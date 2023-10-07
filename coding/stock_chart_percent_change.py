# filename: stock_chart_percent_change.py
import pandas as pd
import matplotlib.pyplot as plt

# Read stock price data for NVDA and Tesla
nvda_url = "https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1609459200&period2=1640995199&interval=1d&events=history&includeAdjustedClose=true"
tesla_url = "https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1609459200&period2=1640995199&interval=1d&events=history&includeAdjustedClose=true"

nvda_df = pd.read_csv(nvda_url, index_col='Date', parse_dates=True, usecols=['Date', 'Close'])
tesla_df = pd.read_csv(tesla_url, index_col='Date', parse_dates=True, usecols=['Date', 'Close'])

# Calculate percentage change
nvda_percent_change = nvda_df['Close'].pct_change() * 100
tesla_percent_change = tesla_df['Close'].pct_change() * 100

# Plotting the chart
plt.figure(figsize=(12, 6))

plt.plot(nvda_percent_change.index, nvda_percent_change, label='NVDA')
plt.plot(tesla_percent_change.index, tesla_percent_change, label='TESLA')

plt.xlabel('Date')
plt.ylabel('% Change')
plt.title('NVDA and TESLA Stock Price Percentage Change YTD')
plt.legend()

plt.show()