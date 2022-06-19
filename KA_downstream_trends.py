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
                current_date = datetime.strptime(row[0],'%Y/%m/%d')
                indivisual = float(row[1])
                company = float(row[2])               
            except ValueError:
                print(current_date,'missing data')
            else:
                indivisuals.append(indivisual)
                companies.append(company)
                dates.append(current_date)
# Get KA data.
indivisuals,companies,dates = [],[],[]
get_price_data('KA_downstream_trends.csv')
# Plot KA data.
fig = plt.figure(dpi=128,figsize=(15,6))
plt.plot(dates,indivisuals,c='red',alpha =0.5)
plt.plot(dates,companies,c='blue',alpha=0.5)
plt.fill_between(dates,indivisuals,companies,facecolor ='blue',alpha=0.1)
# Set format.

plt.title('KA cost trend',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Price per kilometre',fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=6)
plt.show()

