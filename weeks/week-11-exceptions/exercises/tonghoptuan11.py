
"""
====================================================
    TỔNG HỢP TUẦN 11 - EXCEPTION (XỬ LÝ NGOẠI LỆ)
====================================================

Exception là lỗi xảy ra khi chương trình đang chạy.

Ví dụ:
- Chia cho 0
- Nhập chữ thay vì số
- Mở file không tồn tại
- Truy cập biến chưa khai báo

Mục đích:
- Không để chương trình bị crash
- Hiển thị thông báo dễ hiểu
- Làm chương trình mạnh hơn (Robust)
"""

# ==================================================
# 1. KHÔNG XỬ LÝ LỖI
# ==================================================

print("===== Ví dụ 1: Không xử lý lỗi =====")

# Ví dụ này đang được comment để chương trình không dừng

# a = 10
# b = 0
# print(a / b)

# Kết quả:
# ZeroDivisionError
# Chương trình sẽ dừng ngay.


# ==================================================
# 2. TRY - EXCEPT
# ==================================================

print("\n===== Ví dụ 2: try - except =====")

try:

    # Thử thực hiện phép chia

    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:

    # Nếu chia cho 0 thì chạy vào đây

    print("Lỗi: Không thể chia cho 0")


# ==================================================
# 3. NHẬP DỮ LIỆU AN TOÀN
# ==================================================

print("\n===== Ví dụ 3: Nhập số =====")

try:

    number = int(input("Nhập một số: "))

    print("Bạn vừa nhập:", number)

except ValueError:

    print("Lỗi: Bạn phải nhập số")


# ==================================================
# 4. BẮT NHIỀU LOẠI LỖI
# ==================================================

print("\n===== Ví dụ 4: Bắt nhiều lỗi =====")

try:

    n = int(input("Nhập một số để chia 10: "))

    result = 10 / n

    print("Kết quả:", result)

except ValueError:

    print("Lỗi: Phải nhập số")

except ZeroDivisionError:

    print("Lỗi: Không được nhập số 0")


# ==================================================
# 5. ELSE
# ==================================================

print("\n===== Ví dụ 5: else =====")

try:

    x = int(input("Nhập số: "))

except ValueError:

    print("Bạn nhập sai")

else:

    # Chỉ chạy khi không có lỗi

    print("Bạn nhập đúng")


# ==================================================
# 6. FINALLY
# ==================================================

print("\n===== Ví dụ 6: finally =====")

try:

    print(10 / 2)

except:

    print("Có lỗi")

finally:

    # Luôn luôn chạy

    print("Kết thúc chương trình")


# ==================================================
# 7. TRY - EXCEPT - ELSE - FINALLY
# ==================================================

print("\n===== Ví dụ 7: Đầy đủ =====")

try:

    number = int(input("Nhập số: "))

    result = 100 / number

except ValueError:

    print("Bạn phải nhập số")

except ZeroDivisionError:

    print("Không được nhập số 0")

else:

    print("Kết quả là:", result)

finally:

    print("Đã xử lý xong")


# ==================================================
# 8. RAISE
# ==================================================

print("\n===== Ví dụ 8: raise =====")

age = -5

try:

    if age < 0:

        # Tự tạo lỗi

        raise ValueError(
            "Tuổi không được âm"
        )

except ValueError as e:

    print(e)


# ==================================================
# 9. CUSTOM EXCEPTION
# ==================================================

print("\n===== Ví dụ 9: Custom Exception =====")

# Tạo loại lỗi mới

class TuoiKhongHopLeError(Exception):

    pass


# Hàm kiểm tra tuổi

def kiem_tra_tuoi(tuoi):

    if tuoi < 0 or tuoi > 150:

        raise TuoiKhongHopLeError(
            "Tuổi không hợp lệ"
        )

    print("Đăng ký thành công")


try:

    kiem_tra_tuoi(200)

except TuoiKhongHopLeError as e:

    print(e)


# ==================================================
# 10. CHƯƠNG TRÌNH ROBUST
# ==================================================

print("\n===== Ví dụ 10: Robust Program =====")

while True:

    try:

        value = int(
            input("Nhập số nguyên: ")
        )

        break

    except ValueError:

        print("Sai định dạng")
        print("Mời nhập lại")

print("Bạn vừa nhập:", value)


# ==================================================
# 11. EXCEPTION CHAINING
# ==================================================

print("\n===== Ví dụ 11: Exception Chaining =====")

def doc_file():

    try:

        open("abc.txt")

    except FileNotFoundError as loi_goc:

        raise RuntimeError(
            "Lỗi hệ thống"
        ) from loi_goc


try:

    doc_file()

except RuntimeError as e:

    print("Lỗi:", e)

    print("Nguyên nhân gốc:")

    print(e.__cause__)


# ==================================================
# 12. ĐÓNG FILE BẰNG FINALLY
# ==================================================

print("\n===== Ví dụ 12: Đóng file =====")

try:

    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("Không tìm thấy file")

finally:

    try:

        file.close()

        print("Đã đóng file")

    except:

        pass


# ==================================================
# 13. CHƯƠNG TRÌNH TỔNG HỢP
# ==================================================

print("\n===== Ví dụ 13: Tổng hợp =====")

class TuoiError(Exception):

    pass

while True:

    try:

        tuoi = int(
            input("Nhập tuổi của bạn: ")
        )

        if tuoi < 0 or tuoi > 150:

            raise TuoiError(
                "Tuổi phải từ 0 đến 150"
            )

    except ValueError:

        print("Bạn phải nhập số")

    except TuoiError as e:

        print(e)

    else:

        print("Đăng ký thành công")

        break

    finally:

        print("Đã kiểm tra")


# ==================================================
# 14. TÓM TẮT
# ==================================================

print("\n==============================")
print("TÓM TẮT KIẾN THỨC")
print("==============================")

print("try     : Thử chạy")
print("except  : Bắt lỗi")
print("else    : Không lỗi thì chạy")
print("finally : Luôn luôn chạy")
print("raise   : Tự tạo lỗi")
print("Exception : Lỗi khi chương trình chạy")

print("\nHoàn thành Tuần 11 Exception!")

