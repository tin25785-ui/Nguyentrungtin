"""Lời giải Bài tập 02: Toán tử logic và logic nâng cao"""

# TODO 1: Kiểm tra năm nhuận
# Quy tắc: Chia hết cho 400 HOẶC (Chia hết cho 4 VÀ không chia hết cho 100)
nam = int(input("Nhập năm cần kiểm tra: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Năm {nam} là năm nhuận")
else:
    print(f"Năm {nam} không phải năm nhuận")

# TODO 2: Kiểm tra tam giác hợp lệ
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh của một tam giác")
    # Kiểm tra thêm loại tam giác
    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân")
else:
    print("3 cạnh này không thể tạo thành tam giác")