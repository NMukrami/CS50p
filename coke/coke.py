accepted_coins = [50, 25, 10, 5]
balance_coin = 50

while balance_coin > 0:
    print(f"Amount Due: {balance_coin}")
    inserted_coin = int(input("Insert Coin "))

    if inserted_coin in accepted_coins:
        balance_coin -= inserted_coin

if balance_coin < 0:
    print(f"Change Owed: {abs(balance_coin)}")
else:
    print(f"Change Owed: {balance_coin}")