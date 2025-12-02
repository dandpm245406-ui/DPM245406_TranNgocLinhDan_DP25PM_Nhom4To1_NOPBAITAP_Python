from tkinter import *

# ====== Hàm tính toán ======
def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia cho 0")
        else:
            stringKQ.set(a / b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ")

# ====== Giao diện ======
root = Tk()
root.title("Máy tính Cộng – Trừ – Nhân – Chia")
root.minsize(height=200, width=300)

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

Label(root, text="Cộng Trừ Nhân Chia", fg="blue", font=("Tahoma", 16)).grid(row=0, columnspan=3, pady=10)

# Khung chứa các nút
frameButton = Frame(root)
Button(frameButton, text="Cộng", width=10, command=congAction).pack(pady=2, fill=X)
Button(frameButton, text="Trừ", width=10, command=truAction).pack(pady=2, fill=X)
Button(frameButton, text="Nhân", width=10, command=nhanAction).pack(pady=2, fill=X)
Button(frameButton, text="Chia", width=10, command=chiaAction).pack(pady=2, fill=X)
frameButton.grid(row=1, column=0, rowspan=4, padx=10)

# Nhập số a và số b
Label(root, text="Số a:").grid(row=1, column=1, sticky=W, padx=5)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2, padx=5)

Label(root, text="Số b:").grid(row=2, column=1, sticky=W, padx=5)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2, padx=5)

# Kết quả
Label(root, text="Kết quả:").grid(row=3, column=1, sticky=W, padx=5)
Entry(root, width=15, textvariable=stringKQ, state='readonly').grid(row=3, column=2, padx=5)

# Nút thoát
Button(root, text="Thoát", width=10, command=root.quit).grid(row=4, column=2, pady=5)

root.mainloop()
