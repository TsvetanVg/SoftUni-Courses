group_size = int(input())
days = int(input())

spend_coins = 0
party = True
for i in range(1, days + 1):

    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    spend_coins += 50
    spend_coins -= 2 * group_size
    if i % 5 == 0 and i % 3 == 0:
        spend_coins -= 2 * group_size
    if i % 3 == 0:
        spend_coins -= 3 * group_size
    if i % 5 == 0:
        spend_coins += 20 * group_size

total_coins_each_companion = spend_coins // group_size

print(f"{group_size} companions received {total_coins_each_companion} coins each.")
