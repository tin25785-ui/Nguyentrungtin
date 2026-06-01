"""
Bài tập 02: Toán tử logic kết hợp 🧠
====================================
Mục tiêu: Sử dụng and, or, not để xử lý điều kiện phức tạp
"""

# TODO: Kiểm tra một năm có phải năm nhuận hay không
# Quy tắc: Năm nhuận là năm (chia hết cho 4 VÀ không chia hết cho 100) HOẶC chia hết cho 400

nam = int(input("Nhập năm cần kiểm tra: "))

is_leap = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

if is_leap:
    print(f"Năm {nam} là năm nhuận ✅")
else:
    print(f"Năm {nam} không phải năm nhuận ❌")

# TODO: Kiểm tra quyền vào câu lạc bộ
tuoi = int(input("Nhập tuổi của bạn: "))
co_the_thanh_vien = input("Bạn có thẻ thành viên không? (c/k): ").lower() == 'c'

if tuoi >= 18 or co_the_thanh_vien:
    print("Chào mừng! Bạn có thể vào.")
else:
    print("Rất tiếc, bạn không đủ điều kiện vào.")