"""
TỔNG HỢP KIẾN THỨC TUẦN 11: XỬ LÝ NGOẠI LỆ (EXCEPTIONS) 🛡️
=======================================================
Mục tiêu: Viết code "robust" (vững chãi), không crash bất ngờ.
"""

# 1. EXCEPTION LÀ GÌ? TẠI SAO CẦN XỬ LÝ?
# Exception là sự cố xảy ra khi chương trình đang chạy (Runtime).
# Nếu không xử lý, chương trình sẽ dừng ngay lập tức (Crash).
# Xử lý lỗi giúp ta đưa ra thông báo nhẹ nhàng thay vì để màn hình hiện lỗi đỏ lòm.

# 2. CẤU TRÚC ĐẦY ĐỦ: try - except - else - finally
print("--- 1. Ví dụ đầy đủ về cấu trúc xử lý lỗi ---")
def doc_so():
    try:
        # Code có khả năng gây lỗi đặt ở đây
        n = int(input("Nhập một số nguyên để chia 10: "))
        ket_qua = 10 / n
    except ValueError:
        # Chạy khi người dùng nhập chữ thay vì số
        print("❌ Lỗi: Bạn phải nhập số nguyên!")
    except ZeroDivisionError:
        # Chạy khi n = 0
        print("❌ Lỗi: Không thể chia cho số không!")
    else:
        # CHỈ CHẠY KHI KHÔNG CÓ LỖI (Try thành công)
        print(f"✅ Tuyệt vời! Kết quả là: {ket_qua}")
    finally:
        # LUÔN LUÔN CHẠY (Dùng để dọn dẹp, đóng file, giải phóng bộ nhớ)
        print("🔔 Kết thúc giao dịch.")

# doc_so()


# 3. CUSTOM EXCEPTION (Tạo lỗi riêng của bạn)
# Giúp code rõ nghĩa hơn cho các logic nghiệp vụ cụ thể.
print("\n--- 2. Custom Exception ---")

class TuoiKhongHopLeError(Exception):
    """Lỗi khi tuổi nằm ngoài khoảng 0-150."""
    pass

def kiem_tra_dang_ky(tuoi):
    if tuoi < 0 or tuoi > 150:
        # Chủ động ném lỗi (raise)
        raise TuoiKhongHopLeError(f"Tuổi {tuoi} là vô lý!")
    print(f"✅ Đăng ký thành công với {tuoi} tuổi.")

try:
    kiem_tra_dang_ky(200)
except TuoiKhongHopLeError as e:
    print(f"⚠️ Chặn lỗi nghiệp vụ: {e}")


# 4. SO SÁNH VỚI C++ (CHO LẬP TRÌNH VIÊN)
# ==========================================
"""
Đặc điểm         | Python (Exception)            | C++ (Exception)
----------------|-------------------------------|----------------------------------
Cú pháp chính    | try ... except                | try ... catch
Bắt mọi lỗi      | except Exception:             | catch (...)
Khối Else        | Có (chạy khi không lỗi)       | Không có (phải tự viết logic)
Khối Finally     | Có (luôn chạy)                | Không có (thường dùng RAII/Destructor)
Ném lỗi          | raise ValueError("msg")       | throw std::invalid_argument("msg")
Tạo lỗi riêng    | Kế thừa class Exception       | Kế thừa std::exception
Hệ thống lỗi     | Rất phong phú, dùng thường xuyên| Thường dùng cho lỗi nghiêm trọng

Ghi chú cho bạn:
1. Khối 'else' trong Python rất hay, giúp tách biệt code "chạy đúng" ra khỏi khối 'try' 
   để tránh việc bắt nhầm lỗi của các dòng code không liên quan.
   
2. Khối 'finally' trong Python cực kỳ quan trọng vì Python không có cơ chế Destructor 
   tự động giải phóng ngay lập tức như C++ (RAII). Bạn dùng nó để đảm bảo file luôn 
   được đóng (.close()) dù code có lỗi hay không.
"""

# 5. VÍ DỤ CHƯƠNG TRÌNH ROBUST (CHỐNG CRASH)
print("\n--- 3. Ví dụ Robust Program (Nhập đến khi đúng) ---")
def get_safe_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("⚠️ Sai định dạng, mời nhập lại số nguyên.")

# tuoi = get_safe_int("Nhập tuổi của bạn: ")
# print(f"Xác nhận tuổi: {tuoi}")


# 6. EXCEPTION CHAINING (Ném lỗi kèm dấu vết)
print("\n--- 4. Exception Chaining ---")
def xu_ly_du_lieu():
    try:
        # Giả sử lỗi đọc file
        open("file_khong_co.txt")
    except FileNotFoundError as original_error:
        # Ném lỗi mới nhưng vẫn giữ lại nguyên nhân gốc (from)
        raise RuntimeError("Hệ thống dữ liệu bị lỗi") from original_error

try:
    # xu_ly_du_lieu()
    pass
except RuntimeError as e:
    print(f"Lỗi tầng trên: {e}")
    print(f"Nguyên nhân gốc: {e.__cause__}")

if __name__ == "__main__":
    print("\n[Hoàn thành tổng hợp Tuần 11]")