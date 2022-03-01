# My Code
def divide_coin(coin, amount):
    count, remain = divmod(amount, coin)

    return {
        "count": count,
        "remain": remain,
    }


if __name__ == "__main__":
    n = int(input("Input Money : "))
    coins = [500, 100, 50, 10]
    count = 0

    for i in range(0, len(coins)):
        coin = divide_coin(coin=coins[i], amount=n)
        count += coin["count"]
        money = coin["remain"]

    print(count)

    ##################

    # Answer Example
    n = 1260
    count = 0

    # 큰 단위의 화폐부터 차례대로 확인하기
    array = [500, 100, 50, 10]

    for coin in array:
        count += n / coin
        n %= coin

    print(count)
