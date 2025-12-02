import random

# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Nhập khoảng giá trị cho số ngẫu nhiên (ví dụ 1 đến 100)
start = 1
end = 100

# Tạo list ngẫu nhiên không trùng nhau
if N > (end - start + 1):
    print("Không thể tạo N số khác nhau trong khoảng đã cho!")
else:
    lst = random.sample(range(start, end+1), N)
    print("List ngẫu nhiên không trùng nhau:", lst)
