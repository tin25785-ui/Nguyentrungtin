"""
Bài tập 01: Phân loại và xếp hạng 🏆
====================================
Mục tiêu: Sử dụng cấu trúc if/elif/else cơ bản
"""

# TODO: Nhập điểm trung bình (0-10)
# Xếp loại: >= 9.0: Xuất sắc, >= 8.0: Giỏi, >= 6.5: Khá, >= 5.0: Trung bình, < 5.0: Yếu
# Kiểm tra nếu điểm nhập vào không nằm trong khoảng 0-10 thì báo lỗi.

diem = float(input("Nhập điểm trung bình của bạn (0-10): "))

if diem < 0 or diem > 10:
    print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
else:
    if diem >= 9.0:
        xep_loai = "Xuất sắc"
    elif diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    print(f"Với số điểm {diem}, xếp loại của bạn là: {xep_loai}")