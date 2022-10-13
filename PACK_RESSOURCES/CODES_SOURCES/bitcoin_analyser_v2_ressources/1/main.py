from datetime import date, datetime, timedelta
from rates_data_manager import get_and_manage_rates_data
import matplotlib.pyplot as plt
from rates_data_processing import *

date_start = date(2016, 1, 1)
#date_end = date(2020, 5, 6)
date_end = date.today()-timedelta(1)
assets = "BTC/EUR"

rates = get_and_manage_rates_data(assets, date_start, date_end)
print("nb rates:", len(rates))

ma200 = compute_moving_average_for_rates_data(rates, 100)

# rates <- date / value
rates_dates = [datetime.strptime(r["date"], "%Y-%m-%d") for r in rates]
rates_values = [r["value"] for r in rates]
plt.ylabel(assets)
plt.plot(rates_dates, rates_values)  # <--- valeurs
plt.show()

