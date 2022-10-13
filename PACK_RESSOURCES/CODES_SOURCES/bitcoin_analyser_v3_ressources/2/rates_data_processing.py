




def compute_moving_average_for_rates_data(rates, nb_days_interval):
    # 0 1 2 3 4 5 6 7 8 (index)   /  nb_days_interval = 3
    # 5 8 9 3 6 1 3 4 7 (valeurs)
    s = 0
    averages = []   # {"date" : ...date_str., "value": ..moyenne.. }

    for i in range(len(rates)):
        rate = rates[i]
        s += rate["value"]
        a = 0
        if i >= nb_days_interval:
            s -= rates[i-nb_days_interval]["value"]
            a = s / nb_days_interval
        else:
            a = s / (i+1)
        averages.append({"date": rate["date"], "value": a})

    return averages


def compute_buy_and_sell_points_from_ma(short_ma, long_ma, threshold_percent=0):
    buy_mode = True
    points = []
    # [("date_str", buy_mode)]  # buy_mode = True (achat) / False (vente)
    for i in range(len(short_ma)):
        date_str = short_ma[i]["date"]
        sma_value = short_ma[i]["value"]
        lma_value = long_ma[i]["value"]
        mult = 1+threshold_percent/100
        if buy_mode:  # on cherche un point d'achat

            # threshold_percent = 1
            # sma = 80
            # lma = 1000+threshold_percent*1000/100 = 1010

            if sma_value > lma_value*mult:
                points.append((date_str, buy_mode))
                buy_mode = False
        else:
            if sma_value < lma_value/mult:
                points.append((date_str, buy_mode))
                buy_mode = True
    return points


def get_rate_value_for_date_str(rates, date_str):
    for r in rates:
        if r["date"] == date_str:
            return r["value"]
    return None


def compute_buy_and_sell_gains(initial_wallet, rates, buy_and_sell_points):
    # itérer sur buy_and_sell_points
    # attention : terminer par un point de vente
    # connaitre la valeur du cours à une date donnée (get_rate_value_for_date_str)
    # current_wallet = 0  // correspond au portefeuille (argent)
    # shares = 0 // correspondent au nombre de bitcoin

    # Le 2019-02-19 J'achète pour 1000 euros de bitcoin
    # Le 2019-07-30 Je vend les bitcoins et je récupère 2499 euros

    current_wallet = initial_wallet
    shares = 0

    if buy_and_sell_points[-1][1]:
        buy_and_sell_points = buy_and_sell_points[:-1]

    for point in buy_and_sell_points:
        rate_value = get_rate_value_for_date_str(rates, point[0])
        if point[1]:  # achat
            print("Le", point[0] + ", j'achète pour", round(current_wallet), "euros de bitcoin")
            shares = current_wallet / rate_value
            current_wallet = 0

        else:
            current_wallet = shares * rate_value
            shares = 0
            print("Le", point[0] + ", je vend les bitcoins et je récupère", round(current_wallet), "euros")
            print()

    return current_wallet  # retourner le portefeuille final

