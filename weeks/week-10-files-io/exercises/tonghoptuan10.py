# ==================================================
# XỬ LÝ FILE TRONG PYTHON
# (Giống ifstream/ofstream trong C++)
# ==================================================

# --------------------------------------------------
# 1. MỞ FILE VÀ GHI DỮ LIỆU (w = write)
# --------------------------------------------------
# Nếu file chưa có -> tạo mới
# Nếu file đã có -> xóa nội dung cũ và ghi lại

with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Xin chào Python\n")
    file.write("Tôi đang học xử lý file")

# Sau khi thoát khỏi with
# Python sẽ tự động đóng file
# Không cần file.close()


# --------------------------------------------------
# 2. ĐỌC FILE (r = read)
# --------------------------------------------------

with open("hello.txt", "r", encoding="utf-8") as file:
    data = file.read()

print("Nội dung file:")
print(data)


# --------------------------------------------------
# 3. GHI THÊM FILE (a = append)
# --------------------------------------------------
# Không xóa nội dung cũ
# Chỉ thêm vào cuối file

with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("\nĐây là dòng được thêm")


# --------------------------------------------------
# ĐỌC LẠI ĐỂ XEM KẾT QUẢ
# --------------------------------------------------

with open("hello.txt", "r", encoding="utf-8") as file:
    print("\nSau khi thêm:")
    print(file.read())


# ==================================================
# CSV (DỮ LIỆU DẠNG BẢNG)
# ==================================================

import csv

# --------------------------------------------------
# GHI FILE CSV
# --------------------------------------------------

with open("students.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Dòng tiêu đề
    writer.writerow(["Tên", "Điểm"])

    # Dữ liệu
    writer.writerow(["An", 9])
    writer.writerow(["Bình", 8])
    writer.writerow(["Chi", 10])


# --------------------------------------------------
# ĐỌC FILE CSV
# --------------------------------------------------

print("\nĐọc file CSV")

with open("students.csv", "r", encoding="utf-8") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ==================================================
# JSON (GIỐNG DICTIONARY)
# ==================================================

import json

# Tạo dữ liệu

student = {
    "name": "Tin",
    "age": 18,
    "score": 9.5
}


# --------------------------------------------------
# GHI JSON
# --------------------------------------------------

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(
        student,
        file,
        ensure_ascii=False,
        indent=4
    )


# --------------------------------------------------
# ĐỌC JSON
# --------------------------------------------------

with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("\nĐọc JSON")
print(data)

print(data["name"])
print(data["age"])
print(data["score"])


# ==================================================
# PATHLIB (QUẢN LÝ ĐƯỜNG DẪN)
# ==================================================

from pathlib import Path

# Tạo đối tượng file

file = Path("hello.txt")

# File có tồn tại không

print("\nFile có tồn tại không?")
print(file.exists())

# Tên file

print("\nTên file:")
print(file.name)

# Phần mở rộng

print("\nĐuôi file:")
print(file.suffix)

# Đường dẫn

print("\nĐường dẫn:")
print(file)


# ==================================================
# TỔNG HỢP
# ==================================================

print("\n========== GHI NHỚ ==========")

print("open()      : Mở file")
print("r           : Đọc file")
print("w           : Ghi mới")
print("a           : Ghi thêm")
print("read()      : Đọc nội dung")
print("write()     : Ghi nội dung")
print("with        : Tự động đóng file")
print("csv         : Dữ liệu dạng bảng")
print("json        : Dữ liệu dạng dictionary")
print("pathlib     : Quản lý đường dẫn")