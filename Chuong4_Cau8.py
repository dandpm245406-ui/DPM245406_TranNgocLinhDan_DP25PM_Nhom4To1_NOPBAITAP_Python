import math

# Nhập dữ liệu
x = float(input("Nhập giá trị x: "))
a = float(input("Nhập cơ số a: "))

# Kiểm tra điều kiện hợp lệ
if x > 0 and a > 0 and a != 1:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x:.4f}")
else:
    print("Lỗi: x > 0, a > 0 và a ≠ 1 để tính loga.")
