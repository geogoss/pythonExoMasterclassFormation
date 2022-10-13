from datetime import date, datetime, timedelta
from coinapi_service import coin_api_get_exchange_rates_extended
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

date_start = date(2020, 1, 1)
date_end = date.today()-timedelta(1)
assets = "BTC/EUR"

data_filename = assets.replace("/", "_") + ".json"


def load_json_data_from_file(filename):
    f = open(filename, "r")
    json_data = f.read()
    f.close()
    return json_data


def save_rates_data_to_file(filename, rates_data):
    json_data = json.dumps(rates_data)
    f = open(filename, "w")
    f.write(json_data)
    f.close()


def convert_rates_to_date_value_format(rates_data):
    rates_date_value_format = []
    for r in rates_data:
        rates_date_value_format.append({"date": r["time_period_start"][:10], "value": r["rate_close"] })
    return rates_date_value_format


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
    print("Le fichier json existe")
    print("  saved_data_date_start_str", saved_data_date_start_str)
    print("  saved_data_date_end_str", saved_data_date_end_str)

    # - Convertir saved_data_date_start_str -> saved_data_date_start / saved_data_date_end_str -> saved_data_date_end
    saved_data_date_start = datetime.strptime(saved_data_date_start_str, "%Y-%m-%d").date()
    saved_data_date_end = datetime.strptime(saved_data_date_end_str, "%Y-%m-%d").date()

    nb_days_start = (saved_data_date_start-date_start).days

    if nb_days_start > 0:
        print("  on rajoute les données à gauche : ", date_start, saved_data_date_start-timedelta(1))
        rates_start = coin_api_get_exchange_rates_extended(assets, date_start, saved_data_date_start-timedelta(1))
        rates_start_date_value = convert_rates_to_date_value_format(rates_start)
        rates = rates_start_date_value + rates

    nb_days_end = (date_end-saved_data_date_end).days
    if nb_days_end > 0:
        print("  on rajoute les données à droite : ", saved_data_date_end + timedelta(1), date_end)
        rates_end = coin_api_get_exchange_rates_extended(assets, saved_data_date_end + timedelta(1), date_end)
        rates_end_date_value = convert_rates_to_date_value_format(rates_end)
        rates += rates_end_date_value

    save_rates_data_to_file(data_filename, rates)
else:
    rates_api = coin_api_get_exchange_rates_extended(assets, date_start, date_end)
    rates = convert_rates_to_date_value_format(rates_api)
    save_rates_data_to_file(data_filename, rates)

# date_intervals = get_dates_intervals(date(2021, 1, 1), date(2021, 5, 27), 100)

# rates = coin_api_get_exchange_rates_extended(assets, date(2021, 1, 1), date(2021, 5, 27))
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