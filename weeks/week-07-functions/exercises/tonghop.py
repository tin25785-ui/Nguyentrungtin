"""
Bài tập tổng hợp về Hàm (Functions) trong Python.
Mục tiêu:
- Định nghĩa và gọi hàm với `def`.
- Hiểu tham số, đối số và `return`.
- Dùng tham số mặc định và keyword arguments.
- Hiểu phạm vi biến (scope): local vs global.
- Viết docstring chuyên nghiệp.
- So sánh sự khác biệt và giống nhau với C++ về hàm.
"""

import math

# --- 1. Định nghĩa và gọi hàm với `def`, tham số, đối số và `return` ---

def chao_mung(ten):
    """
    In ra lời chào mừng tới một người cụ thể.
    Đây là một hàm không có giá trị trả về (tương đương `void` trong C++).

    Args:
        ten (str): Tên của người cần chào mừng.
    """
    print(f"Xin chào, {ten}! Rất vui được gặp bạn.")

def tinh_tong(a, b):
    """
    Tính tổng của hai số.
    Đây là một hàm có giá trị trả về (tương đương `int`, `float`... trong C++).

    Args:
        a (int/float): Số thứ nhất.
        b (int/float): Số thứ hai.

    Returns:
        int/float: Tổng của a và b.
    """
    return a + b

print("--- Ví dụ 1: Hàm cơ bản (def, tham số, return) ---")
# Gọi hàm không có return
chao_mung("Alice")
chao_mung("Bob")

# Gọi hàm có return và lưu kết quả
ket_qua_tong = tinh_tong(10, 20)
print(f"Tổng của 10 và 20 là: {ket_qua_tong}")

# So sánh với C++:
# Trong C++, bạn sẽ khai báo `void chao_mung(string ten)` và `int tinh_tong(int a, int b)`.
# Python linh hoạt hơn, không cần khai báo kiểu trả về tường minh trong định nghĩa hàm.
# Hàm không có `return` sẽ tự động trả về `None` (tương tự `void` trong C++ không trả về giá trị nào cụ thể).
ket_qua_chao = chao_mung("Charlie")
print(f"Giá trị trả về của hàm chao_mung là: {ket_qua_chao} (kiểu {type(ket_qua_chao)})")
print("Điều này tương tự như hàm `void` trong C++ không trả về giá trị nào cụ thể.")


# --- 2. Tham số mặc định và keyword arguments ---

def thong_tin_nguoi_dung(ten, tuoi=30, thanh_pho="Hà Nội"):
    """
    Hiển thị thông tin của một người dùng với các tham số mặc định.

    Args:
        ten (str): Tên của người dùng (tham số bắt buộc).
        tuoi (int, optional): Tuổi của người dùng. Mặc định là 30.
        thanh_pho (str, optional): Thành phố nơi người dùng sống. Mặc định là "Hà Nội".
    """
    print(f"Tên: {ten}, Tuổi: {tuoi}, Thành phố: {thanh_pho}")

print("\n--- Ví dụ 2: Tham số mặc định và keyword arguments ---")
# Gọi hàm chỉ với tham số bắt buộc (sử dụng giá trị mặc định cho tuổi và thành phố)
thong_tin_nguoi_dung("Minh")

# Gọi hàm ghi đè tham số mặc định theo vị trí
thong_tin_nguoi_dung("Lan", 25)

# Gọi hàm ghi đè tham số mặc định bằng keyword arguments (có thể thay đổi thứ tự)
thong_tin_nguoi_dung("Hoa", thanh_pho="Đà Nẵng", tuoi=22)
thong_tin_nguoi_dung(ten="Quang", tuoi=40) # Rõ ràng hơn khi dùng keyword arguments


# --- 3. Phạm vi biến (scope): local vs global ---

bien_global = "Tôi là biến toàn cục (global variable)"

def ham_local_scope():
    """
    Hàm này minh họa biến cục bộ (local scope).
    """
    bien_local = "Tôi là biến cục bộ (local variable) bên trong ham_local_scope"
    print(f"Trong ham_local_scope: {bien_local}")
    print(f"Trong ham_local_scope, có thể truy cập biến global: {bien_global}")
    # Nếu gán bien_global = "giá trị mới" ở đây mà không dùng `global`,
    # Python sẽ tạo một biến local mới tên là bien_global, không ảnh hưởng đến biến global bên ngoài.

def ham_thay_doi_global():
    """
    Hàm này minh họa cách thay đổi biến toàn cục bằng từ khóa `global`.
    """
    global bien_global # Khai báo rằng ta muốn làm việc với biến global
    print(f"Trước khi thay đổi trong hàm: {bien_global}")
    bien_global = "Giá trị của biến global đã bị thay đổi bởi ham_thay_doi_global"
    print(f"Sau khi thay đổi trong hàm: {bien_global}")

print("\n--- Ví dụ 3: Phạm vi biến (Scope) ---")
print(f"Ngoài hàm (ban đầu): {bien_global}")

ham_local_scope()
# print(bien_local) # Lỗi: NameError, bien_local chỉ tồn tại trong ham_local_scope

print(f"Ngoài hàm (sau ham_local_scope): {bien_global}") # bien_global không thay đổi

ham_thay_doi_global()
print(f"Ngoài hàm (sau ham_thay_doi_global): {bien_global}") # bien_global đã thay đổi

# So sánh với C++:
# Trong C++, biến khai báo ngoài hàm là global. Biến khai báo trong hàm là local.
# Để thay đổi biến global trong C++, bạn chỉ cần truy cập nó (nếu nó không bị che bởi biến local cùng tên).
# Python yêu cầu từ khóa `global` để gán lại giá trị cho biến global từ bên trong hàm,
# nếu không, nó sẽ tạo một biến local mới.


# --- 4. Docstring chuyên nghiệp ---

def tinh_bmi(can_nang: float, chieu_cao: float) -> float:
    """
    Tính chỉ số BMI (Body Mass Index) của một người.

    Args:
        can_nang (float): Cân nặng của người đó tính bằng kilogram (kg).
        chieu_cao (float): Chiều cao của người đó tính bằng mét (m).

    Returns:
        float: Chỉ số BMI làm tròn đến 2 chữ số thập phân.

    Raises:
        ValueError: Nếu `can_nang` hoặc `chieu_cao` nhỏ hơn hoặc bằng 0.

    Example:
        >>> tinh_bmi(70, 1.75)
        22.86
        >>> tinh_bmi(60, 1.60)
        23.44
    """
    if can_nang <= 0 or chieu_cao <= 0:
        raise ValueError("Cân nặng và chiều cao phải là số dương.")
    bmi = can_nang / (chieu_cao ** 2)
    return round(bmi, 2)

print("\n--- Ví dụ 4: Docstring chuyên nghiệp và sử dụng hàm với docstring ---")
try:
    bmi_an = tinh_bmi(70, 1.75)
    print(f"BMI của An (70kg, 1.75m) là: {bmi_an}")
    bmi_binh = tinh_bmi(65, 1.68)
    print(f"BMI của Bình (65kg, 1.68m) là: {bmi_binh}")

    # Thử gọi với giá trị không hợp lệ để xem Raise hoạt động
    # tinh_bmi(0, 1.70)
except ValueError as e:
    print(f"Lỗi khi tính BMI: {e}")

# Bạn có thể xem docstring bằng cách:
# print(tinh_bmi.__doc__)
# help(tinh_bmi)