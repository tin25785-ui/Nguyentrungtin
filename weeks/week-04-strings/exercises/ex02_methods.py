"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print(email.strip().lower())


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print(sentence.title())
print(sentence.count("o"))
print(sentence.replace("python", "PYTHON"))


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ")
parts = ho_ten.split()
if len(parts) >= 2:
    print(f"Họ: {parts[0]}, Tên: {parts[-1]}")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
filename = input("Nhập tên file: ")
print(f"Hợp lệ: {filename.endswith(('.py', '.txt', '.csv'))}")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
text = input("Nhập chuỗi cần mã hóa: ")
shift = int(input("Nhập bước dịch (shift): "))
encoded = ""
for char in text:
    if char.isalpha():
        start = ord('a') if char.islower() else ord('A')
        encoded += chr(start + (ord(char) - start + shift) % 26)
    else:
        encoded += char
print(f"Mã hóa Caesar: {encoded}")
