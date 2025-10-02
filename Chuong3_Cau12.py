for i in range(1, 11):          # i từ 1 đến 10 (các số nhân)
    for j in range(2, 10):      # j từ 2 đến 9 (bảng cửu chương)
        line = "{0}*{1:>2}={2:>2}".format(j, i, i*j)
        print(line, end='\t')   # in trên cùng 1 dòng, cách nhau tab
    print()                    # xuống dòng sau mỗi i
