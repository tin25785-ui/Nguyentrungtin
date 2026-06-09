"""
Bài tập 02: Dict lồng nhau 🪆
================================
Mục tiêu: Xử lý dữ liệu phức tạp với nested dict
"""

# TODO 1: Tạo dict lưu thông tin lớp học
# lop = {
#     "An":  {"tuoi": 20, "diem": [8, 9, 7]},
#     "Bình": {"tuoi": 21, "diem": [7, 6, 8]},
#     "Châu": {"tuoi": 20, "diem": [9, 9, 10]},
# }
# a) In điểm trung bình mỗi học sinh
# b) Tìm học sinh có điểm TB cao nhất
# c) Thêm học sinh "Dũng" với tuổi 22, điểm [6, 7, 8]
lop = {
    "An":  {"tuoi": 20, "diem": [8, 9, 7]},
    "Bình": {"tuoi": 21, "diem": [7, 6, 8]},
    "Châu": {"tuoi": 20, "diem": [9, 9, 10]},
}

print("--- a) Điểm trung bình mỗi học sinh ---")
for ten, info in lop.items():
    diem_tb = sum(info["diem"]) / len(info["diem"])
    print(f"{ten}: {diem_tb:.2f}")

print("\n--- b) Học sinh có điểm TB cao nhất ---")
# Sử dụng lambda để tìm key có điểm trung bình cao nhất
hs_gioi_nhat = max(lop, key=lambda x: sum(lop[x]["diem"]) / len(lop[x]["diem"]))
print(f"Học sinh có điểm TB cao nhất là: {hs_gioi_nhat}")

print("\n--- c) Thêm học sinh Dũng ---")
lop["Dũng"] = {"tuoi": 22, "diem": [6, 7, 8]}
print(f"Danh sách lớp sau khi thêm Dũng: {list(lop.keys())}")


# TODO 2: Quản lý sản phẩm
# Tạo dict products với ít nhất 3 sản phẩm
# Mỗi sản phẩm có: ten, gia, so_luong
# Viết hàm: tong_gia_tri_kho(products) → tổng giá × số lượng
products = {
    "p1": {"ten": "Laptop", "gia": 15000000, "so_luong": 5},
    "p2": {"ten": "Chuột", "gia": 200000, "so_luong": 20},
    "p3": {"ten": "Bàn phím", "gia": 500000, "so_luong": 10}
}

def tong_gia_tri_kho(products):
    """Tính tổng giá trị tồn kho của tất cả sản phẩm."""
    return sum(p["gia"] * p["so_luong"] for p in products.values())

tong_gia_tri = tong_gia_tri_kho(products)
print(f"\nTổng giá trị kho: {tong_gia_tri:,} VNĐ")

# TODO 3 (Thử thách): Danh bạ điện thoại
# Tạo dict danh bạ, viết các hàm:
# - them_lien_he(ten, sdt)
# - tim_lien_he(tu_khoa) → tìm theo tên
# - xoa_lien_he(ten)
# - hien_thi_tat_ca()
danh_ba = {}

def them_lien_he(ten, sdt):
    danh_ba[ten] = sdt
    print(f"✅ Đã thêm: {ten} - {sdt}")

def tim_lien_he(tu_khoa):
    ket_qua = {ten: sdt for ten, sdt in danh_ba.items() if tu_khoa.lower() in ten.lower()}
    return ket_qua

def xoa_lien_he(ten):
    if ten in danh_ba:
        del danh_ba[ten]
        print(f"🗑️ Đã xóa liên hệ: {ten}")
    else:
        print(f"❌ Không tìm thấy liên hệ: {ten}")

def hien_thi_tat_ca():
    if not danh_ba:
        print("📭 Danh bạ hiện đang trống.")
        return
    print("\n--- DANH BẠ ĐIỆN THOẠI ---")
    for ten, sdt in danh_ba.items():
        print(f"- {ten}: {sdt}")

print("\n--- Thử nghiệm Thử thách Danh bạ ---")
them_lien_he("Nguyễn Văn An", "0901234567")
them_lien_he("Trần Thị Bình", "0912345678")
hien_thi_tat_ca()
print(f"🔍 Kết quả tìm kiếm 'An': {tim_lien_he('An')}")
xoa_lien_he("Trần Thị Bình")
hien_thi_tat_ca()
