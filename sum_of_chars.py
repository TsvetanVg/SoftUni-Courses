numbers_of_lines = int(input())
sum = 0
for i in range(numbers_of_lines):
    char = ord(input())
    sum += char
print(f"The sum equals: {sum}")
