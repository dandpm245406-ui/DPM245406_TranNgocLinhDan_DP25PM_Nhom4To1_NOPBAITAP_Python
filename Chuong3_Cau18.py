size = 5
for i in range(size):
    # In khoảng trắng
    for j in range(size - i - 1):
        print('  ', end='')  # 2 khoảng trắng để căn đều với dấu *
    # In dấu *
    for k in range(i + 1):
        print('* ', end='')
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

size = 5
total_lines = size * 2 - 1

for i in range(total_lines):
    if i < size:
        # In tam giác 1 bình thường
        for j in range(i + 1):
            print('*', end=' ')
        print()
    else:
        # In khoảng trắng bằng chiều rộng tam giác 1
        print('  ' * size, end='')
        # Tính dòng thứ trong tam giác 2 (bắt đầu từ 0)
        line_in_t2 = i - size
        # In tam giác 2: giảm dần số dấu *
        for k in range(size - line_in_t2):
            print('*', end=' ')
        print()
