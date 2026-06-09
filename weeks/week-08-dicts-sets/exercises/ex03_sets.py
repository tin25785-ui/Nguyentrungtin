"""
Bài tập 03: Set & Phép toán tập hợp 🔢
=========================================
Mục tiêu: Dùng set cho bài toán tập hợp
"""

# TODO 1: Tạo 2 set: môn học kỳ 1 và kỳ 2
# hk1 = {"Toán", "Văn", "Anh", "Lý", "Hóa"}
# hk2 = {"Toán", "Văn", "Anh", "Sinh", "Sử"}
# Tìm: môn cả 2 kỳ, chỉ kỳ 1, chỉ kỳ 2, tất cả các môn
hk1 = {"Toán", "Văn", "Anh", "Lý", "Hóa"}
hk2 = {"Toán", "Văn", "Anh", "Sinh", "Sử"}

print("--- TODO 1: Phép toán tập hợp môn học ---")
print(f"Môn học cả 2 kỳ: {hk1 & hk2}")
print(f"Chỉ có ở kỳ 1:   {hk1 - hk2}")
print(f"Chỉ có ở kỳ 2:   {hk2 - hk1}")
print(f"Tất cả các môn:  {hk1 | hk2}")


# TODO 2: Loại bỏ trùng lặp từ list bằng set
# words = ["apple", "banana", "apple", "cherry", "banana", "date"]
# In ra các từ duy nhất (giữ thứ tự)
words = ["apple", "banana", "apple", "cherry", "banana", "date"]

print("\n--- TODO 2: Loại bỏ trùng lặp (giữ thứ tự) ---")
seen = set()
unique_words = []
for w in words:
    if w not in seen:
        unique_words.append(w)
        seen.add(w)
print(f"Danh sách duy nhất: {unique_words}")


# TODO 3: Nhập 2 câu từ người dùng
# Tìm: từ chung, từ chỉ có ở câu 1, từ chỉ có ở câu 2
print("\n--- TODO 3: So sánh từ vựng giữa 2 câu ---")
cau1 = input("Nhập câu thứ nhất: ").lower().split()
cau2 = input("Nhập câu thứ hai: ").lower().split()

set1 = set(cau1)
set2 = set(cau2)

print(f"Các từ chung:        {set1 & set2}")
print(f"Từ chỉ có ở câu 1:   {set1 - set2}")
print(f"Từ chỉ có ở câu 2:   {set2 - set1}")


# TODO 4 (Thử thách): Kiểm tra 2 chuỗi có phải anagram không
# Anagram: cùng bộ ký tự, khác thứ tự
# "listen" & "silent" → True
# "hello" & "world" → False
print("\n--- TODO 4: Kiểm tra Anagram ---")
def check_anagram(s1, s2):
    # Loại bỏ khoảng trắng và chuyển về chữ thường để so sánh chính xác
    str1 = s1.replace(" ", "").lower()
    str2 = s2.replace(" ", "").lower()
    
    # Cách nhanh nhất là sắp xếp các ký tự và so sánh
    return sorted(str1) == sorted(str2)

test_cases = [
    ("listen", "silent"),
    ("hello", "world"),
    ("rail safety", "fairy tales")
]

for a, b in test_cases:
    print(f"'{a}' & '{b}' là anagram? {check_anagram(a, b)}")
