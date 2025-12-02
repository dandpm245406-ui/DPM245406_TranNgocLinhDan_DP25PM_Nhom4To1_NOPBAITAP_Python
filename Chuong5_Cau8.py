import os

# Lấy tên file đầy đủ (ví dụ: muabui.mp3)
def get_filename(path):
    return os.path.basename(path)

# Lấy tên file không có phần mở rộng (ví dụ: muabui)
def get_filename_no_ext(path):
    return os.path.splitext(os.path.basename(path))[0]


# --- Ví dụ chạy ---
path = r"d:\music\muabui.mp3"

print(get_filename(path))         # → muabui.mp3
print(get_filename_no_ext(path))  # → muabui
