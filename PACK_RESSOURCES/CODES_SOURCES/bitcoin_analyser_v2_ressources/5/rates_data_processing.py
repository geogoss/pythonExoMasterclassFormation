




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

