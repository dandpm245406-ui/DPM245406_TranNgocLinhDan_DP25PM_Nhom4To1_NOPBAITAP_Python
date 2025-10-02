n, m = 0, 100

while True:
    n = int(input("Nhập số nguyên: "))
    if n < 0 or n == m:
        break
    print("n =", n)
