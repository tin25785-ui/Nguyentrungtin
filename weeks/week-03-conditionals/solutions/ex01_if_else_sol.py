"""Lời giải Bài tập 01: Cấu trúc điều kiện cơ bản"""

# TODO 1: Kiểm tra số chẵn/lẻ
n = int(input("Nhập một số nguyên: "))
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")

# TODO 2: Kiểm tra số âm, dương hoặc bằng 0
x = float(input("Nhập số x: "))
if x > 0:
    print("x là số dương")
elif x < 0:
    print("x là số âm")
else:
    print("x bằng 0")

# TODO 3: Xếp loại học lực
diem = float(input("Nhập điểm trung bình: "))
if 9.0 <= diem <= 10:
    print("Xếp loại: Xuất sắc")
elif diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# TODO 4: Tìm số lớn nhất trong 3 số
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

max_val = a
if b > max_val: max_val = b
if c > max_val: max_val = c
print(f"Số lớn nhất là: {max_val}")