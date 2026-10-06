a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

is_triangle = (a < b + c) and (b < a + c) and (c < a + b)

print(is_triangle)