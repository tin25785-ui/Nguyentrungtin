"""Lời giải Bài tập 01: Cơ bản về List (Thêm, Sửa, Xóa)"""

# TODO 1: Khởi tạo list trái cây
fruits = ["táo", "chuối", "cam"]
print(f"Danh sách ban đầu: {fruits}")

# TODO 2: Thêm "xoài" vào cuối danh sách và "nho" vào vị trí đầu tiên
fruits.append("xoài")
fruits.insert(0, "nho")
print(f"Sau khi thêm: {fruits}")

# TODO 3: Thay đổi phần tử "chuối" thành "dâu tây"
if "chuối" in fruits:
    index_chuoi = fruits.index("chuối")
    fruits[index_chuoi] = "dâu tây"
print(f"Sau khi sửa: {fruits}")

# TODO 4: Xóa phần tử cuối cùng bằng pop() và xóa "cam" bằng remove()
item_cuoi = fruits.pop()
fruits.remove("cam")
print(f"Đã xóa '{item_cuoi}' và 'cam'. Danh sách còn lại: {fruits}")