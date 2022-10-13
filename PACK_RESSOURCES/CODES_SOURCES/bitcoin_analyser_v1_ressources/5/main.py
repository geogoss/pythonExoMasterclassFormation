
from coinapi_service import coin_api_get_exchange_rates

assets = "BTC/EUR"
rates = coin_api_get_exchange_rates(assets, "2021-02-01", "2021-02-10")

if rates:
    print(assets + ", nombre de cours:", len(rates))
    for r in rates:
        print(r["time_period_start"][:10], ":", r["rate_close"])
# .time_period_start    :     rate_close
# 2021-01-01 : 24032.11824302815
# 2021-01-02 : 24032.11824302815