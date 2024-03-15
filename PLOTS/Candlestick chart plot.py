import yfinance as yf
import mplfinance as mpf
# Define the stock symbol and data range
symbol = input("Enter stock name : ")
start_date = '2011-01-01'
end_date = '2023-10-13'

# Fetch stock data
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Create the candlestick chart
mpf.plot(stock_data, type='candle', style='yahoo', title=f'{symbol} Candlestick Chart')
