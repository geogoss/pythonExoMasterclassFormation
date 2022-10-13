from datetime import date, datetime, timedelta
from rates_data_manager import get_and_manage_rates_data

date_start = date(2019, 1, 1)
date_end = date.today()-timedelta(1)
assets = "BTC/EUR"

rates = get_and_manage_rates_data(assets, date_start, date_end)
print("nb rates:", len(rates))
