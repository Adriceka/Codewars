def loose_change(cents):
    cents = int(cents)

    coin_keys = ['Pennies', 'Nickels', 'Dimes', 'Quarters']
    coin_values = [1, 5, 10, 25]

    wallet = dict(zip(coin_keys, coin_values))
    coins = sorted(wallet.values())

    change = []
    coins_available = len(coins) - 1

    while cents > 0 and coins_available >= 0:
        if cents >= coins[coins_available]:
            cents -= coins[coins_available]
            change.append(coins[coins_available])
        else:
            coins_available -= 1

    change_dict = dict.fromkeys(coin_keys, 0)
    value_to_name = {v: k for k, v in wallet.items()}

    for coin in change:
        change_dict[value_to_name[coin]] += 1

    return change_dict

if __name__ == '__main__':
    assert loose_change(29) ==  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) ==  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) ==   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}