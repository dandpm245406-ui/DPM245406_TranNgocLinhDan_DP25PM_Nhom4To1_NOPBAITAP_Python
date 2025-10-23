import math

# Nhập tọa độ hai điểm A và B
xA = float(input("Nhập hoành độ điểm A: "))
yA = float(input("Nhập tung độ điểm A: "))
xB = float(input("Nhập hoành độ điểm B: "))
yB = float(input("Nhập tung độ điểm B: "))

# Tính độ dài đoạn AB
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Xuất kết quả
print(f"Độ dài đoạn AB là: {AB:.2f}")
