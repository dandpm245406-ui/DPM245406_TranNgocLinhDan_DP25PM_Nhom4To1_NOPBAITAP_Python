from tkinter import *
from tkinter import messagebox

# ====== Hàm xử lý đăng nhập ======
def loginAction():
    username = entryUsername.get()
    password = entryPassword.get()

    # Dữ liệu mẫu, bạn có thể lưu trong file hoặc database
    user_data = {
        "admin": "123456",
        "user1": "abcdef"
    }

    if username in user_data and user_data[username] == password:
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Đăng nhập", "Tài khoản hoặc mật khẩu không đúng!")

def clearAction():
    entryUsername.delete(0, END)
    entryPassword.delete(0, END)

# ====== Giao diện ======
root = Tk()
root.title("Đăng nhập")
root.geometry("300x180")
root.resizable(False, False)

Label(root, text="Màn hình Đăng nhập", fg="blue", font=("Arial", 14)).pack(pady=10)

# Username
frameUser = Frame(root)
Label(frameUser, text="Username:", width=10, anchor=W).pack(side=LEFT)
entryUsername = Entry(frameUser, width=20)
entryUsername.pack(side=LEFT)
frameUser.pack(pady=5)

# Password
framePass = Frame(root)
Label(framePass, text="Password:", width=10, anchor=W).pack(side=LEFT)
entryPassword = Entry(framePass, width=20, show="*")
entryPassword.pack(side=LEFT)
framePass.pack(pady=5)

# Nút
frameButton = Frame(root)
Button(frameButton, text="Đăng nhập", width=10, command=loginAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Xóa", width=10, command=clearAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", width=10, command=root.quit).pack(side=LEFT, padx=5)
frameButton.pack(pady=10)

root.mainloop()
