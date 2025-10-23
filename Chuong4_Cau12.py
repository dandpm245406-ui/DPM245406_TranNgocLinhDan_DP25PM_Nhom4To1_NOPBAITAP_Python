def oscillate(start, end):
    # In cặp từ start đến 0 (âm trước, dương sau)
    for i in range(start, 1):
        yield i
        yield -i
    # In cặp từ 1 đến end-1 (dương trước, âm sau)
    for i in range(1, end):
        yield i
        yield -i

# Gọi và in kết quả:
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
