def sum_divisors(n):
    """Tính tổng các ước số dương của n, không kể chính n."""
    s = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            s += i
    return s

def is_perfect(n):
    """Kiểm tra n có phải là số hoàn thiện không."""
    return sum_divisors(n) == n

def is_abundant(n):
    """Kiểm tra n có phải là số thịnh vượng không."""
    return sum_divisors(n) > n

# Ví dụ kiểm tra
n = 6
print(f"{n} là số hoàn thiện? {is_perfect(n)}")   # True

n = 12
print(f"{n} là số thịnh vượng? {is_abundant(n)}")  # True
