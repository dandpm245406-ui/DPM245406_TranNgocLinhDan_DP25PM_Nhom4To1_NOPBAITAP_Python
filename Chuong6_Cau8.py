# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

M = []

# Nhập từng số thực
for i in range(n):
    while True:
        try:
            num = float(input(f"M[{i}]: "))
            M.append(num)
            break
        except ValueError:
            print("Vui lòng nhập số thực hợp lệ!")

# Sắp xếp giảm dần
M.sort(reverse=True)

# In kết quả
print("Dãy số sau khi sắp xếp giảm dần:", M)
