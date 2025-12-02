from tkinter import *

# ====== Hàm xử lý nhấn nút ======
def clickButton(value):
    current = stringDisplay.get()
    stringDisplay.set(current + str(value))

def clearDisplay():
    stringDisplay.set("")

def calculate():
    try:
        result = eval(stringDisplay.get())  # eval tính toán biểu thức
        stringDisplay.set(result)
    except:
        stringDisplay.set("Lỗi!")

# ====== Giao diện ======
root = Tk()
root.title("Simple Calculator")
root.resizable(False, False)

stringDisplay = StringVar()

# Entry hiển thị
Entry(root, textvariable=stringDisplay, font=("Arial", 20), bd=5, relief=RIDGE, justify=RIGHT).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Danh sách nút
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
    'C'
]

# Vẽ nút
row = 1
col = 0
for b in buttons:
    if b == "=":
        Button(root, text=b, width=5, height=2, font=("Arial", 15), command=calculate).grid(row=row, column=col, padx=3, pady=3)
    elif b == "C":
        Button(root, text=b, width=23, height=2, font=("Arial", 15), command=clearDisplay).grid(row=row, column=0, columnspan=4, padx=3, pady=3)
    else:
        Button(root, text=b, width=5, height=2, font=("Arial", 15), command=lambda x=b: clickButton(x)).grid(row=row, column=col, padx=3, pady=3)
    col +=1
    if col > 3:
        col = 0
        row +=1

root.mainloop()
