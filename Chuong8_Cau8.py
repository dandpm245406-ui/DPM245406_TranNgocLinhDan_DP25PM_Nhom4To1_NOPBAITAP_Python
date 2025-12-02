from tkinter import *

def chuyenF_C():
    try:
        f = float(entryF.get())
        c = (f - 32) * 5 / 9
        stringResult.set(f"{f}°F = {c:.2f}°C")
    except ValueError:
        stringResult.set("Vui lòng nhập số hợp lệ!")

def xoa():
    entryF.delete(0, END)
    stringResult.set("")

# ====== Giao diện ======
root = Tk()
root.title("Chuyển Độ F → C")
root.geometry("300x150")
root.resizable(False, False)

Label(root, text="Nhập nhiệt độ (°F):", font=("Arial", 12)).pack(pady=10)
entryF = Entry(root, width=20, font=("Arial", 12))
entryF.pack()

Button(root, text="Chuyển sang °C", command=chuyenF_C).pack(pady=5)
Button(root, text="Xóa", command=xoa).pack(pady=5)

stringResult = StringVar()
Label(root, textvariable=stringResult, font=("Arial", 12), fg="blue").pack(pady=5)

root.mainloop()
