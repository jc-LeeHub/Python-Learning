import csv

from matplotlib import pyplot as plt
from datetime import datetime

#创建一个阅读器存储读取的首行csv信息
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [], [], []
    #遍历每一行，提取最高、最低温度以及日期
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data!')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#可视化
fig = plt.figure(dpi=128, figsize=(10, 6))


plt.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
plt.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

