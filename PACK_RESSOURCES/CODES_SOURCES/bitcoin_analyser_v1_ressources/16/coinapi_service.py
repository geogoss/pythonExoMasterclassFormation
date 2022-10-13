import requests
import json
from coinapi_config import API_KEY, BASE_URL
from datetime import date, datetime, timedelta
headers = {'X-CoinAPI-Key': API_KEY}


'''def coinapi_service_get_all_assets():
    url = BASE_URL + 'v1/assets'
    response = requests.get(url, headers=headers)

    # 200 / sinon afficher le code d'erreur
    if response.status_code == 200:
        print("L'appel à l'API a fonctionné")
        data = json.loads(response.text)
        nb_assets = len(data)
        # asset_id
        # name
        print("Nombre d'assets monétaires:", nb_assets)
        if nb_assets >= 10:
            for i in range(10):
                d = data[i]
                print(d["asset_id"] + ": " + d["name"])

        print()
        print("Quota restant:", response.headers["x-ratelimit-remaining"])
    else:
        # cas d'erreur
        print("L'appel à l'API a retourné une erreur:", response.status_code)
'''

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

# extended : start and end dates can be seperated more than 100 days
def coin_api_get_exchange_rates_extended(assets, start_date, end_date):
    rates = []
    dates_intervals = get_dates_intervals(start_date, end_date, 100)
    if len(dates_intervals) > 0:
        for i in dates_intervals:
            rates += coin_api_get_exchange_rates(assets, i[0], i[1])
    return rates


def coin_api_get_exchange_filtered_rates_extended(assets, start_date, end_date):
    rates = coin_api_get_exchange_rates_extended(assets, start_date, end_date)
    filtered_rates = filter_inconsistent_rate_values(rates)
    return filtered_rates

def rate_is_inconsistent(rate):
    # x10 / 10
    return False

def filter_inconsistent_rate_values(input_rates):
    if len(input_rates) < 2:
        return input_rates
    filtered_rates = []
    for i in range(len(input_rates)):
        r = input_rates[i]
        if rate_is_inconsistent(r):
            # prendre le jour précédent ou suivant
            reference_rate = None
            if i > 0:
                reference_rate = input_rates[i-1]
            else:
                reference_rate = input_rates[i+1]
            patched_rate = r
            patched_rate["rate_open"] = reference_rate["rate_open"]
            patched_rate["rate_close"] = reference_rate["rate_close"]
            patched_rate["rate_high"] = reference_rate["rate_high"]
            patched_rate["rate_low"] = reference_rate["rate_low"]
            filtered_rates.append(patched_rate)
        else:
            filtered_rates.append(r)

    return filtered_rates

# assets : str "BTC/EUR"
# start_date / end_date : date objets (inclusive)
def coin_api_get_exchange_rates(assets, start_date, end_date):
    # Bitcoin en euros
    # 1 jour
    # 1 janv 2021 -> 10 janv 2021
    # -> gestion erreurs
    # -> deserialiser
    # -> afficher tel quel
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = (end_date + timedelta(1)).strftime("%Y-%m-%d")

    url = BASE_URL + "v1/exchangerate/" +\
          assets + "/history?period_id=1DAY&time_start=" +\
          start_date_str + "T00:00:00&time_end=" + end_date_str + "T00:00:00"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("L'appel à l'API a fonctionné")
        data = json.loads(response.text)
        # print(data)
        print("Quota restant:", response.headers["x-ratelimit-remaining"])
        return data
    else:
        print("L'appel à l'API a retourné une erreur:", response.status_code)
        return None
