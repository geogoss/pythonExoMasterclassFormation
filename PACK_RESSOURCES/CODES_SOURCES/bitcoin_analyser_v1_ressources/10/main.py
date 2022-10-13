from datetime import date, datetime, timedelta
from coinapi_service import coin_api_get_exchange_rates
import json
from os import path

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

date_end = date.today()
date_end_str = date_end.strftime("%Y-%m-%d")

date_start = date_end - timedelta(10)
date_start_str = date_start.strftime("%Y-%m-%d")

assets = "BTC/EUR"

data_filename = assets.replace("/", "_") + ".json"


def load_json_data_from_file(filename):
    f = open(filename, "r")
    json_data = f.read()
    f.close()
    return json_data


def save_json_data_to_file(filename, json_data):
    f = open(filename, "w")
    f.write(json_data)
    f.close()


def get_json_rates(rates_data):
    rates_json = []
    for r in rates_data:
        rates_json.append({"date": r["time_period_start"][:10], "value": r["rate_close"] })
    return json.dumps(rates_json)


# date_start / date_end : date objects
# max_days : int
# start : 1/1/2021
# End : 27/5/2021
# -> [[1/1/2021, 10/04/2021], [11/04/2021, 27/5/2021]]
def get_dates_intervals(date_start, date_end, max_days):
    diff = date_end-date_start
    diff_days = diff.days
    dates_intervals = []
    interval_begin_date = date_start
    while diff_days > 0:
        nb_days_to_add = max_days-1
        if diff_days < max_days-1:
            nb_days_to_add = diff_days
        interval_end_date = interval_begin_date + timedelta(nb_days_to_add)
        dates_intervals.append([interval_begin_date, interval_end_date])
        diff_days -= nb_days_to_add+1
        interval_begin_date = interval_end_date + timedelta(1)

    return dates_intervals


# config : date debut / date fin / assets
# 1 - lire fichier json (si il existe)
#     date_debut / date_fin
# - fichier existe
# - saved_data_date_start / saved_data_date_end
# - load_json_data_from_file(...) -> json
rates = []
if path.exists(data_filename):
    # le fichier json existe
    json_rates = load_json_data_from_file(data_filename)
    rates = json.loads(json_rates)

if len(rates) > 0:
    saved_data_date_start_str = rates[0]["date"]
    saved_data_date_end_str = rates[-1]["date"]
    print("saved_data_date_start_str", saved_data_date_start_str)
    print("saved_data_date_end_str", saved_data_date_end_str)
    # Fichier json existe -> [ date_start/saved_data_date_start ] ... [date_end/saved_data_date_end]
    # 3 - faire les appels à l'api (avant / après)  <--- passer la limite des 100 jours
    # 4 - Consolider les données (mettre à jour le fichier json)
else:
    # Fichier json n'existe pas ou pas de data -> [date_start / date_end]
    # 3 - faire les appels à l'api (avant / après)  <--- passer la limite des 100 jours
    # 4 - Consolider les données (mettre à jour le fichier json)
    pass

print(get_dates_intervals(date(2021, 1, 1), date(2021, 5, 27), 100))

rates = coin_api_get_exchange_rates(assets, "2021-01-01", "2021-04-11")
print()
'''print("Date start", date_start_str)
print("Date end", date_end_str)


rates = coin_api_get_exchange_rates(assets, date_start_str, date_end_str)

if rates:
    json = get_json_rates(rates)
    save_json_data_to_file(data_filename, json)
    print(json)
    print(assets + ", nombre de cours:", len(rates))
    for r in rates:
        print(r["time_period_start"][:10], ":", r["rate_close"])
'''