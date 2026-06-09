"""
Bài tập 02: Nhiều loại Exception 🎯
=====================================
Mục tiêu: Xử lý nhiều lỗi, dùng else và finally
"""

# TODO 1: Viết chương trình đọc file và chia số
# try:
#     Đọc file chứa 2 số → chia số 1 cho số 2
# except FileNotFoundError: ...
# except ValueError: ...
# except ZeroDivisionError: ...
# else: in kết quả
# finally: in "Hoàn tất"
print("--- TODO 1: Đọc file và chia số ---")
filename = "numbers.txt"
# Tạo file mẫu để test nếu chưa có
with open(filename, "w") as f:
    f.write("100\n20")

try:
    with open(filename, "r") as f:
        lines = f.readlines()
        if len(lines) < 2:
            raise ValueError("File không đủ dữ liệu để chia.")
        num1 = float(lines[0].strip())
        num2 = float(lines[1].strip())
        result = num1 / num2
except FileNotFoundError:
    print(f"❌ Lỗi: Không tìm thấy file '{filename}'.")
except ValueError as e:
    print(f"❌ Lỗi dữ liệu: {e}")
except ZeroDivisionError:
    print("❌ Lỗi: Không thể chia cho số 0.")
else:
    print(f"✅ Kết quả chia: {result}")
finally:
    print("🔔 Hoàn tất xử lý file.")

# TODO 2: Viết hàm get_value(data, key, index)
# data = {"scores": [85, 92, 78]}
# get_value(data, "scores", 1) → 92
# Xử lý: KeyError, IndexError, TypeError
def get_value(data, key, index):
    try:
        return data[key][index]
    except KeyError:
        print(f"❌ Lỗi: Key '{key}' không tồn tại.")
    except IndexError:
        print(f"❌ Lỗi: Chỉ số {index} nằm ngoài phạm vi danh sách.")
    except TypeError:
        print("❌ Lỗi: Dữ liệu không đúng cấu trúc (không phải dict/list).")
    return None

print("\n--- TODO 2: Truy cập dữ liệu an toàn ---")
data = {"scores": [85, 92, 78]}
print(f"Giá trị tìm được: {get_value(data, 'scores', 1)}")
get_value(data, "grades", 0)  # Test KeyError

# TODO 3: Nhập liệu an toàn (lặp đến khi đúng)
# Viết hàm get_float(prompt) hỏi người dùng nhập float
# Lặp lại nếu nhập sai, trả về khi nhập đúng
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Giá trị không hợp lệ. Vui lòng nhập một số thực!")

print("\n--- TODO 3: Nhập liệu an toàn ---")
# f = get_float("Nhập một số thực bất kỳ: ")
# print(f"Bạn đã nhập: {f}")

# TODO 4 (Thử thách): Decorator xử lý lỗi
# Viết decorator @safe_call in lỗi thay vì crash
import functools

def safe_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"⚠️ [Safe Call] Đã chặn crash trong '{func.__name__}': {e}")
            return None
    return wrapper

@safe_call
def chia_nguy_hiem(a, b):
    return a / b

print("\n--- TODO 4: Decorator xử lý lỗi ---")
chia_nguy_hiem(10, 0) # Sẽ không crash, chỉ in cảnh báo
