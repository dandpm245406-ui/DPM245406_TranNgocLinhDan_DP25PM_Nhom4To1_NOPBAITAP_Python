while True:
    n = int(input("Nhập 1 số nguyên dương: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương!")
        continue

    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1

    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không là số nguyên tố")

    hoi = input("Tiếp không? (c/k): ")
    if hoi == "k":
        break

print("BYE!")
