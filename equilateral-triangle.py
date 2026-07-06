def draw_equilateral_triangle():
    tall = int(input("Enter how tall you want the triangle: "))

    for i in range(tall):
        empty_space = " " * (tall - i - 1)
        hash_marks = "*" * (2 * i + 1)
        print(empty_space + hash_marks)


if __name__ == "__main__":
    draw_equilateral_triangle()
