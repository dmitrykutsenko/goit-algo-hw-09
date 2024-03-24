# all is about greedy

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    coin_count = {}
    remaining_amount = amount
    
    for coin in coins:
        if remaining_amount <= 0:
            break
        coin_count[coin] = remaining_amount // coin
        remaining_amount %= coin

    return {k: v for k, v in coin_count.items() if v > 0}


def find_min_coins(amount):
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми
    min_coins = [0] + [float('inf')] * amount

    # Обчислення мінімальної кількості монет для кожної суми
    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1

    # Відновлення кількості монет кожного номіналу
    coin_count = {}
    i = amount
    while i > 0:
        for coin in coins:
            # if min_coins[i] == min_coins[i - coin] + 1: # by S
            if i >= coin and min_coins[i] == min_coins[i - coin] + 1:
                coin_count[coin] = coin_count.get(coin, 0) + 1
                i -= coin
                break

    return coin_count


def compare_results():
    matches = 0
    mismatches = 0

    for amount in range(1, 1001):
        greedy_result = find_coins_greedy(amount)
        dynamic_result = find_min_coins(amount)

        if greedy_result == dynamic_result:
            matches += 1
        else:
            mismatches += 1

    print("Кількість співпадінь результатів двох алгоритмів в діапазоні від 1коп. до 1000 коп.:  ", matches)
    print("Кількість НЕспівпадінь результатів двох алгоритмів в діапазоні від 1коп. до 1000 коп.:", mismatches)

compare_results()


def main():
    # Запитуємо у користувача суму решти
    while True:
        # Введення значення для пошуку
        amount = input("Введіть цілочислену суму решти в копійках (або exit для виходу): ")

        # Перевірка на exit
        if amount.lower() == "exit":
            break
        else:
            # Перевірка, чи введено число
            try:
                # Перетворення введеного значення в int
                amount = int(amount)
            except ValueError:
                print("Введено невірне значення. Спробуйте ще раз.")
                continue

        # 1. Жадібні результати
        result_greedy = find_coins_greedy(amount)
        print("Згідно Жадібного алгоритму маємо - Кількість монет по номіналам:", result_greedy)

        # 2. Динамічні результати
        result_dm = find_min_coins(amount)
        print("Згідно Динамічного програмування - Кількість монет по номіналам:", result_dm)
              
        print("Чи рівні результати:", result_greedy == result_dm)
        print()  # Пустий рядок для розділення виводу між тестами


if (__name__ == "__main__") or (__name__ == "__hw_09__"):
    main()
