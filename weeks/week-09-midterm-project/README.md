# Dự án giữa kỳ: Hệ thống Quản lý Học sinh 🎓

Đây là dự án hoàn thành trong Tuần 09 của khóa học **Python Journey**. Dự án này tổng hợp các kiến thức từ Tuần 1 đến Tuần 8 để xây dựng một ứng dụng quản lý học sinh chạy trên terminal.

## 🚀 Tính năng

- **Quản lý danh sách**: Thêm, xem, tìm kiếm và xóa học sinh.
- **Tính toán & Xếp loại**: Tự động tính điểm trung bình và xếp loại học lực (Xuất sắc, Giỏi, Khá, Trung bình, Yếu).
- **Thống kê**: Xem tổng quan về lớp học (tổng số học sinh, điểm cao nhất/thấp nhất, phân bổ xếp loại).
- **Sắp xếp**: Sắp xếp danh sách theo tên hoặc theo điểm trung bình.
- **Xử lý lỗi**: Kiểm tra tính hợp lệ của dữ liệu đầu vào (điểm 0-10, tên không rỗng, v.v.).

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ**: Python 3.x
- **Kiến thức áp dụng**:
  - Biến và kiểu dữ liệu (Strings, Int, Float)
  - Cấu trúc dữ liệu (Lists, Dictionaries)
  - Vòng lặp (for, while)
  - Hàm (Functions) và Docstrings
  - Xử lý ngoại lệ cơ bản (try-except)

## 📖 Cách chạy chương trình

1. Đảm bảo bạn đã cài đặt Python trên máy tính.
2. Di chuyển vào thư mục dự án:
   ```bash
   cd weeks/week-09-midterm-project
   ```
3. Chạy chương trình:
   ```bash
   python student_manager.py
   ```

## 📝 Cấu trúc code

- `tinh_diem_tb()`: Tính trung bình cộng 3 môn Toán, Văn, Anh.
- `xep_loai()`: Phân loại học sinh dựa trên điểm trung bình.
- `them_hoc_sinh()`: Nhập thông tin và kiểm tra trùng lặp.
- `xem_danh_sach()`: Hiển thị bảng thông tin học sinh đẹp mắt.
- `thong_ke()`: Hiển thị biểu đồ cột đơn giản và các chỉ số thống kê.

## 👤 Tác giả

Dự án được thực hiện bởi **AI Assistant** trong lộ trình học Python Journey.
