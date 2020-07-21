import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('MSFT', '2016-01-01', '2020-01-01')

data.Close.plot()
plt.show()