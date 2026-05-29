#top three items in shop
shop = {
    'item1': 45.50,
    'item2': 35,
    'item3': 41.30,
    'item4': 55,
    'item5': 24
}

sorted_items = sorted(shop.items(),
                      key=lambda x: x[1],
                      reverse=True)

for item, price in sorted_items[:3]:
    print(item, price)