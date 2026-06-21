# Text Analyzer 📝

Phân tích văn bản chi tiết.

## Yêu cầu
1. Nhập đoạn văn bản (hoặc đọc từ file)
2. Đếm: số ký tự, số từ, số câu
3. Tìm từ dài nhất, từ ngắn nhất
4. Đếm tần suất mỗi từ → in top 5 từ xuất hiện nhiều nhất
5. In thống kê tổng hợp

## Gợi ý
- Dùng `split()` để tách từ
- Dùng `lower()` trước khi đếm
- Dùng dict để đếm tần suất

## Nộp bài
Hoàn thành code và commit lên GitHub với message: `"Complete mini-project week 04"`

Phương thức	Ý nghĩa	Ví dụ
strip()	Loại bỏ khoảng trắng (hoặc ký tự chỉ định) ở 2 đầu chuỗi.	" hi ".strip() -> "hi"
lower()	Chuyển toàn bộ chuỗi thành chữ thường.	"Hi".lower() -> "hi"
upper()	Chuyển toàn bộ chuỗi thành chữ HOA.	"hi".upper() -> "HI"
title()	Viết hoa chữ cái đầu tiên của mỗi từ.	"học python".title() -> "Học Python"
replace(a, b)	Thay thế chuỗi a bằng chuỗi b.	"mèo".replace("m", "mèo ")
count(sub)	Đếm số lần chuỗi con sub xuất hiện.	"banana".count("a") -> 3
find(sub)	Tìm vị trí đầu tiên của sub (trả về -1 nếu không thấy).	"abc".find("b") -> 1
split()	Tách chuỗi thành một List các từ.	"a b".split() -> ["a", "b"]
startswith()	Kiểm tra chuỗi có bắt đầu bằng... hay không.	"Hello".startswith("He") -> True
endswith()	Kiểm tra chuỗi có kết thúc bằng... hay không.	"file.py".endswith(".py") -> True
isalpha()	Trả về True nếu chuỗi chỉ chứa chữ cái.	"Python".isalpha() -> True
isdigit()	Trả về True nếu chuỗi chỉ chứa chữ số.	"123".isdigit() -> True
isalnum()	Trả về True nếu là chữ cái hoặc chữ số.	"A1".isalnum() -> True
islower()	Kiểm tra chuỗi có đang viết thường hết không.	"abc".islower() -> True
isupper()	Kiểm tra chuỗi có đang viết HOA hết không.	"ABC".isupper() -> True
isspace()	Kiểm tra chuỗi chỉ toàn khoảng trắng/tab/xuống dòng.	" "