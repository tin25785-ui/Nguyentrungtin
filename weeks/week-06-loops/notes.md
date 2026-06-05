# Tuần 06 — Vòng Lặp: for và while 🔄

## 1. Vòng lặp `for` (Duyệt theo tập hợp)
Dùng khi bạn biết trước số lần lặp hoặc muốn duyệt qua một danh sách (list, tuple, string).

```python
fruits = ["táo", "chuối", "cam"]
for fruit in fruits:
    print(f"Tôi thích ăn {fruit}")
```

### Hàm `range()`
- `range(5)`: 0, 1, 2, 3, 4
- `range(1, 6)`: 1, 2, 3, 4, 5
- `range(1, 10, 2)`: 1, 3, 5, 7, 9 (bước nhảy là 2)

## 2. Vòng lặp `while` (Duyệt theo điều kiện)
Dùng khi bạn không biết trước số lần lặp, vòng lặp chạy chừng nào điều kiện còn đúng (`True`).

```python
count = 1
while count <= 5:
    print(f"Lần thứ {count}")
    count += 1
```

## 3. Điều khiển vòng lặp
- `break`: Thoát khỏi vòng lặp ngay lập tức.
- `continue`: Bỏ qua các dòng lệnh còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo.

## 4. Vòng lặp lồng nhau (Nested Loops)
Dùng để xử lý dữ liệu đa chiều (như ma trận hoặc bảng cửu chương).

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()
```

## 5. List Comprehension (Nâng cao)
Cách viết ngắn gọn để tạo list mới từ một vòng lặp.
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers] # [1, 4, 9, 16, 25]
```

---
### 🔑 Ghi nhớ:
1. **`for`**: Dùng cho dãy số hoặc danh sách có sẵn.
2. **`while`**: Dùng khi chờ đợi một sự kiện xảy ra (như người dùng nhập đúng mật khẩu).
3. **Vô hạn (Infinite loop)**: Cẩn thận với `while True` mà không có điểm dừng (`break`).