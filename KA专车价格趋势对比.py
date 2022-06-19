# KA专车价格趋势对比
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
                ka_upstream = float(row[1])
                ka_downstream = float(row[2])
                zc_upstream = float(row[3])
                zc_downstream = float(row[4])
                current_date = datetime.strptime(row[0],'%Y/%m/%d')
            except ValueError:
                print(current_date,'missing data')
            else:
                ka_upstreams.append(ka_upstream)
                ka_downstreams.append(ka_downstream)
                zc_upstreams.append(zc_upstream)
                zc_downstreams.append(zc_downstream)
                dates.append(current_date)
# Get data.
ka_upstreams,ka_downstreams,zc_upstreams,zc_downstreams,dates = [],[],[],[],[]
get_price_data('foryou_price_2021.csv')
# Plot KA data.
fig = plt.figure(dpi=128,figsize=(15,6))
plt.plot(dates,ka_upstreams,c='red',alpha =0.5)
plt.plot(dates,ka_downstreams,c='red',alpha =0.3)
plt.plot(dates,zc_upstreams,c='blue',alpha=0.5)
plt.plot(dates,zc_downstreams,c='blue',alpha=0.3)
plt.fill_between(dates,ka_upstreams,ka_downstreams,facecolor ='red',alpha=0.1)
plt.fill_between(dates,zc_upstreams,zc_downstreams,facecolor ='blue',alpha=0.1)
# Set format.

plt.title('Price trend',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Price per kilometre',fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=6)
plt.show()

