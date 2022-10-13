




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


def compute_buy_and_sell_points_from_ma(short_ma, long_ma):
    buy_mode = True
    points = []
    # [("date_str", buy_mode)]  # buy_mode = True (achat) / False (vente)
    for i in range(len(short_ma)):
        date_str = short_ma[i]["date"]
        sma_value = short_ma[i]["value"]
        lma_value = long_ma[i]["value"]
        if buy_mode:  # on cherche un point d'achat
            if sma_value > lma_value:
                points.append((date_str, buy_mode))
                buy_mode = False
        else:
            if sma_value < lma_value:
                points.append((date_str, buy_mode))
                buy_mode = True
    return points


