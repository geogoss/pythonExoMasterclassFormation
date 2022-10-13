from datetime import date, datetime, timedelta
from coinapi_service import coin_api_get_exchange_rates

'''
date1 = date.today() # date du jour
#date2 = date1 + timedelta(10)  # additionner / soustraire des jours
date3 = date(2021, 1, 30)
diff = date1-date3
# print(diff.days)
date3_str = date3.strftime("%d/%m/%Y")  # Y (Years)  m (months)  d (days)

date4 = datetime.strptime("2021-02-01", "%Y-%m-%d").date()
date4 += timedelta(1)
print(date4)
'''

date_today = date.today()
date_today_str = date_today.strftime("%Y-%m-%d")

date_start = date_today - timedelta(10)
date_start_str = date_start.strftime("%Y-%m-%d")

print("Date start", date_start_str)
print("Date end", date_today_str)

assets = "BTC/EUR"
rates = coin_api_get_exchange_rates(assets, date_start_str, date_today_str)

if rates:
    print(assets + ", nombre de cours:", len(rates))
    for r in rates:
        print(r["time_period_start"][:10], ":", r["rate_close"])


# .time_period_start    :     rate_close
# 2021-01-01 : 24032.11824302815
# 2021-01-02 : 24032.11824302815