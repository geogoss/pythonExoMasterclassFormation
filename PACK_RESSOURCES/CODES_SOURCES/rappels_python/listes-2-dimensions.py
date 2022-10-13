# NOTION : Les listes à 2 dimensions
#  x  0  1  2  /   y
t = [[1, 2, 3],  # 0
     [4, 5, 6],  # 1
     [7, 8, 9]]  # 2

# print(t[2][0])   # t[y][x]
for l in t:
    ligne = ""
    for e in l:
        ligne += str(e) + " "
    print(ligne)
