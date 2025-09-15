while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue

    doubled = ""
    for char in text:
        doubled += char * 2
    print(doubled)
