import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demo Button Styles")
root.geometry("400x300")

# ====== Label giải thích ======
ttk.Label(root, text="Các style Button trong Tkinter ttk", font=("Arial", 14)).pack(pady=10)

# ====== Tạo style và nút ======
style = ttk.Style()

# Lấy danh sách style mặc định
available_styles = style.theme_names()
print("Các theme có sẵn:", available_styles)

# Một số nút mẫu
frame = ttk.Frame(root)
frame.pack(pady=10)

# Style mặc định TButton
ttk.Button(frame, text="TButton (mặc định)").pack(pady=5)

# Thay đổi theme
for theme in available_styles:
    style.theme_use(theme)
    ttk.Label(frame, text=f"Theme: {theme}", foreground="blue").pack(pady=2)
    ttk.Button(frame, text="Button theo theme").pack(pady=2)

# Một số style khác (toolbutton, toggle)
style.configure("My.TButton", foreground="red", font=("Arial", 12, "bold"))
ttk.Button(frame, text="TButton custom", style="My.TButton").pack(pady=5)

root.mainloop()
