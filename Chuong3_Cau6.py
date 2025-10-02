def doc_so(n):
    so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    if n < 10:
        return so[n]
    else:
        hang_chuc = n // 10
        hang_dv = n % 10
        
        # Đọc hàng chục
        if hang_chuc == 1:
            ket_qua = "mười"
        else:
            ket_qua = so[hang_chuc] + " mươi"
        
        # Đọc hàng đơn vị
        if hang_dv == 0:
            return ket_qua
        elif hang_dv == 1:
            # Nếu hàng chục > 1 thì đọc là "mốt"
            if hang_chuc > 1:
                ket_qua += " mốt"
            else:
                ket_qua += " một"
        elif hang_dv == 5:
            # Nếu hàng chục >= 1 thì đọc là "lăm"
            if hang_chuc >= 1:
                ket_qua += " lăm"
            else:
                ket_qua += " năm"
        else:
            ket_qua += " " + so[hang_dv]
        
        return ket_qua

# Ví dụ sử dụng
n = int(input("Nhập số n (0-99): "))
if 0 <= n <= 99:
    print(doc_so(n))
else:
    print("Vui lòng nhập số trong khoảng từ 0 đến 99.")