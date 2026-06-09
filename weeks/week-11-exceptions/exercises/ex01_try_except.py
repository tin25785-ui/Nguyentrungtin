"""
Bài tập 01: try/except cơ bản 🛡️
====================================
Mục tiêu: Bắt lỗi cơ bản với try/except
"""

# TODO 1: Nhập số từ người dùng, chia 100 cho số đó
# Xử lý: ValueError (nhập chữ), ZeroDivisionError (nhập 0)
try:
    number = int(input("Nhập một số: "))
    result = 100 / number
    print(f"Kết quả 100 / {number} là: {result}")
except ValueError:
    print("Lỗi: Vui lòng nhập một con số hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0!")

# TODO 2: Nhập index, truy cập phần tử trong list
# fruits = ["apple", "banana", "cherry"]
# Xử lý: IndexError (index ngoài phạm vi), ValueError (nhập chữ)
fruits = ["apple", "banana", "cherry"]
try:
    index = int(input(f"Nhập vị trí bạn muốn lấy (0-{len(fruits)-1}): "))
    print(f"Trái cây tại vị trí {index} là: {fruits[index]}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên cho vị trí!")
except IndexError:
    print(f"Lỗi: Vị trí không tồn tại! Vui lòng nhập từ 0 đến {len(fruits)-1}.")

# TODO 3: Viết hàm safe_divide(a, b)
# Trả về kết quả chia, hoặc None nếu chia cho 0
# Dùng try/except
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Chạy thử TODO 3
print(f"safe_divide(10, 2): {safe_divide(10, 2)}")
print(f"safe_divide(10, 0): {safe_divide(10, 0)}")

# TODO 4: Đọc file không tồn tại
# Xử lý FileNotFoundError, in thông báo thân thiện
try:
    with open("du_lieu_bi_mat.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("Thông báo: Rất tiếc, file 'du_lieu_bi_mat.txt' không tồn tại trên hệ thống.")

# TODO 5 (Thử thách): Viết hàm safe_int(text, default=0)
# Chuyển text sang int, trả default nếu không chuyển được
def safe_int(text, default=0):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default

# Chạy thử TODO 5
print(f"safe_int('123'): {safe_int('123')}")
print(f"safe_int('abc', default=-1): {safe_int('abc', default=-1)}")
print(f"safe_int(None): {safe_int(None)}")
