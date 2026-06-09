"""
Bài tập 03: Custom Exception 🏗️
==================================
Mục tiêu: Tạo exception riêng và raise
"""

# TODO 1: Tạo class InsufficientFundsError(Exception)
# Viết hàm rut_tien(so_du, so_tien)
# Raise InsufficientFundsError nếu rút quá số dư 
class InsufficientFundsError(Exception):
    """Ngoại lệ tùy chỉnh khi số dư không đủ để thực hiện giao dịch."""
    def __init__(self, so_du_hien_tai, so_tien_rut):
        self.so_du_hien_tai = so_du_hien_tai
        self.so_tien_rut = so_tien_rut
        message = (f"Không đủ tiền để rút. Số dư hiện tại: {so_du_hien_tai:,} VNĐ, "
                   f"Số tiền muốn rút: {so_tien_rut:,} VNĐ.")
        super().__init__(message)

def rut_tien(so_du, so_tien):
    """
    Thực hiện rút tiền từ tài khoản.
    Raise InsufficientFundsError nếu số tiền rút lớn hơn số dư.
    """
    if so_tien > so_du:
        raise InsufficientFundsError(so_du, so_tien)
    return so_du - so_tien

print("--- TODO 1: Rút tiền an toàn ---")
tai_khoan = 1000000 # 1 triệu VNĐ
print(f"Số dư ban đầu: {tai_khoan:,} VNĐ")

try:
    tai_khoan = rut_tien(tai_khoan, 500000)
    print(f"Rút 500,000 VNĐ thành công. Số dư còn lại: {tai_khoan:,} VNĐ")
    
    tai_khoan = rut_tien(tai_khoan, 800000) # Sẽ gây lỗi
    print(f"Rút 800,000 VNĐ thành công. Số dư còn lại: {tai_khoan:,} VNĐ")
except InsufficientFundsError as e:
    print(f"❌ Lỗi giao dịch: {e}")

# TODO 2: Tạo class InvalidAgeError(Exception)
# Viết hàm kiem_tra_tuoi(tuoi) raise nếu tuổi < 0 hoặc > 150 
class InvalidAgeError(Exception):
    """Ngoại lệ tùy chỉnh khi tuổi nhập vào không hợp lệ."""
    def __init__(self, tuoi):
        self.tuoi = tuoi
        message = f"Tuổi {tuoi} không hợp lệ. Tuổi phải nằm trong khoảng 0-150."
        super().__init__(message)

def kiem_tra_tuoi(tuoi):
    """
    Kiểm tra tính hợp lệ của tuổi.
    Raise TypeError nếu tuổi không phải số nguyên.
    Raise InvalidAgeError nếu tuổi nằm ngoài khoảng 0-150.
    """
    if not isinstance(tuoi, int):
        raise TypeError("Tuổi phải là một số nguyên.")
    if not (0 <= tuoi <= 150):
        raise InvalidAgeError(tuoi)
    print(f"✅ Tuổi {tuoi} hợp lệ.")
    return True

print("\n--- TODO 2: Kiểm tra tuổi ---")
try:
    kiem_tra_tuoi(30)
    kiem_tra_tuoi(-5) # Sẽ gây lỗi
    kiem_tra_tuoi(200) # Sẽ gây lỗi
    kiem_tra_tuoi("hai mươi") # Sẽ gây lỗi
except (InvalidAgeError, TypeError) as e:
    print(f"❌ Lỗi kiểm tra tuổi: {e}")

# TODO 3: Hệ thống đăng ký đơn giản
# Tạo: WeakPasswordError, DuplicateUserError
# Viết hàm dang_ky(username, password, existing_users)
# Raise lỗi phù hợp nếu mật khẩu yếu hoặc user đã tồn tại 
class WeakPasswordError(Exception):
    """Ngoại lệ khi mật khẩu không đủ mạnh."""
    pass

class DuplicateUserError(Exception):
    """Ngoại lệ khi tên người dùng đã tồn tại."""
    pass

def dang_ky(username, password, existing_users):
    """
    Thực hiện đăng ký người dùng mới.
    Raise DuplicateUserError nếu username đã tồn tại.
    Raise WeakPasswordError nếu mật khẩu quá yếu (ví dụ: < 8 ký tự).
    """
    if username in existing_users:
        raise DuplicateUserError(f"Tên người dùng '{username}' đã tồn tại.")
    if len(password) < 8:
        raise WeakPasswordError("Mật khẩu phải có ít nhất 8 ký tự.")
    
    existing_users.add(username)
    print(f"✅ Đăng ký thành công cho người dùng: {username}")

print("\n--- TODO 3: Hệ thống đăng ký ---")
users_da_dang_ky = {"admin", "user123"}

try:
    dang_ky("newuser", "password123", users_da_dang_ky)
    dang_ky("admin", "securepass", users_da_dang_ky) # Sẽ gây lỗi DuplicateUserError
    dang_ky("short", "123", users_da_dang_ky) # Sẽ gây lỗi WeakPasswordError
except (WeakPasswordError, DuplicateUserError) as e:
    print(f"❌ Lỗi đăng ký: {e}")

# TODO 4 (Thử thách): Exception chain
# raise NewError("...") from original_error
print("\n--- TODO 4 (Thử thách): Exception Chaining ---")
def doc_cau_hinh(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        # Bắt lỗi FileNotFoundError và raise một lỗi mới, 
        # nhưng vẫn giữ thông tin về lỗi gốc
        raise ValueError(f"Không thể đọc cấu hình từ '{file_path}'.") from e

try:
    doc_cau_hinh("cau_hinh_khong_ton_tai.txt")
except ValueError as e:
    print(f"❌ Lỗi: {e}")
    if e.__cause__: # Kiểm tra xem có lỗi gốc không
        print(f"   Nguyên nhân gốc: {e.__cause__}")
