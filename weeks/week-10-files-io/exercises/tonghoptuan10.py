"""
Bài tập tổng hợp: Xử lý File, CSV, JSON và Pathlib trong Python.
Mục tiêu: Củng cố kỹ năng đọc/ghi dữ liệu an toàn và hiệu quả.
"""
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

try:
    with open("hello.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print("Nội dung file:")
    print(data)
except FileNotFoundError:
    print("Lỗi: File hello.txt không tồn tại.")
    data = ""


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

try:
    with open("hello.txt", "r", encoding="utf-8") as file:
        print("\nSau khi thêm:")
        print(file.read())
except FileNotFoundError:
    print(" Không thể đọc file sau khi ghi thêm.")


# --------------------------------------------------
# 4. MỞ FILE ĐÃ CÓ VÀ THỰC HIỆN CÁC THAO TÁC ĐỌC
# --------------------------------------------------
print("\n==================================================")
print("THAO TÁC VỚI FILE ĐÃ CÓ (hello.txt)")
print("==================================================")

file_to_read = "hello.txt"

# Đọc toàn bộ nội dung file
print("\n--- Đọc toàn bộ nội dung file ---")
try:
    with open(file_to_read, "r", encoding="utf-8") as file:
        full_content = file.read()
        print(full_content)
except FileNotFoundError:
    print(f"❌ Lỗi: File '{file_to_read}' không tồn tại.")

# Đọc file theo từng dòng
print("\n--- Đọc file theo từng dòng ---")
try:
    with open(file_to_read, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, 1):
            print(f"Dòng {i}: {line.strip()}") # .strip() để loại bỏ ký tự xuống dòng
except FileNotFoundError:
    print(f" Lỗi: File '{file_to_read}' không tồn tại.")

# Đọc tất cả các dòng vào một danh sách
print("\n--- Đọc tất cả các dòng vào một danh sách ---")
try:
    with open(file_to_read, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
        print(f"Số lượng dòng: {len(all_lines)}")
        for i, line in enumerate(all_lines, 1):
            print(f"Dòng {i} (từ list): {line.strip()}")
except FileNotFoundError:
    print(f" Lỗi: File '{file_to_read}' không tồn tại.")

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

try:
    with open("students.csv", "r", encoding="utf-8") as file:
        # Sử dụng DictReader để truy cập qua tên cột, code sẽ rõ ràng hơn
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Học sinh: {row['Tên']} - Điểm: {row['Điểm']}")
except FileNotFoundError:
    print(" File students.csv chưa được tạo.")

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

try:
    with open("student.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\nĐọc JSON")
    print(data)
    print(f"Tên: {data['name']}, Tuổi: {data['age']}, Điểm: {data['score']}")
except FileNotFoundError:
    print(" File student.json không tồn tại.")
except json.JSONDecodeError:
    print("Lỗi: Định dạng file JSON không hợp lệ.")
    
# ==================================================
# PATHLIB (QUẢN LÝ ĐƯỜNG DẪN)
# ==================================================

from pathlib import Path

# Tạo đối tượng file

file_path = Path("hello.txt")

# File có tồn tại không

print("\nFile có tồn tại không?")
print(f"{file_path.name}: {'Có' if file_path.exists() else 'Không'}")

# Tên file

print("\nTên file:")
print(file_path.name)

# Phần mở rộng

print("\nĐuôi file:")
print(file_path.suffix)


# Đường dẫn

print(f"\nĐường dẫn tuyệt đối: {file_path.absolute()}")


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