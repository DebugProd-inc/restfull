from test_values import implementation_values

# проверка функциональности ВС
# сравнение расстояния от геометрического центра с максимальным
# если расстояние меньше или равно допустимому, то оно
# записывается в доспустимые значения


def functional_check(distance, mu_max):
    if max(distance) <= mu_max:
        implementation_values(distance)
        return True
    else:
        return False
