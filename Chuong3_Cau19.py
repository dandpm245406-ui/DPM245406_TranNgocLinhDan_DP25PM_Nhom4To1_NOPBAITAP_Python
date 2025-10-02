def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def calculate_s(x, n):
    result = 0
    for i in range(n + 1):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

if __name__ == "__main__":
    x = float(input("Nhập x: "))
    n = int(input("Nhập n: "))
    print(f"S({x}, {n}) = {calculate_s(x, n)}")
