# weeks/week-09-midterm-project/student_manager.py
# Hệ thống quản lý học sinh
# Tác giả: AI Assistant
# Tuần 09 — Dự án giữa kỳ

# ─── DỮ LIỆU ─────────────────────────────────
# Danh sách học sinh là list of dicts
students = []

# ─── CÁC HÀM CỐT LÕI ────────────────────────

def tinh_diem_tb(hoc_sinh: dict) -> float:
    """Tính điểm trung bình của một học sinh."""
    diem = [hoc_sinh["toan"], hoc_sinh["van"], hoc_sinh["anh"]]
    return round(sum(diem) / len(diem), 2)


def xep_loai(dtb: float) -> str:
    """Xếp loại dựa trên điểm trung bình."""
    if dtb >= 9:
        return "Xuất sắc"
    elif dtb >= 8:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def input_diem(msg: str) -> float:
    """Nhập và kiểm tra điểm hợp lệ (0-10)."""
    while True:
        try:
            diem = float(input(msg))
            if 0 <= diem <= 10:
                return diem
            print("❌ Điểm phải nằm trong khoảng từ 0 đến 10!")
        except ValueError:
            print("❌ Vui lòng nhập một số hợp lệ!")


def them_hoc_sinh():
    """Thêm học sinh mới vào danh sách."""
    print("\n=== THÊM HỌC SINH ===")
    
    ten = input("Tên học sinh: ").strip()
    if not ten:
        print("❌ Tên không được rỗng!")
        return
    
    # Kiểm tra trùng tên
    if any(hs["ten"].lower() == ten.lower() for hs in students):
        print(f"❌ Học sinh '{ten}' đã tồn tại!")
        return
    
    try:
        tuoi = int(input("Tuổi: "))
    except ValueError:
        print("❌ Tuổi phải là số nguyên!")
        return
        
    toan = input_diem("Điểm Toán (0-10): ")
    van  = input_diem("Điểm Văn (0-10): ")
    anh  = input_diem("Điểm Anh (0-10): ")
    
    hoc_sinh = {
        "ten": ten,
        "tuoi": tuoi,
        "toan": toan,
        "van": van,
        "anh": anh,
    }
    students.append(hoc_sinh)
    dtb = tinh_diem_tb(hoc_sinh)
    print(f"Đã thêm {ten} — ĐTB: {dtb} — {xep_loai(dtb)}")


def xem_danh_sach(danh_sach=None):
    """Hiển thị danh sách học sinh dạng bảng."""
    ds = danh_sach if danh_sach is not None else students
    
    if not ds:
        print("📭 Danh sách trống!")
        return
    
    print(f"\n{'='*80}")
    print(f"{'STT':<5}{'Tên':<20}{'Tuổi':<6}{'Toán':<7}{'Văn':<7}{'Anh':<7}{'ĐTB':<7}{'Xếp loại'}")
    print(f"{'─'*80}")
    
    for i, hs in enumerate(ds, 1):
        dtb = tinh_diem_tb(hs)
        loai = xep_loai(dtb)
        print(f"{i:<5}{hs['ten']:<20}{hs['tuoi']:<6}"
              f"{hs['toan']:<7.1f}{hs['van']:<7.1f}{hs['anh']:<7.1f}"
              f"{dtb:<7.2f}{loai}")
    
    print(f"{'='*80}")
    print(f"Tổng: {len(ds)} học sinh")


def tim_hoc_sinh():
    """Tìm học sinh theo tên."""
    ten = input("Nhập tên cần tìm: ").strip().lower()
    ket_qua = [hs for hs in students if ten in hs["ten"].lower()]
    
    if not ket_qua:
        print(f"🔍 Không tìm thấy học sinh nào có tên '{ten}'")
        return
    
    print(f"\n🔍 Tìm thấy {len(ket_qua)} kết quả:")
    xem_danh_sach(ket_qua)


