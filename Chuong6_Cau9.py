import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Mảng cho sẵn
M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

# Danh sách kết quả
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nguyen_to = [x for x in M if is_prime(x)]
khong_nguyen_to = [x for x in M if not is_prime(x)]

# Xuất kết quả
print(f"Dòng 1 (số lẻ): {le} - Tổng cộng: {len(le)} số lẻ")
print(f"Dòng 2 (số chẵn): {chan} - Tổng cộng: {len(chan)} số chẵn")
print(f"Dòng 3 (số nguyên tố): {nguyen_to}")
print(f"Dòng 4 (không phải số nguyên tố): {khong_nguyen_to}")
