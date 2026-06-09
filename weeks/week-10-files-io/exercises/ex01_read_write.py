"""
Bài tập 01: Đọc và ghi file text 📄
======================================
Mục tiêu: Dùng open(), read, write với context manager
"""

# TODO 1: Ghi danh sách 5 câu nói yêu thích vào file "quotes.txt"
# Dùng with open("quotes.txt", "w") as f:
quotes = [
    "Học, học nữa, học mãi.",
    "Không có gì quý hơn độc lập tự do.",
    "Có công mài sắt có ngày nên kim.",
    "Một cây làm chẳng nên non.",
    "Lá lành đùm lá rách."
]
with open("quotes.txt", "w", encoding="utf-8") as f:
    for quote in quotes:
        f.write(quote + "\n")
print("--- Đã tạo file quotes.txt ---")

# TODO 2: Đọc file "quotes.txt" và in ra từng dòng có số thứ tự
# Dùng enumerate()
print("\n--- Nội dung file quotes.txt ---")
with open("quotes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")

# TODO 3: Thêm (append) 2 câu nói mới vào cuối file "quotes.txt"
# Dùng mode "a"
new_quotes = [
    "Uống nước nhớ nguồn.",
    "Ăn quả nhớ kẻ trồng cây."
]
with open("quotes.txt", "a", encoding="utf-8") as f:
    for quote in new_quotes:
        f.write(quote + "\n")
print("\n--- Đã thêm 2 câu nói mới ---")

# TODO 4: Đọc file, đếm số dòng, số từ, số ký tự
# In thống kê
with open("quotes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    # splitlines() trả về list các dòng, không bao gồm ký tự \n
    lines = content.splitlines()
    num_lines = len(lines)
    # split() mặc định tách theo khoảng trắng (space, tab, newline)
    num_words = len(content.split())
    num_chars = len(content)

print("\n📊 THỐNG KÊ FILE:")
print(f"- Số dòng:   {num_lines}")
print(f"- Số từ:     {num_words}")
print(f"- Số ký tự:  {num_chars}")

# TODO 5 (Thử thách): Copy nội dung file, chuyển thành UPPER CASE
# Đọc "quotes.txt" → ghi vào "quotes_upper.txt" (chữ in hoa)
with open("quotes.txt", "r", encoding="utf-8") as f_in:
    content = f_in.read()

with open("quotes_upper.txt", "w", encoding="utf-8") as f_out:
    f_out.write(content.upper())
print("\n--- Đã tạo file quotes_upper.txt thành công ---")
