"""
TỔNG HỢP KIẾN THỨC TUẦN 08: DICTIONARY & SET 📖
=============================================
Mục tiêu: Nắm vững cấu trúc dữ liệu Map (Dict) và Set trong Python.
So sánh với C++ để hiểu sâu hơn về bản chất.
"""

# ==========================================
# 1. DICTIONARY (Dữ liệu theo cặp Key-Value)
# ==========================================
# C++: Tương đương std::unordered_map (Hash Table) hoặc std::map (Tree).
# Python: 'dict' là Hash Table, cực nhanh để tra cứu.

print("--- 1. Dictionary Cơ bản ---")
hoc_sinh = {
    "ten": "An",
    "tuoi": 20,
    "diem": 8.5
}

# dict.get(key, default) - AN TOÀN HƠN dict[key]
# C++: map[key] sẽ tự tạo phần tử mới nếu key không tồn tại.
#      map.at(key) sẽ văng ngoại lệ (error).
# Python: .get() trả về None (hoặc default) nếu không thấy key, giúp app không bị crash.
print(f"Tên: {hoc_sinh.get('ten')}")
print(f"Địa chỉ: {hoc_sinh.get('dia_chi', 'Chưa cập nhật')}") 


# ==========================================
# 2. DUYỆT DICT (Keys, Values, Items)
# ==========================================
print("\n--- 2. Duyệt Dictionary ---")
kho = {"tao": 10, "cam": 5, "xoai": 8}

# Duyệt cả key và value (Pythonic nhất)
# C++: for (const auto& [key, value] : my_map) (C++17 Structured Bindings)
for item, sl in kho.items():
    print(f"- {item}: {sl} quả")


# ==========================================
# 3. DICT COMPREHENSION
# ==========================================
# C++: Không có cú pháp tương đương, phải dùng vòng lặp for truyền thống.
print("\n--- 3. Dict Comprehension ---")
gia_goc = {"p1": 100, "p2": 200, "p3": 300}
gia_giam = {k: v * 0.9 for k, v in gia_goc.items() if v > 150}
print(f"Sản phẩm giảm giá (>150): {gia_giam}")


# ==========================================
# 4. DICT LỒNG NHAU (Nested Dict)
# ==========================================
print("\n--- 4. Dữ liệu phức tạp ---")
lop_hoc = {
    "lop_A": {"sl": 30, "gv": "Thầy Bình"},
    "lop_B": {"sl": 25, "gv": "Cô Lan"}
}
print(f"GV lớp A: {lop_hoc['lop_A']['gv']}")


# ==========================================
# 5. SET (Tập hợp không trùng lặp)
# ==========================================
# C++: Tương đương std::unordered_set.
# Đặc điểm: Tự động loại bỏ phần tử trùng, không có thứ tự.

print("\n--- 5. Set & Phép toán tập hợp ---")
anh = {"An", "Bình", "Chi"}
phap = {"Chi", "Dũng", "An"}

# Phép giao (&): Những người học cả 2 thứ tiếng
# C++: Phải dùng std::set_intersection (rất dài dòng)
print(f"Học cả Anh & Pháp: {anh & phap}")

# Phép hợp (|): Tất cả sinh viên duy nhất
print(f"Tất cả sinh viên: {anh | phap}")

# Phép hiệu (-): Học Anh nhưng không học Pháp
print(f"Chỉ học Anh: {anh - phap}")


# ==========================================
# 💡 GHI CHÚ SO SÁNH VỚI C++ (CHO LẬP TRÌNH VIÊN)
# ==========================================
"""
1. Kiểu dữ liệu (Typing):
   - C++: std::unordered_map<string, int> -> Key/Value phải cố định kiểu.
   - Python: dict có thể chứa 'ten': "An" (string) và 'tuoi': 20 (int) trong cùng một rổ.

2. Quản lý bộ nhớ:
   - Python quản lý tự động (Garbage Collection).
   - Trong C++, nếu lưu con trỏ trong map, bạn phải tự quản lý việc giải phóng vùng nhớ.

3. Tốc độ:
   - C++ nhanh hơn về mặt thực thi thuần túy.
   - Python nhanh hơn về mặt "thời gian viết code" (Developer productivity) nhờ các phép 
     toán tập hợp (| & -) và comprehension.

4. Truy cập Key không tồn tại:
   - C++: map[non_existent_key] sẽ CHÈN một giá trị mặc định vào map.
   - Python: dict[non_existent_key] sẽ báo lỗi KeyError. Do đó .get() là "vũ khí" cực mạnh.

5. Tính Duy nhất của Key (Set/Dict):
   - Cả hai đều dùng Hash Table để đảm bảo tính duy nhất. 
   - Key trong Python phải là 'Hashable' (không thay đổi được như string, int, tuple). 
     Bạn không thể dùng List làm Key cho Dict trong Python (C++ cũng tương tự với unordered_map).
"""

if __name__ == "__main__":
    print("\n--- Hoàn thành tổng hợp Tuần 08 ---")