"""
Mini-Project: Máy tính điểm GPA 📊
Mô tả: Nhập điểm các môn, tính GPA hệ 4 và xếp loại học lực.
Tác giả: Gemini Code Assist
"""

print("=== HỆ THỐNG TÍNH ĐIỂM GPA ===")

# 1. Nhập số lượng môn học
try:
    so_luong_mon = int(input("Nhập số lượng môn học: "))
except ValueError:
    print("Lỗi: Số lượng môn học phải là một số nguyên.")
    exit()

tong_diem_tin_chi = 0
tong_so_tin_chi = 0

# 2. Lặp qua từng môn để nhập dữ liệu
for i in range(1, so_luong_mon + 1):
    print(f"\n--- Nhập thông tin môn thứ {i} ---")
    ten_mon = input("Tên môn học: ").strip()
    
    try:
        tin_chi = int(input(f"Số tín chỉ của môn '{ten_mon}': "))
        diem_10 = float(input(f"Điểm hệ 10 của môn '{ten_mon}': "))
        
        # Kiểm tra tính hợp lệ của điểm
        if not (0 <= diem_10 <= 10):
            print("⚠️ Điểm không hợp lệ (phải từ 0-10). Môn này sẽ bị bỏ qua.")
            continue
            
        # 3. Chuyển đổi điểm hệ 10 sang hệ 4 (theo gợi ý)
        # Công thức: điểm_4 = điểm_10 * 4 / 10
        diem_4 = (diem_10 * 4) / 10
        
        # Tích lũy để tính GPA: Σ(điểm_4 * tín chỉ) / Σ tín chỉ
        tong_diem_tin_chi += (diem_4 * tin_chi)
        tong_so_tin_chi += tin_chi
        
    except ValueError:
        print("⚠️ Lỗi nhập liệu. Vui lòng nhập số cho tín chỉ và điểm.")
        continue

# 4. Tính toán GPA cuối cùng và Xếp loại
if tong_so_tin_chi > 0:
    gpa = tong_diem_tin_chi / tong_so_tin_chi
    
    # Dùng if/elif/else cho xếp loại theo yêu cầu của đề bài
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

    # 5. Hiển thị bảng kết quả đẹp
    print("\n" + "═"*40)
    print(f"{'KẾT QUẢ HỌC TẬP':^40}")
    print("─"*40)
    print(f" Tổng số tín chỉ:    {tong_so_tin_chi}")
    print(f" Điểm GPA (Hệ 4):    {gpa:.2f}")
    print(f" Xếp loại học lực:   {xep_loai}")
    print("═"*40)
else:
    print("\n[!] Không có đủ dữ liệu hợp lệ để tính toán GPA.")