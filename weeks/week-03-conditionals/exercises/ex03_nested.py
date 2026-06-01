"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý các tình huống có nhiều tầng quyết định
"""

# TODO: Hệ thống rút tiền ATM đơn giản
so_du = 5000000  # 5 triệu
han_muc_rut = 2000000  # 2 triệu/lần

so_tien_rut = int(input("Nhập số tiền bạn muốn rút: "))

if so_tien_rut > 0:
    if so_tien_rut <= so_du:
        if so_tien_rut <= han_muc_rut:
            so_du -= so_tien_rut
            print(f"Rút tiền thành công! Số dư còn lại: {so_du:,} VNĐ")
        else:
            print(f"Thất bại: Số tiền rút vượt quá hạn mức {han_muc_rut:,} VNĐ/lần.")
    else:
        print("Thất bại: Số dư tài khoản không đủ.")
else:
    print("Lỗi: Số tiền rút phải lớn hơn 0.")