def xoa_hoc_sinh():
    """Xóa học sinh theo tên."""
    ten = input("Tên học sinh cần xóa: ").strip()
    for i, hs in enumerate(students):
        if hs["ten"].lower() == ten.lower():
            confirm = input(f"Bạn có chắc muốn xóa '{hs['ten']}'? (c/k): ").lower()
            if confirm == 'c':
                students.pop(i)
                print(f"✅ Đã xóa học sinh '{hs['ten']}'")
            else:
                print("Hủy bỏ xóa.")
            return
    print(f"❌ Không tìm thấy '{ten}'")


def thong_ke():
    """Thống kê toàn lớp."""
    if not students:
        print(" Danh sách trống!")
        return
    
    diem_tb_list = [tinh_diem_tb(hs) for hs in students]
    
    print(f"\n{'='*40}")
    print("       THỐNG KÊ TOÀN LỚP")
    print(f"{'─'*40}")
    print(f"  Tổng học sinh:   {len(students)}")
    print(f"  ĐTB cao nhất:    {max(diem_tb_list):.2f}")
    print(f"  ĐTB thấp nhất:   {min(diem_tb_list):.2f}")
    print(f"  ĐTB toàn lớp:    {sum(diem_tb_list)/len(diem_tb_list):.2f}")
    
    # Phân bổ xếp loại
    print(f"\n  Phân bổ xếp loại:")
    loai_names = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
    for loai in loai_names:
        so_hs = sum(1 for dtb in diem_tb_list if xep_loai(dtb) == loai)
        if so_hs > 0:
            bar = "" * so_hs
            print(f"    {loai:<12}: {bar} ({so_hs})")
    print(f"{'='*40}")


def sap_xep():
    """Sắp xếp danh sách học sinh."""
    if not students:
        print("📭 Danh sách trống!")
        return
        
    print("\n--- Sắp xếp danh sách ---")
    print("1. Theo tên (A-Z)")
    print("2. Theo điểm trung bình (Cao -> Thấp)")
    lua_chon = input("Chọn kiểu sắp xếp: ")
    
    if lua_chon == "1":
        students.sort(key=lambda hs: hs["ten"].lower())
        print(" Đã sắp xếp theo tên!")
    elif lua_chon == "2":
        students.sort(key=tinh_diem_tb, reverse=True)
        print("Đã sắp xếp theo điểm trung bình!")
    else:
        print("Lựa chọn không hợp lệ!")
        return
    
    xem_danh_sach()

# ─── MENU CHÍNH ───────────────────────────────

def hien_thi_menu():
    print("\n" + "="*35)
    print("  HỆ THỐNG QUẢN LÝ HỌC SINH")
    print("="*35)
    print("  1. Thêm học sinh")
    print("  2. Xem danh sách")
    print("  3. Tìm học sinh")
    print("  4. Xóa học sinh")
    print("  5. Thống kê")
    print("  6. Sắp xếp danh sách")
    print("  0. Thoát")
    print("="*35)


def main():
    # Thêm dữ liệu mẫu
    students.extend([
        {"ten": "Nguyễn Văn An", "tuoi": 16, "toan": 9.0, "van": 8.5, "anh": 9.5},
        {"ten": "Trần Thị Bình", "tuoi": 17, "toan": 7.0, "van": 8.0, "anh": 6.5},
        {"ten": "Lê Minh Châu",   "tuoi": 16, "toan": 5.5, "van": 6.0, "anh": 5.0},
        {"ten": "Phạm Hoàng Đức", "tuoi": 15, "toan": 10.0, "van": 9.0, "anh": 9.5},
    ])
    
    actions = {
        "1": them_hoc_sinh,
        "2": xem_danh_sach,
        "3": tim_hoc_sinh,
        "4": xoa_hoc_sinh,
        "5": thong_ke,
        "6": sap_xep,
    }
    
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng: ").strip()
        
        if lua_chon == "0":
            print("👋 Tạm biệt!")
            break
        elif lua_chon in actions:
            actions[lua_chon]()
        else:
            print("⚠️ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
