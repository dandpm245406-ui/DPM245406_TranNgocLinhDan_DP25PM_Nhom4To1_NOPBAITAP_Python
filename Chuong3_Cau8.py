# Nhập 2 số a và b
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập phép toán
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# Thực hiện phép toán
if phep_toan == '+':
    ket_qua = a + b
elif phep_toan == '-':
    ket_qua = a - b
elif phep_toan == '*':
    ket_qua = a * b
elif phep_toan == '/':
    if b != 0:
        ket_qua = a / b
    else:
        ket_qua = "Lỗi: Không thể chia cho 0"
else:
    ket_qua = "Phép toán không hợp lệ!"

# In kết quả
print("Kết quả:", ket_qua)
                            