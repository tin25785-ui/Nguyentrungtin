"""
Bài tập 03: In hoa văn bằng vòng lặp lồng 🎨
===============================================
Mục tiêu: Thành thạo nested loops
"""

# TODO 1: In tam giác vuông cao n dòng
# n = 5:
# *
# **
# ***
# ****
# *****
n = 5
for i in range(1, n + 1):
    print("*" * i)
print()

# TODO 2: In tam giác cân cao n dòng (căn giữa)
# n = 5:
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
print()

# TODO 3: In hình kim cương cao n dòng (n lẻ)
# n = 5:
#   *
#  ***
# *****
#  ***
#   *
for i in range(1, n // 2 + 2):
    print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))
for i in range(n // 2, 0, -1):
    print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))
print()

# TODO 4 (Thử thách): In bàn cờ n x n
# n = 4:
# ■ □ ■ □
# □ ■ □ ■
# ■ □ ■ □
# □ ■ □ ■
n_board = 4
for r in range(n_board):
    for c in range(n_board):
        if (r + c) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
