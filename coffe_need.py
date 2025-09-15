count = 0
valid_commands = ["coding", "cat", "dog", "movie"]

while True:
    command = input()
    if command == "END":
        break

    if command.lower() not in valid_commands:
        continue

    if command.isupper():
        count += 2
    else:
        count += 1

if count >= 5:
    print("You need extra sleep")
else:
    print(count)
