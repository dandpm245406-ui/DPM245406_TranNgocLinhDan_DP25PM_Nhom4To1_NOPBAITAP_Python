import re

def NegativeNumberInStrings(s):
    # Tìm số nguyên âm có dạng -5, -12, -999...
    numbers = re.findall(r'-\d+', s)
    return numbers

# Ví dụ chạy thử
test = "abc-5xyz-12k9l--p"
print(NegativeNumberInStrings(test))
