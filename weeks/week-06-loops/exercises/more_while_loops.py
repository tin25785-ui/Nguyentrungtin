"""
CÁC VÍ DỤ NÂNG CAO VỀ VÒNG LẶP WHILE ⏳
======================================
File này giúp bạn thành thạo cách điều khiển luồng chương trình bằng điều kiện.
"""

# 1. Vòng lặp While cơ bản (Dùng biến đếm)
print("--- 1. Đếm số lần thực hiện ---")
count = 1
while count <= 3:
    print(f"Đây là lần lặp thứ {count}")
    count += 1  # Quan trọng: Phải thay đổi điều kiện để không bị lặp vô tận


# 2. Sử dụng "Sentinel Value" (Giá trị lính canh)
# Lặp cho đến khi người dùng nhập một giá trị cụ thể để dừng
print("\n--- 2. Nhập dữ liệu cho đến khi gõ 'quit' ---")
message = ""
while message.lower() != 'quit':
    message = input("Nhập tin nhắn (hoặc 'quit' để dừng): ")
    if message.lower() != 'quit':
        print(f">> Bạn vừa nói: {message}")


# 3. Vòng lặp While True và Break (Mẫu thiết kế menu)
print("\n--- 3. Sử dụng While True để tạo vòng lặp vô hạn có kiểm soát ---")
while True:
    print("\n[1] Nói xin chào")
    print("[2] Thoát")
    choice = input("Chọn chức năng: ")
    
    if choice == '1':
        print("Xin chào bạn! Chúc một ngày tốt lành.")
    elif choice == '2':
        print("Đang thoát chương trình...")
        break  # Thoát hẳn vòng lặp ngay lập tức
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


# 4. Sử dụng While với Else (Một tính năng đặc biệt của Python)
# Khối else sẽ chạy khi điều kiện while trở thành False (không bị ngắt bởi break)
print("\n--- 4. Kết hợp While - Else ---")
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
else:
    print("\nĐã đếm xong về 0, khối else được thực thi!")


# 5. Xử lý phần tử trong List bằng While (Dùng pop)
print("\n--- 5. Chuyển đổi dữ liệu giữa 2 danh sách ---")
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # Lấy phần tử cuối ra
    print(f"Đang xác thực người dùng: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"Danh sách đã xác thực: {confirmed_users}")

"""
GHI CHÚ VỀ VÒNG LẶP WHILE:

1.  Khi nào dùng While?: 
    - Khi bạn chờ đợi một sự kiện (người dùng nhập đúng mật khẩu, cảm biến trả về giá trị...).
    - Khi bạn duyệt và sửa đổi danh sách (như ví dụ 5 dùng .pop()).

2.  Lỗi lặp vô tận (Infinite Loop): 
    Đây là lỗi phổ biến nhất. Hãy luôn đảm bảo biến điều kiện (ví dụ: `count`) 
    được cập nhật bên trong thân vòng lặp.

3.  While vs For:
    - For: Dùng khi biết "Duyệt qua bao nhiêu phần tử".
    - While: Dùng khi biết "Lặp cho đến khi nào điều kiện này sai".
"""