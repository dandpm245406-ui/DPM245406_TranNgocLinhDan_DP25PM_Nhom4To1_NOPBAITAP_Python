def ToiUuChuoiDanhTu(s):
    # Xóa khoảng trắng dư và tách thành các từ
    words = s.strip().split()

    # Viết hoa ký tự đầu và viết thường phần còn lại
    words = [w.capitalize() for w in words]

    # Ghép lại thành chuỗi hoàn chỉnh
    return " ".join(words)


# Ví dụ chạy
s = "   TRần    duY   thAnH   "
print(ToiUuChuoiDanhTu(s))
