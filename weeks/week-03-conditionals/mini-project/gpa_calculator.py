"""
Mini-Project Tuần 03: Máy tính điểm GPA 📊
"""

print("--- CHƯƠNG TRÌNH TÍNH ĐIỂM GPA ---")

# 1. Nhập số lượng môn học
so_mon = int(input("Nhập số lượng môn học: "))

tong_diem_he_4 = 0
tong_tin_chi = 0

# 2. Lặp qua từng môn để nhập liệu
for i in range(1, so_mon + 1):
    print(f"\nNhập thông tin môn thứ {i}:")
    ten_mon = input("  Tên môn học: ")
    tin_chi = int(input("  Số tín chỉ: "))
    diem_10 = float(input("  Điểm hệ 10: "))
    
    # Chuyển đổi điểm hệ 10 sang hệ 4
    diem_4 = diem_10 * 4 / 10
    
    # Tính tổng có trọng số
    tong_diem_he_4 += (diem_4 * tin_chi)
    tong_tin_chi += tin_chi

# 3. Tính GPA cuối cùng
if tong_tin_chi > 0:
    gpa = tong_diem_he_4 / tong_tin_chi
    
    # 4. Xếp loại dựa trên GPA hệ 4
    if gpa >= 3.6:
        xep_loai = "Xuất sắc"
    elif gpa >= 3.2:
        xep_loai = "Giỏi"
    elif gpa >= 2.5:
        xep_loai = "Khá"
    elif gpa >= 2.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    # 5. In kết quả đẹp
    print("\n" + "="*35)
    print(f"{'KẾT QUẢ HỌC TẬP':^35}")
    print("-" * 35)
    print(f"Tổng số tín chỉ: {tong_tin_chi}")
    print(f"Điểm GPA hệ 4:   {gpa:.2f}")
    print(f"Xếp loại:        {xep_loai}")
    print("=" * 35)
else:
    print("Dữ liệu không hợp lệ.")