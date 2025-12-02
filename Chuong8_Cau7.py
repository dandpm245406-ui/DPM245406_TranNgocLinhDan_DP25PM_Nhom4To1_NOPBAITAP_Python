from tkinter import *

# Thiên Can
can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
# Địa Chi
chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def chuyen_am_lich():
    try:
        nam_duong = int(entryYear.get())
        can_index = (nam_duong + 6) % 10  # Quy ước: năm 2020 là Canh Tý
        chi_index = (nam_duong + 8) % 12  # Quy ước: năm 2020 là Canh Tý
        stringResult.set(f"Năm Âm lịch: {can[can_index]} {chi[chi_index]}")
    except ValueError:
        stringResult.set("Vui lòng nhập số hợp lệ!")

# ====== Giao diện ======
root = Tk()
root.title("Chuyển Năm Dương → Âm Lịch")
root.geometry("350x150")
root.resizable(False, False)

Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack(pady=10)
entryYear = Entry(root, width=20, font=("Arial", 12))
entryYear.pack()

Button(root, text="Chuyển sang Âm lịch", command=chuyen_am_lich).pack(pady=10)

stringResult = StringVar()
Label(root, textvariable=stringResult, font=("Arial", 12), fg="blue").pack(pady=5)

root.mainloop()
