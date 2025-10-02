from math import sqrt
print("Chương trình Giải Phương trình bậc 2")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    # Phương trình bậc nhất bx + c = 0
    if b == 0 and c == 0:
        print("Vô số nghiệm")
    elif b == 0 and c != 0:
        print("Vô nghiệm")
    else:
        x = -c / b
        print("Nghiệm của phương trình là x =", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b - sqrt(delta)) / (2*a)
        x2 = (-b + sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
