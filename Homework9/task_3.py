# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    goods = []
    good_price = 0
    for price in file.readlines():
        if price.isspace():
            goods.append(good_price)
            good_price = 0
            continue
        good_price += int(price)
    goods.append(good_price)
    sorted_prices = sorted(goods, reverse=True)
    three_most_expensive_purchases = sum(sorted_prices[:3])

assert three_most_expensive_purchases == 202346
