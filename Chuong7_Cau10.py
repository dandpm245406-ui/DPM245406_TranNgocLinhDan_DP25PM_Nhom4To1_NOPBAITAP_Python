import json
import os

# ======= Class =======
class ClassRoom:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.students = []  # danh sách sinh viên thuộc lớp

class Student:
    def __init__(self, code, name, birth_year, class_code):
        self.code = code
        self.name = name
        self.birth_year = birth_year
        self.class_code = class_code

# ======= Hàm lưu và đọc file JSON =======
def save_to_file(classes, filename="students.json"):
    data = []
    for cls in classes:
        cls_data = {
            "code": cls.code,
            "name": cls.name,
            "students": [
                {"code": s.code, "name": s.name, "birth_year": s.birth_year} 
                for s in cls.students
            ]
        }
        data.append(cls_data)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Lưu file JSON thành công!")

def load_from_file(filename="students.json"):
    classes = []
    if not os.path.exists(filename):
        return classes
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for cls_data in data:
            cls = ClassRoom(cls_data["code"], cls_data["name"])
            for s in cls_data.get("students", []):
                student = Student(s["code"], s["name"], s["birth_year"], cls.code)
                cls.students.append(student)
            classes.append(cls)
    return classes

# ======= Hàm quản lý =======
def add_class(classes):
    code = input("Nhập mã lớp: ")
    name = input("Nhập tên lớp: ")
    classes.append(ClassRoom(code, name))

def add_student(classes):
    code = input("Nhập mã sinh viên: ")
    name = input("Nhập tên sinh viên: ")
    birth_year = int(input("Nhập năm sinh: "))
    class_code = input("Nhập mã lớp của sinh viên: ")
    for cls in classes:
        if cls.code == class_code:
            cls.students.append(Student(code, name, birth_year, class_code))
            print("Thêm sinh viên thành công!")
            return
    print("Không tìm thấy lớp học!")

def display(classes):
    for cls in classes:
        print(f"\nLớp: {cls.code} - {cls.name}")
        for s in cls.students:
            print(f"  {s.code} | {s.name} | {s.birth_year}")

def search_student(classes):
    key = input("Nhập mã hoặc tên sinh viên cần tìm: ").lower()
    for cls in classes:
        for s in cls.students:
            if key in s.code.lower() or key in s.name.lower():
                print(f"Tìm thấy: {s.code} | {s.name} | {s.birth_year} | Lớp {cls.name}")

def sort_students_by_birthyear(classes):
    for cls in classes:
        cls.students.sort(key=lambda x: x.birth_year)
    print("Sắp xếp sinh viên theo năm sinh thành công!")

def edit_student(classes):
    code = input("Nhập mã sinh viên cần sửa: ")
    for cls in classes:
        for s in cls.students:
            if s.code == code:
                s.name = input(f"Sửa tên ({s.name}): ") or s.name
                birth_input = input(f"Sửa năm sinh ({s.birth_year}): ")
                if birth_input:
                    s.birth_year = int(birth_input)
                print("Sửa thành công!")
                return
    print("Không tìm thấy sinh viên!")

def delete_student(classes):
    code = input("Nhập mã sinh viên cần xóa: ")
    for cls in classes:
        for s in cls.students:
            if s.code == code:
                cls.students.remove(s)
                print("Xóa sinh viên thành công!")
                return
    print("Không tìm thấy sinh viên!")

# ======= Main menu =======
def main():
    classes = load_from_file()
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm lớp học")
        print("2. Thêm sinh viên")
        print("3. Hiển thị danh sách")
        print("4. Tìm sinh viên")
        print("5. Sửa sinh viên")
        print("6. Xóa sinh viên")
        print("7. Sắp xếp sinh viên theo năm sinh")
        print("8. Lưu file JSON")
        print("0. Thoát")
        choice = input("Chọn: ")
        if choice == "1":
            add_class(classes)
        elif choice == "2":
            add_student(classes)
        elif choice == "3":
            display(classes)
        elif choice == "4":
            search_student(classes)
        elif choice == "5":
            edit_student(classes)
        elif choice == "6":
            delete_student(classes)
        elif choice == "7":
            sort_students_by_birthyear(classes)
        elif choice == "8":
            save_to_file(classes)
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
