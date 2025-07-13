#1. Libraries and data acquisition
#First, install the necessary libraries:
#pandas: For data manipulation.
#yfinance: To fetch historical stock data.
#matplotlib: For plotting and visualization.
#numpy: For numerical operations. 

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Fetch historical stock data for a given ticker symbol
def get_stock_data(symbol, period="1y"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df

# Example: Get Apple (AAPL) stock data
df = get_stock_data("AAPL", period="1y")




#2. Calculating the moving average and its slope
#Next, calculate the moving average and its slope to identify potential trends. 

# Calculate a Simple Moving Average (SMA)
def calculate_moving_average(df, window=5):
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

# Calculate the slope of the moving average
def calculate_moving_average_slope(df, window=5):
    df = calculate_moving_average(df, window)
    df[f'SMA_{window}_Slope'] = np.degrees(np.arctan((df[f'SMA_{window}'] - df[f'SMA_{window}'].shift(window)) / window)) # Using arctan for slope in degrees, {Link: according to Stack Overflow https://stackoverflow.com/questions/71225951/how-to-create-a-column-that-returns-the-slope-of-a-moving-average}
    return df

# Apply moving average and slope calculation
df = calculate_moving_average_slope(df, window=5) # Using a 50-day SMA for this example
df = df.dropna() # Remove rows with NaN values resulting from the rolling average calculation, {Link: according to Medium https://medium.com/coinmonks/python-stock-analysis-with-20-50-day-moving-averages-de72ff9fa3b3}

#3. Generating trading signals
#Trading signals can be generated based on the slope of the moving average. A positive slope could indicate an uptrend (buy signal), while a negative slope could indicate a downtrend (sell signal). You might also define thresholds for the slope to trigger these signals. 
def generate_signals_from_slope(df, window=5, slope_threshold=5): # Define a slope threshold
    df['Signal'] = 0  # Initialize signal column
    df.loc[df[f'SMA_{window}_Slope'] > slope_threshold, 'Signal'] = 1  # Buy signal
    df.loc[df[f'SMA_{window}_Slope'] < -slope_threshold, 'Signal'] = -1  # Sell signal
    return df

df = generate_signals_from_slope(df, window=5, slope_threshold=5)

import numpy as np
from scipy.signal import find_peaks

plt.plot(df.index, df[f'SMA_5'], label='5-day SMA', alpha=0.8)

df2=df[f'SMA_5']
# Convert dates to numerical values (e.g., timestamps or simply an integer range)
# For simplicity, using an integer range for x-axis
time = np.arange(len(df2))
data = df[f'SMA_5']

# Find peaks (local maxima)
peaks_indices, _ = find_peaks(data, prominence=3) # Adjust prominence as needed
min_value = data.min()
max_value = data.max()


# Find peaks (local maxima)
peaks_indices, _ = find_peaks(data.values, prominence=3) # Adjust prominence as needed
peaks_values = data.iloc[peaks_indices]

# Find valleys (local minima) by finding peaks in the inverted series
valleys_indices, _ = find_peaks(-data.values, prominence=3)
valleys_values = data.iloc[valleys_indices]

# Calculate the slope (derivative)
#slope = np.diff(data.values) / np.diff(data.index.values)
slope = np.diff(data) / np.diff(time)

# The slope array will be one element shorter than the time series
# Align it with the original time_series for plotting
slope_time_points = data.index.values[:-1]


plt.figure(figsize=(12, 6))

# Plot the original time series
plt.plot(data.index, data.values, label='Time Series')

# Plot global min and max
plt.axhline(y=min_value, color='orange', linestyle='--', label='Global Min')
plt.axhline(y=max_value, color='red', linestyle='--', label='Global Max')

# Plot peaks and valleys
plt.plot(peaks_values.index, peaks_values.values, "o", color='green', markersize=8, label='Peaks')
plt.plot(valleys_values.index, valleys_values.values, "o", color='purple', markersize=8, label='Valleys')

plt.title('Time Series with Min, Max, Peaks, and Valleys')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


# Concatenate the Series
concatenated_series = pd.concat([peaks_values, valleys_values])

# Sort the concatenated Series by index
sorted_series = concatenated_series.sort_index()

print("Original Series 1:")
print(peaks_values)
print("\nOriginal Series 2:")
print(valleys_values)
print("\nConcatenated Series (unsorted):")
print(concatenated_series)
print("\nConcatenated Series (sorted by index):")
print(sorted_series)


# Calculate the difference with default periods=1
diff_s = sorted_series.diff(periods=-1)
print("Difference with periods=1:\n", diff_s)

# Calculate the difference with periods=2
#diff_s_periods_2 = sorted_series.diff(periods=2)
#print("\nDifference with periods=2:\n", diff_s_periods_2)

# Calculate the difference with periods=-1 (difference with the next element)
#diff_s_periods_neg_1 = sorted_series.diff(periods=-1)
#print("\nDifference with periods=-1:\n", diff_s_periods_neg_1)



#4. Visualization
#Visualize the stock price, moving average, and the generated trading signals to observe the strategy in action. 

def plot_slope_strategy(df, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['Close'], label='Close Price', alpha=0.8)
    plt.plot(df.index, df[f'SMA_5'], label='5-day SMA', alpha=0.8)
    
    # Plotting buy and sell signals
    plt.scatter(df[df['Signal'] == 1].index, df[df['Signal'] == 1]['Close'], 
                marker='^', color='green', s=100, label='Buy Signal')
    plt.scatter(df[df['Signal'] == -1].index, df[df['Signal'] == -1]['Close'], 
                marker='v', color='red', s=100, label='Sell Signal')

    plt.title(f'{symbol} Stock Price with Moving Average Slope Signals')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

plot_slope_strategy(df, "AAPL")
