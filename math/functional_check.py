# проверка функциональности ВС
# сравнение расстояния от геометрического центра с максимальным


def functional_check(distance, mu_max):
    if distance <= mu_max:
        return True
    else:
        return False
