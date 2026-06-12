
# ===================================================
# TỔNG HỢP HÀM (FUNCTIONS) TRONG PYTHON
# ===================================================

# Import thư viện toán học
# Muốn dùng các hàm như sqrt(), pi, pow() thì phải import
import math


# ===================================================
# 1. HÀM (FUNCTION)
# ===================================================

# Tạo một hàm tên hello
def hello():

    # In ra màn hình
    print("Xin chào Python")


# Gọi hàm để chạy
hello()


# ===================================================
# 2. THAM SỐ (PARAMETER) VÀ ĐỐI SỐ (ARGUMENT)
# ===================================================

# name là THAM SỐ
# Tham số là biến được khai báo khi tạo hàm
def show_name(name):

    print("Xin chào", name)


# "Tin" là ĐỐI SỐ
# Đối số là giá trị truyền vào khi gọi hàm
show_name("Tin")


# ===================================================
# 3. RETURN
# ===================================================

# Hàm cộng hai số
def add(a, b):

    # Trả kết quả về nơi gọi hàm
    return a + b


# Gọi hàm
# x sẽ nhận giá trị trả về
x = add(5, 3)

print(x)

# Quá trình:
#
# add(5,3)
#    ↓
# 5 + 3 = 8
#    ↓
# return 8
#    ↓
# x = 8


# ===================================================
# 4. PRINT KHÁC RETURN
# ===================================================

def sum_number(a, b):

    # Chỉ in ra màn hình
    print(a + b)


y = sum_number(5, 3)

# Hàm không có return
# Python tự trả về None
print(y)

# Kết quả:
#
# 8
# None


# ===================================================
# 5. THAM SỐ MẶC ĐỊNH (DEFAULT PARAMETER)
# ===================================================

def greet(name, message="Chào bạn"):

    print(message, name)


# Không truyền message
# Python dùng giá trị mặc định
greet("Tin")

# Có truyền message
# Python dùng giá trị mới
greet("Tin", "Chúc bạn học tốt")


# ===================================================
# 6. KEYWORD ARGUMENTS
# ===================================================

def create_account(username, password, role="user"):

    print("Username:", username)
    print("Password:", password)
    print("Role:", role)


# Truyền dữ liệu theo tên biến
# Không cần đúng thứ tự
create_account(
    password="123456",
    username="Tin",
    role="admin"
)


# ===================================================
# 7. SCOPE (PHẠM VI BIẾN)
# ===================================================

# x được tạo ngoài hàm
# => Global Variable
x = 100


def test():

    # y được tạo trong hàm
    # => Local Variable
    y = 10

    print(x)
    print(y)


test()

# x là Global nên dùng được
print(x)

# print(y)
# Lỗi vì y là Local
# y chỉ tồn tại trong hàm test()


# ===================================================
# 8. TỪ KHÓA GLOBAL
# ===================================================

count = 0


def increase():

    # Cho phép sửa biến Global
    global count

    count += 1


increase()
increase()

print(count)

# Kết quả:
# 2


# ===================================================
# 9. DOCSTRING
# ===================================================

def square(number):
    """
    Hàm tính bình phương của một số.

    Args:
        number: Số cần tính.

    Returns:
        Bình phương của số.
    """

    return number ** 2


print(square(5))


# ===================================================
# 10. HÀM TÍNH GIAI THỪA
# ===================================================

def factorial(n):

    result = 1

    for i in range(1, n + 1):

        result *= i

    return result


print(factorial(5))

# Quá trình:
#
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120


# ===================================================
# 11. IMPORT MATH
# ===================================================

# Căn bậc hai
print(math.sqrt(25))

# Lũy thừa
print(math.pow(2, 3))

# Số PI
print(math.pi)

# Làm tròn lên
print(math.ceil(4.2))

# Làm tròn xuống
print(math.floor(4.9))


# ===================================================
# KIẾN THỨC CẦN NHỚ
# ===================================================

# def
# -> Dùng để tạo hàm

# Function
# -> Đoạn code thực hiện một công việc

# Parameter (Tham số)
# -> Biến khai báo trong hàm
# -> Giống như cái hộp trống

# Argument (Đối số)
# -> Giá trị truyền vào hàm
# -> Giống như đồ bỏ vào hộp

# print
# -> Chỉ in ra màn hình

# return
# -> Trả kết quả về để dùng tiếp

# Default Parameter
# -> Tham số có giá trị mặc định

# Keyword Arguments
# -> Truyền dữ liệu theo tên biến

# Local Variable
# -> Biến tạo trong hàm
# -> Chỉ dùng trong hàm

# Global Variable
# -> Biến tạo ngoài hàm
# -> Dùng được nhiều nơi

# global
# -> Cho phép sửa biến Global trong hàm

# Docstring
# -> Mô tả chức năng của hàm

# import math
# -> Nạp thư viện toán học

