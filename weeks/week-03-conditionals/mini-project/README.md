# Máy tính điểm GPA 📊

Nhập điểm các môn → tính GPA → xếp loại → hiển thị kết quả.

## Yêu cầu
1. Nhập số lượng môn học
2. Với mỗi môn: nhập tên môn, số tín chỉ, điểm (0-10)
3. Tính GPA theo công thức: Σ(điểm × tín chỉ) / Σ tín chỉ
4. Xếp loại: >= 3.6 Xuất sắc, >= 3.2 Giỏi, >= 2.5 Khá, >= 2.0 TB
5. In bảng kết quả đẹp

## ⚙️ Cách chương trình hoạt động (Bản chất logic)

1. **Khởi tạo**: Chương trình tạo hai biến "tích lũy" là `tong_diem_he_4` và `tong_tin_chi` để cộng dồn dữ liệu trong quá trình nhập.
2. **Vòng lặp (Loop)**: Dựa trên số môn bạn nhập, chương trình chạy một vòng lặp để thu thập tên môn, số tín chỉ và điểm số.
3. **Quy đổi & Trọng số**: 
   - Điểm hệ 10 được quy đổi sang hệ 4 bằng công thức: `diem_10 * 4 / 10`.
   - Điểm này sau đó được nhân với số tín chỉ của môn đó (trọng số) trước khi cộng vào tổng.
4. **Tính GPA**: Sau khi nhập xong, chương trình lấy `tổng (điểm hệ 4 × tín chỉ)` chia cho `tổng số tín chỉ`.
5. **Rẽ nhánh (Conditionals)**: Kết quả GPA cuối cùng được đưa qua bộ lọc `if/elif/else` để xác định danh hiệu tương ứng (Xuất sắc, Giỏi, Khá...).
6. **Định dạng (Formatting)**: Sử dụng kỹ thuật f-string để in bảng kết quả thẳng hàng và làm tròn số thập phân.

## Nộp bài
Hoàn thành code và commit lên GitHub với message: `"Complete mini-project week 03"`
