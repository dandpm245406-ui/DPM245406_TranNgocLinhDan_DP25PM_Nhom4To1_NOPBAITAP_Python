from tkinter import *

def tinh_BMI():
    try:
        cannang = float(entryWeight.get())
        chieucao = float(entryHeight.get())
        if chieucao <= 0:
            stringResult.set("Chiều cao phải > 0")
            return
        bmi = cannang / (chieucao ** 2)
        # Xác định mức BMI
        if bmi < 18.5:
            muc = "Thiếu cân"
        elif bmi < 24.9:
            muc = "Bình thường"
        elif bmi < 29.9:
            muc = "Thừa cân"
        else:
            muc = "Béo phì"
        stringResult.set(f"BMI = {bmi:.2f} → {muc}")
    except ValueError:
        stringResult.set("Vui lòng nhập số hợp lệ!")

def xoa():
    entryWeight.delete(0, END)
    entryHeight.delete(0, END)
    stringResult.set("")

# ====== Giao diện ======
root = Tk()
root.title("BMI Calculator")
root.geometry("350x200")
root.resizable(False, False)

Label(root, text="Chỉ số BMI", font=("Arial", 16), fg="blue").pack(pady=10)

# Nhập cân nặng
frameWeight = Frame(root)
Label(frameWeight, text="Cân nặng (kg):", width=15, anchor=W).pack(side=LEFT)
entryWeight = Entry(frameWeight, width=15)
entryWeight.pack(side=LEFT)
frameWeight.pack(pady=5)

# Nhập chiều cao
frameHeight = Frame(root)
Label(frameHeight, text="Chiều cao (m):", width=15, anchor=W).pack(side=LEFT)
entryHeight = Entry(frameHeight, width=15)
entryHeight.pack(side=LEFT)
frameHeight.pack(pady=5)

# Nút
frameButton = Frame(root)
Button(frameButton, text="Tính BMI", width=12, command=tinh_BMI).pack(side=LEFT, padx=5)
Button(frameButton, text="Xóa", width=12, command=xoa).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", width=12, command=root.quit).pack(side=LEFT, padx=5)
frameButton.pack(pady=10)

# Kết quả
stringResult = StringVar()
Label(root, textvariable=stringResult, font=("Arial", 12), fg="red").pack(pady=5)

root.mainloop()
