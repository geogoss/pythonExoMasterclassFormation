from datetime import date, datetime, timedelta
from rates_data_manager import get_and_manage_rates_data
import matplotlib.pyplot as plt
from rates_data_processing import *

date_start = date(2019, 1, 1)
date_end = date(2020, 7, 1)
# date_end = date.today()-timedelta(1)
assets = "BTC/EUR"

rates = get_and_manage_rates_data(assets, date_start, date_end)
print("nb rates:", len(rates))

ma_intervals = [10, 50]
ma_list = []

for interval in ma_intervals:
    ma = compute_moving_average_for_rates_data(rates, interval)
    ma_list.append((ma, interval))

buy_and_sell_points = compute_buy_and_sell_points_from_ma(ma_list[0][0], ma_list[1][0], 1)

# [(..adverages.., interval), (..adverages.., interval), (..adverages.., interval)]
# ma20 = compute_moving_average_for_rates_data(rates, 20)
# ma100 = compute_moving_average_for_rates_data(rates, 100)

# rates <- date / value
rates_dates = [datetime.strptime(r["date"], "%Y-%m-%d") for r in rates]
rates_values = [r["value"] for r in rates]
plt.ylabel(assets)
plt.plot(rates_dates, rates_values)  # <--- valeurs

for ma_item in ma_list:
    ma_values = [r["value"] for r in ma_item[0]]
    plt.plot(rates_dates, ma_values, label="MA" + str(ma_item[1]))

# r y
# plt.axvline(x=date(2020, 5, 1), color='y')
# buy_and_sell_points
# [0] date_str
# [1] true/false
#  plt.axvline(x=date(2020, 5, 1), color='y')
for point in buy_and_sell_points:
    date_obj = datetime.strptime(point[0], "%Y-%m-%d")
    plt.axvline(x=date_obj, color='r' if point[1] else 'y')

plt.legend()
plt.show()

