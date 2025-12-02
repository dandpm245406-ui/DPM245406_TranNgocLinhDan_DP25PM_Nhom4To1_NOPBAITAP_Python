import os

# ======= Class =======
class Category:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.products = []  # danh sách sản phẩm thuộc danh mục

class Product:
    def __init__(self, code, name, price, category_code):
        self.code = code
        self.name = name
        self.price = price
        self.category_code = category_code

# ======= Hàm lưu và đọc file =======
def save_to_file(categories, filename="data.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for cat in categories:
            f.write(f"C|{cat.code}|{cat.name}\n")
            for p in cat.products:
                f.write(f"P|{p.code}|{p.name}|{p.price}|{p.category_code}\n")
    print("Lưu file thành công!")

def load_from_file(filename="data.txt"):
    categories = []
    if not os.path.exists(filename):
        return categories
    cat_dict = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("C|"):
                _, code, name = line.split("|")
                cat = Category(code, name)
                categories.append(cat)
                cat_dict[code] = cat
            elif line.startswith("P|"):
                _, code, name, price, cat_code = line.split("|")
                p = Product(code, name, float(price), cat_code)
                if cat_code in cat_dict:
                    cat_dict[cat_code].products.append(p)
    return categories

# ======= Hàm quản lý =======
def add_category(categories):
    code = input("Nhập mã danh mục: ")
    name = input("Nhập tên danh mục: ")
    categories.append(Category(code, name))

def add_product(categories):
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập đơn giá: "))
    cat_code = input("Nhập mã danh mục của sản phẩm: ")
    for cat in categories:
        if cat.code == cat_code:
            cat.products.append(Product(code, name, price, cat_code))
            print("Thêm sản phẩm thành công!")
            return
    print("Không tìm thấy danh mục!")

def display(categories):
    for cat in categories:
        print(f"\nDanh mục: {cat.code} - {cat.name}")
        for p in cat.products:
            print(f"  {p.code} | {p.name} | {p.price}")

def search_product(categories):
    key = input("Nhập mã hoặc tên sản phẩm cần tìm: ").lower()
    for cat in categories:
        for p in cat.products:
            if key in p.code.lower() or key in p.name.lower():
                print(f"Tìm thấy: {p.code} | {p.name} | {p.price} | Danh mục {cat.name}")

def sort_products_by_price(categories):
    for cat in categories:
        cat.products.sort(key=lambda x: x.price)
    print("Sắp xếp thành công theo giá tăng dần!")

def edit_product(categories):
    code = input("Nhập mã sản phẩm cần sửa: ")
    for cat in categories:
        for p in cat.products:
            if p.code == code:
                p.name = input(f"Sửa tên ({p.name}): ") or p.name
                price_input = input(f"Sửa giá ({p.price}): ")
                if price_input:
                    p.price = float(price_input)
                print("Sửa thành công!")
                return
    print("Không tìm thấy sản phẩm!")

def delete_product(categories):
    code = input("Nhập mã sản phẩm cần xóa: ")
    for cat in categories:
        for p in cat.products:
            if p.code == code:
                cat.products.remove(p)
                print("Xóa thành công!")
                return
    print("Không tìm thấy sản phẩm!")

# ======= Main menu =======
def main():
    categories = load_from_file()
    while True:
        print("\n===== QUẢN LÝ SẢN PHẨM =====")
        print("1. Thêm danh mục")
        print("2. Thêm sản phẩm")
        print("3. Hiển thị danh sách")
        print("4. Tìm sản phẩm")
        print("5. Sửa sản phẩm")
        print("6. Xóa sản phẩm")
        print("7. Sắp xếp sản phẩm theo giá")
        print("8. Lưu file")
        print("0. Thoát")
        choice = input("Chọn: ")
        if choice == "1":
            add_category(categories)
        elif choice == "2":
            add_product(categories)
        elif choice == "3":
            display(categories)
        elif choice == "4":
            search_product(categories)
        elif choice == "5":
            edit_product(categories)
        elif choice == "6":
            delete_product(categories)
        elif choice == "7":
            sort_products_by_price(categories)
        elif choice == "8":
            save_to_file(categories)
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
