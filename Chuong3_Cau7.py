def nam_nhuan(nam):
    # Năm nhuận nếu chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def ngay_ke_sau(ngay, thang, nam):
    # Số ngày trong từng tháng
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        ngay_max = 31
    elif thang in [4, 6, 9, 11]:
        ngay_max = 30
    elif thang == 2:
        if nam_nhuan(nam):
            ngay_max = 29
        else:
            ngay_max = 28
    else:
        return None  # Tháng không hợp lệ
    
    # Tính ngày kế tiếp
    if ngay < ngay_max:
        ngay += 1
    else:
        ngay = 1
        if thang == 12:
            thang = 1
            nam += 1
        else:
            thang += 1
    
    return ngay, thang, nam

# Nhập ngày tháng năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra ngày hợp lệ đơn giản
def ngay_hop_le(ngay, thang, nam):
    if thang < 1 or thang > 12:
        return False
    if ngay < 1:
        return False
    if thang in [1,3,5,7,8,10,12]:
        return ngay <= 31
    elif thang in [4,6,9,11]:
        return ngay <= 30
    elif thang == 2:
        if nam_nhuan(nam):
            return ngay <= 29
        else:
            return ngay <= 28
    else:
        return False

if ngay_hop_le(ngay, thang, nam):
    ngay_moi = ngay_ke_sau(ngay, thang, nam)
    if ngay_moi:
        print(f"Ngày kế sau là: {ngay_moi[0]}/{ngay_moi[1]}/{ngay_moi[2]}")
    else:
        print("Ngày hoặc tháng không hợp lệ.")
else:
    print("Ngày nhập không hợp lệ.")