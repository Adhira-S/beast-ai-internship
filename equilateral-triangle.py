height = 5

for i in range(height):
    spaces = " " * (height - i - 1)
    hashes = "#" * (2 * i + 1)
    print(spaces + hashes)
