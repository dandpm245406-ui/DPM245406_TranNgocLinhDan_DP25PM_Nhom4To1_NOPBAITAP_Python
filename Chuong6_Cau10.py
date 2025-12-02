# Hàm nhập ma trận
def nhap_matrix(name):
    rows = int(input(f"Nhập số dòng của ma trận {name}: "))
    cols = int(input(f"Nhập số cột của ma trận {name}: "))
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Nhập dòng {i+1} của {name} (cách nhau bằng space): ").split()))
                if len(row) != cols:
                    print(f"Số phần tử phải bằng {cols}, nhập lại!")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Nhập không hợp lệ, vui lòng nhập số.")
    return matrix

# Hàm cộng 2 ma trận
def cong_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Hàm tính ma trận chuyển vị
def chuyen_vi(M):
    return [list(row) for row in zip(*M)]

# Hàm in ma trận
def in_matrix(M):
    for row in M:
        print(row)

# --- Main ---
print("Nhập ma trận A:")
A = nhap_matrix("A")

print("\nNhập ma trận B:")
B = nhap_matrix("B")

# Cộng 2 ma trận nếu cùng kích thước
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("\nKhông thể cộng 2 ma trận do kích thước khác nhau!")
else:
    C = cong_matrix(A, B)
    print("\nMa trận A + B là:")
    in_matrix(C)

# Chuyển vị ma trận A và B
print("\nChuyển vị ma trận A:")
in_matrix(chuyen_vi(A))

print("\nChuyển vị ma trận B:")
in_matrix(chuyen_vi(B))
