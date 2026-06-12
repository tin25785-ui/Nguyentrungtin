# ==========================================
# TỔNG HỢP DICTIONARY (DICT) VÀ SET PYTHON
# ==========================================

# ------------------------------------------
# 1. DICTIONARY (DICT)
# ------------------------------------------

# Tạo dictionary
students = {
    "An": 8.5,
    "Bình": 9.0
}

# In dictionary
print("Dictionary ban đầu:")
print(students)

# Truy cập giá trị bằng key
print("\nĐiểm của An:")
print(students["An"])

# Thêm dữ liệu
students["Chi"] = 7.5

# Sửa dữ liệu
students["An"] = 10

# Xóa dữ liệu
del students["Bình"]

print("\nDictionary sau khi thêm, sửa, xóa:")
print(students)


# ------------------------------------------
# 2. DUYỆT DICTIONARY
# ------------------------------------------

print("\nDuyệt keys()")
for key in students.keys():
    print(key)

print("\nDuyệt values()")
for value in students.values():
    print(value)

print("\nDuyệt items()")
for key, value in students.items():
    print(key, ":", value)


# ------------------------------------------
# 3. SET
# ------------------------------------------

# Set không cho phép phần tử trùng
numbers = {1, 2, 2, 3, 3, 4, 5}

print("\nSet:")
print(numbers)

# Thêm phần tử
numbers.add(6)

# Xóa phần tử
numbers.remove(2)

print("\nSet sau khi thêm và xóa:")
print(numbers)


# ------------------------------------------
# 4. CÁC PHÉP TOÁN TẬP HỢP
# ------------------------------------------

A = {1, 2, 3}
B = {3, 4, 5}

# Hợp
print("\nHợp A | B")
print(A | B)

# Giao
print("\nGiao A & B")
print(A & B)

# Hiệu
print("\nHiệu A - B")
print(A - B)


# ------------------------------------------
# 5. DICTIONARY LỒNG NHAU
# ------------------------------------------

students_info = {
    "An": {
        "tuoi": 18,
        "diem": 8.5
    },
    "Bình": {
        "tuoi": 19,
        "diem": 9.0
    }
}

print("\nThông tin học sinh:")

for ten, thongtin in students_info.items():
    print("----------------")
    print("Tên:", ten)
    print("Tuổi:", thongtin["tuoi"])
    print("Điểm:", thongtin["diem"])

# Lấy điểm của An
print("\nĐiểm của An:")
print(students_info["An"]["diem"])


# ------------------------------------------
# 6. CHỌN CẤU TRÚC DỮ LIỆU
# ------------------------------------------

# List: lưu danh sách
fruits = ["Táo", "Cam", "Xoài"]

# Tuple: dữ liệu cố định
birthday = (20, 10, 2005)

# Dictionary: key -> value
scores = {
    "An": 8,
    "Bình": 9
}

# Set: không cho trùng
subjects = {"Toán", "Lý", "Toán", "Hóa"}

print("\nList:")
print(fruits)

print("\nTuple:")
print(birthday)

print("\nDictionary:")
print(scores)

print("\nSet:")
print(subjects)


# ==========================================
# TÓM TẮT
# ==========================================

# List      -> Danh sách
# Tuple     -> Dữ liệu cố định
# Dictionary-> Key -> Value
# Set       -> Không cho trùng