import csv
from tkinter.ttk import LabeledScale
from matplotlib import pyplot as plt
from datetime import datetime
def get_price_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
       
        for row in reader:
            try:
                upstream = float(row[1])
                downstream = float(row[2])
                current_date = datetime.strptime(row[0],'%Y/%m/%d')
            except ValueError:
                print(current_date,'missing data')
            else:
                upstreams.append(upstream)
                downstreams.append(downstream)
                dates.append(current_date)
# Get KA data.
upstreams,downstreams,dates = [],[],[]
get_price_data('KA_price_2021.csv')
# Plot KA data.
fig = plt.figure(dpi=128,figsize=(15,6))
plt.plot(dates,upstreams,c='red',alpha =0.5)
plt.plot(dates,downstreams,c='blue',alpha=0.5)
plt.fill_between(dates,upstreams,downstreams,facecolor ='blue',alpha=0.1)
# Set format.

plt.title('KA price trend',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Price per kilometre',fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=6)
plt.show()

