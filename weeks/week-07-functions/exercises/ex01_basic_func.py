"""
Bài tập 01: Hàm cơ bản 🧩
============================
Mục tiêu: Viết hàm đầu tiên với def và return
"""

import math

# TODO 1: Viết hàm chao(ten) in ra "Xin chào, [ten]!"
# Gọi hàm 3 lần với 3 tên khác nhau
def chao(ten):
    print(f"Xin chào, {ten}!")

chao("An")
chao("Bình")
chao("Chi")

# TODO 2: Viết hàm tinh_dien_tich_hinh_tron(ban_kinh)
# Trả về diện tích (pi * r^2)
# In kết quả với bán kính = 5, 7, 10
def tinh_dien_tich_hinh_tron(ban_kinh):
    return math.pi * (ban_kinh ** 2)

for r in [5, 7, 10]:
    dt = tinh_dien_tich_hinh_tron(r)
    print(f"Diện tích hình tròn bán kính {r} là: {dt:.2f}")

# TODO 3: Viết hàm la_so_chan(n) trả về True/False
# Viết hàm la_so_nguyen_to(n) trả về True/False
# Test với nhiều giá trị
def la_so_chan(n):
    return n % 2 == 0

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Số 10 có là số chẵn không? {la_so_chan(10)}")
print(f"Số 7 có là số nguyên tố không? {la_so_nguyen_to(7)}")
print(f"Số 15 có là số nguyên tố không? {la_so_nguyen_to(15)}")

# TODO 4: Viết hàm tinh_thong_ke(numbers)
# Trả về tuple: (min, max, trung_binh, tong)
# Gọi hàm và unpack kết quả
def tinh_thong_ke(numbers):
    if not numbers:
        return 0, 0, 0, 0
    return (min(numbers), max(numbers), sum(numbers) / len(numbers), sum(numbers))

nho_nhat, lon_nhat, trung_binh, tong_cong = tinh_thong_ke([10, 20, 30, 40, 50])
print(f"Thống kê list [10...50]: Min={nho_nhat}, Max={lon_nhat}, TB={trung_binh}, Tổng={tong_cong}")

# TODO 5 (Thử thách): Viết hàm đệ quy tinh_giai_thua(n)
# 5! = 5 × 4 × 3 × 2 × 1 = 120
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

print(f"Giai thừa của 5 là: {tinh_giai_thua(5)}")
