import pandas as pd
import os

# File Excel để lưu dữ liệu
FILENAME = "nhanvien.xlsx"

# ====== Hàm thêm nhân viên ======
def add_employee():
    code = input("Nhập mã nhân viên: ")
    name = input("Nhập tên nhân viên: ")
    age = int(input("Nhập tuổi nhân viên: "))
    
    # Kiểm tra file đã tồn tại chưa
    if os.path.exists(FILENAME):
        df = pd.read_excel(FILENAME)
    else:
        df = pd.DataFrame(columns=["Mã", "Tên", "Tuổi"])
    
    # Thêm nhân viên mới
    df = pd.concat([df, pd.DataFrame({"Mã":[code], "Tên":[name], "Tuổi":[age]})], ignore_index=True)
    df.to_excel(FILENAME, index=False)
    print("Thêm nhân viên thành công!")

# ====== Hàm đọc danh sách nhân viên ======
def read_employees():
    if not os.path.exists(FILENAME):
        print("Chưa có dữ liệu.")
        return
    df = pd.read_excel(FILENAME)
    print("\nDanh sách nhân viên:")
    print(df)

# ====== Hàm sắp xếp nhân viên theo tuổi ======
def sort_employees_by_age():
    if not os.path.exists(FILENAME):
        print("Chưa có dữ liệu.")
        return
    df = pd.read_excel(FILENAME)
    df_sorted = df.sort_values(by="Tuổi", ascending=True)
    print("\nDanh sách nhân viên theo tuổi tăng dần:")
    print(df_sorted)

# ====== Menu chính ======
def main():
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1. Thêm nhân viên")
        print("2. Xem danh sách nhân viên")
        print("3. Sắp xếp nhân viên theo tuổi")
        print("0. Thoát")
        choice = input("Chọn: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            sort_employees_by_age()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
