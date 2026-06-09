"""
Bài tập 03: Scope & Module hóa 🏗️
====================================
Mục tiêu: Hiểu local/global scope, tổ chức code
"""

# TODO 1: Đọc code sau và dự đoán output TRƯỚC KHI chạy
x = 10
def thay_doi():
    x = 20
    print(f"Trong hàm: x = {x}")

thay_doi()
print(f"Ngoài hàm: x = {x}")
# Dự đoán: 
# Trong hàm: x = 20
# Ngoài hàm: x = 10
# Giải thích: 'x' trong hàm là biến local, không ảnh hưởng đến biến 'x' global ở ngoài.


# TODO 2: Viết chương trình "Sổ tay đơn giản"
def them_ghi_chu(danh_sach, noi_dung):
    """Thêm một nội dung mới vào danh sách ghi chú."""
    danh_sach.append(noi_dung)
    print("✅ Đã thêm ghi chú mới.")

def xem_ghi_chu(danh_sach):
    """In ra toàn bộ danh sách ghi chú."""
    if not danh_sach:
        print("📭 Sổ tay hiện đang trống.")
        return
    print("\n--- DANH SÁCH GHI CHÚ ---")
    for i, gc in enumerate(danh_sach, 1):
        print(f"{i}. {gc}")

def tim_ghi_chu(danh_sach, tu_khoa):
    """Tìm kiếm ghi chú có chứa từ khóa nhất định."""
    ket_qua = [gc for gc in danh_sach if tu_khoa.lower() in gc.lower()]
    if not ket_qua:
        print(f"🔍 Không tìm thấy kết quả nào cho: '{tu_khoa}'")
    else:
        print(f"🔍 Tìm thấy {len(ket_qua)} ghi chú:")
        for gc in ket_qua:
            print(f"  - {gc}")

def menu():
    """Menu điều khiển chương trình sổ tay."""
    so_tay = ["Học Python cơ bản", "Mua sữa cho bé"]
    while True:
        print("\n--- MENU SỔ TAY ---")
        print("1. Thêm ghi chú")
        print("2. Xem tất cả")
        print("3. Tìm kiếm")
        print("4. Thoát")
        chon = input("Chọn chức năng (1-4): ")
        
        if chon == '1':
            nd = input("Nhập nội dung ghi chú: ")
            them_ghi_chu(so_tay, nd)
        elif chon == '2':
            xem_ghi_chu(so_tay)
        elif chon == '3':
            tk = input("Nhập từ khóa cần tìm: ")
            tim_ghi_chu(so_tay, tk)
        elif chon == '4':
            print("Đã thoát chương trình Sổ tay.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng thử lại.")


# TODO 3 (Thử thách): Viết module my_math.py riêng
import my_math

def test_my_math():
    print("\n--- KIỂM TRA MODULE MY_MATH ---")
    print(f"10 + 5 = {my_math.cong(10, 5)}")
    print(f"10 - 7 = {my_math.tru(10, 7)}")
    print(f"4 * 3  = {my_math.nhan(4, 3)}")
    print(f"10 / 2 = {my_math.chia(10, 2)}")
    print(f"2 ^ 5  = {my_math.luy_thua(2, 5)}")

if __name__ == "__main__":
    # Gọi hàm menu hoặc test_my_math để chạy thử
    # menu()
    test_my_math()
