import xml.etree.ElementTree as ET
from collections import defaultdict

# ===== Đọc danh sách nhóm thiết bị =====
def read_nhom(filename="nhomthietbi.xml"):
    tree = ET.parse(filename)
    root = tree.getroot()
    nhoms = {}
    for nhom in root.findall("nhom"):
        ma = nhom.find("ma").text
        ten = nhom.find("ten").text
        nhoms[ma] = ten
    return nhoms

# ===== Đọc danh sách thiết bị =====
def read_thietbi(filename="ThietBi.xml"):
    tree = ET.parse(filename)
    root = tree.getroot()
    thietbis = []
    for tb in root.findall("thietbi"):
        manhom = tb.get("manhom")
        ma = tb.find("ma").text
        ten = tb.find("ten").text
        thietbis.append({"ma": ma, "ten": ten, "manhom": manhom})
    return thietbis

# ===== Hiển thị danh sách nhóm =====
def hien_thi_nhom(nhoms):
    print("\nDanh sách Nhóm thiết bị:")
    for ma, ten in nhoms.items():
        print(f"{ma} - {ten}")

# ===== Hiển thị toàn bộ thiết bị =====
def hien_thi_thietbi(thietbis, nhoms):
    print("\nDanh sách Thiết bị:")
    for tb in thietbis:
        ten_nhom = nhoms.get(tb["manhom"], "Không xác định")
        print(f"{tb['ma']} | {tb['ten']} | Nhóm: {ten_nhom}")

# ===== Lọc thiết bị theo nhóm =====
def loc_theo_nhom(thietbis, nhoms):
    ma_nhom = input("Nhập mã nhóm cần lọc: ")
    if ma_nhom not in nhoms:
        print("Không tìm thấy nhóm!")
        return
    print(f"\nThiết bị thuộc nhóm {nhoms[ma_nhom]}:")
    for tb in thietbis:
        if tb["manhom"] == ma_nhom:
            print(f"{tb['ma']} | {tb['ten']}")

# ===== Nhóm có nhiều thiết bị nhất =====
def nhom_nhieu_thietbi_nhat(thietbis, nhoms):
    count = defaultdict(int)
    for tb in thietbis:
        count[tb["manhom"]] += 1
    if not count:
        print("Không có thiết bị nào!")
        return
    max_count = max(count.values())
    nhoms_max = [nhoms[ma] for ma, c in count.items() if c == max_count]
    print("\nNhóm thiết bị có số lượng nhiều nhất:")
    for ten in nhoms_max:
        print(f"{ten} ({max_count} thiết bị)")

# ===== Main Menu =====
def main():
    nhoms = read_nhom()
    thietbis = read_thietbi()

    while True:
        print("\n===== QUẢN LÝ THIẾT BỊ =====")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc Thiết bị theo Nhóm thiết bị")
        print("4. Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất")
        print("0. Thoát")
        choice = input("Chọn: ")
        if choice == "1":
            hien_thi_nhom(nhoms)
        elif choice == "2":
            hien_thi_thietbi(thietbis, nhoms)
        elif choice == "3":
            loc_theo_nhom(thietbis, nhoms)
        elif choice == "4":
            nhom_nhieu_thietbi_nhat(thietbis, nhoms)
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
