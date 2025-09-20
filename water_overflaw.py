
number_of_lines = int(input())
capacity_of_tank = 255
sum_of_liters = 0
for i in range(0, number_of_lines):
    aded_liters = int(input())
    sum_of_liters += aded_liters

    if sum_of_liters > capacity_of_tank:
        print(f"Insufficient capacity!")
        sum_of_liters -= aded_liters


print(sum_of_liters)