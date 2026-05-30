"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"
tuoi = int(input("Nhập tuổi: "))
if tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem = float(input("Nhập điểm (0-10): "))
if 9 <= diem <= 10:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("TB")
else:
    print("Yếu")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
nam = int(input("Nhập năm cần kiểm tra: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải năm nhuận")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= c:
    # Ở đây ta đã biết a không phải lớn nhất (vì điều kiện trên sai)
    # Nên chỉ cần so sánh b và c
    lon_nhat = b
else:
    lon_nhat = c

print(f"Số lớn nhất trong 3 số là: {lon_nhat}")
