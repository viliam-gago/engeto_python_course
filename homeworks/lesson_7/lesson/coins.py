def change_coins(amount):
    values = [50, 20, 10, 5, 2, 1]
    coins = dict()

    for key in values:
        while key <= amount:
            amount -= key
            coins[key] = coins.setdefault(key, 0) + 1
    return coins

print(change_coins(124))