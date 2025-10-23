import math

a = float(input("Nhập giá trị a: "))
n = int(input("Nhập số lần lồng căn n: "))

# Biến chứa kết quả
y = 0

# Tính từ trong ra ngoài
for i in range(n):
    y = math.sqrt(a + y)

print(f"Giá trị biểu thức căn bậc 2 lồng nhau {n} lần là: {y:.6f}")
