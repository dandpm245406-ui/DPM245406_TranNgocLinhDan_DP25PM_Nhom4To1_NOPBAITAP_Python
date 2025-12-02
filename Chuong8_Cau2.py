from tkinter import *
from math import sqrt

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())
    except ValueError:
        stringKQ.set("Hệ số không hợp lệ")
        return

    if a == 0:  # Phương trình bậc 1: bx + c = 0
        if b == 0:
            if c == 0:
                stringKQ.set("Vô số nghiệm")
            else:
                stringKQ.set("Vô nghiệm")
        else:
            x = -c / b
            stringKQ.set(f"x = {x}")
    else:  # Phương trình bậc 2
        delta = b**2 - 4*a*c
        if delta < 0:
            stringKQ.set("Vô nghiệm")
        elif delta == 0:
            x = -b / (2*a)
            stringKQ.set(f"Nghiệm kép x1 = x2 = {x}")
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            stringKQ.set(f"x1 = {x1}; x2 = {x2}")

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# ====== Giao diện ======
root = Tk()
root.title("Giải phương trình bậc 2")
root.minsize(width=300, height=200)

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

Label(root, text="Phương Trình Bậc 2", fg="red", font=("Tahoma", 16)).grid(row=0, column=0, columnspan=2)

Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
Entry(root, width=25, textvariable=stringHSA).grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
Entry(root, width=25, textvariable=stringHSB).grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
Entry(root, width=25, textvariable=stringHSC).grid(row=3, column=1, padx=5, pady=5)

# Khung chứa nút
frameButton = Frame(root)
Button(frameButton, text="Giải", width=10, command=giaiAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp", width=10, command=tiepAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", width=10, command=root.quit).pack(side=LEFT, padx=5)
frameButton.grid(row=4, column=0, columnspan=2, pady=10)

Label(root, text="Kết quả:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
Entry(root, width=25, textvariable=stringKQ, state='readonly').grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
