import random
import csv

# ===== Hàm tạo CSV =====
def tao_csv(filename="data.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):
            row = [random.randint(0, 100) for _ in range(10)]
            writer.writerow(row)
    print(f"Tạo file {filename} thành công!")

# ===== Hàm đọc CSV và tính tổng =====
def doc_va_tong(filename="data.csv"):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f, delimiter=';')
            for i, row in enumerate(reader, 1):
                numbers = [int(x) for x in row]
                print(f"Dòng {i}: {numbers} -> Tổng = {sum(numbers)}")
    except FileNotFoundError:
        print(f"File {filename} không tồn tại!")

# ===== Main =====
if __name__ == "__main__":
    tao_csv()          # Tạo file CSV với 10x10 số ngẫu nhiên
    print("\nĐọc file và tính tổng từng dòng:")
    doc_va_tong()
