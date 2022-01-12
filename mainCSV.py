'''
Are there differences in activity patterns between weekdays and weekends?

1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.

2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).

NOTES: I want to clarify that I did not do this code alone and I had the help of a friend, Richie. I was not able to figure this out myself and had copied his code. But I also want to clarify that
I try to understand the code as well.

'''
#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read the csv file
df = pd.read_csv('D:\BINUS\Algorithm\dataVis\dataActivity.csv')

#convert to datetime format
df['date'] = pd.to_datetime(df['date'])

#clarifies which column is weekday and weekend
df['weekday'] = np.where(df['date'].dt.dayofweek < 5, 'weekday', 'weekend')

#returns the first n rows to only display the amount of n rows stated here
df.head(1500)

#group the weekday data into a weekday column
weekday = df.groupby('weekday')
weekday = weekday.get_group('weekday')

#group the weekend data into a weekend column
weekend = df.groupby('weekday')
weekend = weekend.get_group('weekend')

#Creating both the Weekday and Weekend Graph
weekday[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekday")
weekend[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekend")

#show the graph(s)
plt.show()