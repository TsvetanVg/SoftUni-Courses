snowballs = int(input())
best_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for i in range(1, snowballs + 1):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight_of_snowball // time_needed) ** quality

    if best_value < value:
        best_value = value
        snowball_weight =weight_of_snowball
        snowball_time = time_needed
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {best_value} ({snowball_quality})")