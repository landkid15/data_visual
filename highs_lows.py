import csv
from matplotlib import pyplot as plt
from datetime import datetime
def get_weather_data(filename):
    """从文件中获取日期、最高气温、最低气温"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)     
        for row in reader:
            try:
                high = int(row[1])
                low = int(row[3])
                current_date = datetime.strptime(row[0],'%Y-%m-%d')
            except ValueError:
                print(current_date,'missing data')
            else:
                highs.append(high)
                lows.append(low)
                dates.append(current_date)
# Get weather data for Sitka.
dates,highs,lows =[],[],[]
get_weather_data('sitka_weather_2014.csv')
# Plot Sitka weather data.
fig =plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, highs,c='red',alpha=0.5)
plt.plot(dates, lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# Get weather data for Death Valley
dates,highs,lows =[],[],[]
get_weather_data('death_valley_2014.csv')
# Plot Death Valley weather data.
plt.plot(dates, highs,c='red',alpha=0.3)
plt.plot(dates, lows,c='blue',alpha=0.3)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.08)
# Set format.
plt.title('High and low tempratures - 2014\n Sitka, AK and Death Valley, CA',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temprature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()