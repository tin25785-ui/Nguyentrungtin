"""
Bài tập 01: Dictionary cơ bản 📖
==================================
Mục tiêu: Tạo, truy cập, sửa đổi dict
"""

# TODO 1: Tạo dict lưu thông tin sinh viên
# Keys: "ten", "tuoi", "diem", "lop"
# In ra từng giá trị bằng cả dict["key"] và dict.get("key") 
print("--- TODO 1: Thông tin sinh viên ---")
sinh_vien = {
    "ten": "Nguyễn Văn A",
    "tuoi": 20,
    "diem": 8.5,
    "lop": "K20 Khoa Học Máy Tính"
}

print(f"Tên sinh viên (dict['key']): {sinh_vien['ten']}")
print(f"Tuổi sinh viên (dict.get('key')): {sinh_vien.get('tuoi')}")
print(f"Điểm sinh viên (dict['key']): {sinh_vien['diem']}")
print(f"Lớp sinh viên (dict.get('key')): {sinh_vien.get('lop')}")
print(f"Số điện thoại (dict.get('key', 'Không có')): {sinh_vien.get('sdt', 'Không có')}") # Ví dụ với key không tồn tại

# TODO 2: Cho danh sách điểm:
# diem = {"Toán": 8, "Văn": 7, "Anh": 9, "Lý": 6, "Hóa": 8}
# a) Thêm môn "Sinh": 7
# b) Sửa điểm "Văn" thành 8
# c) Xóa môn "Hóa"
# d) In ra tên và điểm từng môn (dùng items()) 
# e) Tính điểm trung bình 
print("\n--- TODO 2: Thao tác với danh sách điểm ---")
diem = {"Toán": 8, "Văn": 7, "Anh": 9, "Lý": 6, "Hóa": 8}
print(f"Điểm ban đầu: {diem}")

# a) Thêm môn "Sinh": 7
diem["Sinh"] = 7
print(f"Sau khi thêm Sinh: {diem}")

# b) Sửa điểm "Văn" thành 8
diem["Văn"] = 8
print(f"Sau khi sửa điểm Văn: {diem}")

# c) Xóa môn "Hóa"
del diem["Hóa"]
print(f"Sau khi xóa Hóa: {diem}")

# d) In ra tên và điểm từng môn (dùng items())
print("\nĐiểm từng môn:")
for mon, score in diem.items():
    print(f"- {mon}: {score}")

# e) Tính điểm trung bình
tong_diem = sum(diem.values())
so_mon = len(diem)
diem_trung_binh = tong_diem / so_mon
print(f"Điểm trung bình: {diem_trung_binh:.2f}")

# TODO 3: Dict comprehension
# Tạo dict bình phương: {1: 1, 2: 4, 3: 9, ..., 10: 100}
# Lọc chỉ giữ số chẵn: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100} 
print("\n--- TODO 3: Dict comprehension ---")

# Tạo dict bình phương
dict_binh_phuong = {x: x**2 for x in range(1, 11)}
print(f"Dict bình phương (1-10): {dict_binh_phuong}")

# Lọc chỉ giữ số chẵn
dict_chan = {k: v for k, v in dict_binh_phuong.items() if k % 2 == 0}
print(f"Dict bình phương (chỉ số chẵn): {dict_chan}")

# TODO 4 (Thử thách): Đếm tần suất ký tự trong chuỗi
# Nhập chuỗi, đếm số lần xuất hiện mỗi ký tự
# "hello" → {"h": 1, "e": 1, "l": 2, "o": 1} 
print("\n--- TODO 4: Đếm tần suất ký tự ---")
chuoi_nhap = input("Nhập một chuỗi để đếm tần suất ký tự: ")

tan_suat_ky_tu = {}
for char in chuoi_nhap:
    tan_suat_ky_tu[char] = tan_suat_ky_tu.get(char, 0) + 1

print(f"Tần suất ký tự trong chuỗi '{chuoi_nhap}': {tan_suat_ky_tu}")
