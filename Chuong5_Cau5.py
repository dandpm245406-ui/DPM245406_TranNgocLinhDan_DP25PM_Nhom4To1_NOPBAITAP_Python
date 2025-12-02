# Nhập chuỗi
s = input("Nhập chuỗi: ")

# Các biến đếm
hoa = thuong = so = dac_biet = khoang_trang = nguyen_am = phu_am = 0

# Tập nguyên âm (cả hoa và thường)
nguyen_am_set = "aeiouAEIOUáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựéèẻẽẹêếềểễệ"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch == " ":
        khoang_trang += 1
    else:
        dac_biet += 1

    # Kiểm tra nguyên âm và phụ âm
    if ch.lower() in nguyen_am_set:
        nguyen_am += 1
    elif ch.isalpha():  # là chữ nhưng không phải nguyên âm → phụ âm
        phu_am += 1

# Xuất kết quả
print("Số chữ in HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số ký tự đặc biệt:", dac_biet)
print("Số khoảng trắng:", khoang_trang)
print("Số chữ nguyên âm:", nguyen_am)
print("Số chữ phụ âm:", phu_am)
