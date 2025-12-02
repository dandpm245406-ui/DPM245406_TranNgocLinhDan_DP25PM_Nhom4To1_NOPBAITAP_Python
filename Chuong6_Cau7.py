# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

numbers = []

print("Nhập dãy số theo thứ tự tăng:")

for i in range(N):
    while True:
        try:
            num = int(input(f"Số thứ {i+1}: "))
            # Kiểm tra thứ tự tăng
            if i == 0 or num > numbers[-1]:
                numbers.append(num)
                break
            else:
                print("Nhập sai, số phải lớn hơn số trước. Nhập lại!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

# In dãy số đã nhập
print("Dãy số theo thứ tự tăng là:", numbers)
