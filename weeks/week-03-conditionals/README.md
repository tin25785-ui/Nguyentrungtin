# Tuần 03: Câu lệnh điều kiện 🔀

> *"Cuộc sống là tổng của tất cả những lựa chọn của bạn." — Albert Camus*

## 🎯 Mục tiêu tuần này

Sau tuần này, bạn sẽ:

- Viết câu lệnh `if/elif/else` đúng cú pháp
- Dùng toán tử so sánh: `==` `!=` `>` `<` `>=` `<=`
- Dùng toán tử logic: `and`, `or`, `not`
- Viết biểu thức điều kiện một dòng (ternary)
- Tránh lỗi logic phổ biến với điều kiện

## 📖 Kiến thức cần nắm

if/elif/else, comparison operators, and/or/not, ternary, truthy/falsy

Chi tiết xem tại [`notes.md`](notes.md)

## ✍️ Bài tập

Mở thư mục `exercises/` và hoàn thành theo thứ tự:

1. **`ex01_if_else.py`** — Phân loại và xếp hạng
   - *Bản chất:* Python kiểm tra từ trên xuống dưới. Khi gặp điều kiện nào đúng (`True`) đầu tiên, nó thực hiện khối lệnh đó rồi thoát ra ngay, không kiểm tra các phần `elif` hay `else` còn lại.
2. **`ex02_logical.py`** — Toán tử logic kết hợp
   - *Bản chất:* Gom nhiều điều kiện vào một dòng. `and` yêu cầu tất cả phải đúng, `or` chỉ cần một cái đúng. Giúp code gọn gàng hơn thay vì phải viết nhiều câu lệnh `if` rời rạc.
3. **`ex03_nested.py`** — Điều kiện lồng nhau
   - *Bản chất:* Luồng kiểm tra theo tầng (Cha - Con). Python chỉ kiểm tra điều kiện bên trong nếu điều kiện bao quanh nó đã thỏa mãn. Rất hữu ích cho các quy trình cần lọc nhiều bước như rút tiền ATM.

> 💡 Mỗi file có TODO comment hướng dẫn chi tiết. Hãy thử trước khi xem solutions!

## 🚀 Mini-Project: Máy tính điểm GPA 📊

Nhập điểm các môn → tính GPA → xếp loại học lực → hiển thị kết quả

Xem chi tiết tại [`mini-project/README.md`](mini-project/README.md)

## 📚 Đọc thêm

| Nguồn | Chương | Link |
|:------|:-------|:-----|
| Think Python | Chapter 4: Conditionals and Recursion | [Đọc](https://allendowney.github.io/ThinkPython/chap04.html) |

## ✅ Checklist cuối tuần

- [ ] Đọc notes.md
- [ ] Hoàn thành `ex01_if_else.py`
- [ ] Hoàn thành `ex02_logical.py`
- [ ] Hoàn thành `ex03_nested.py`
- [ ] Hoàn thành Mini-Project
- [ ] Commit code lên GitHub
- [ ] Đánh dấu trong PROGRESS.md
