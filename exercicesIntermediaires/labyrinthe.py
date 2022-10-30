# Labyrinthe (Maze)
#   Tableaux à 2 dimensions
#   Récursivité
#   Recherche de chemin
#
# 0 : mur
# 1 : chemin
# -1 : déjà parcouru
# 8 : entrée
# 9 : sortie
# pas de déplacement en diagonales

# x = 0  1  2  3  4  5      y
m = [[8, 1, 1, 1, 1, 0],  # 0
     [1, 0, 1, 0, 1, 0],  # 1
     [1, 0, 1, 1, 1, 1],  # 2 
     [1, 0, 0, 0, 1, 0],  # 3 
     [1, 1, 1, 0, 1, 0],  # 4      
     [0, 1, 0, 0, 1, 9]]  # 5


def cherche_chemin(m, x, y):


     print("Exploring at:", x, y)

     if m[y][x] == 9:
          print("la sortie de ce putain de labyrinthe est : ", x, y)
          for l in m:
               d = ""
               for e in l:
                    if e == -1:
                         d += str(e) + " "
                    else:
                         d += " " + str(e) + " "
               print(d)
               
          exit(0)
     

     m[y][x] = -1

     # exploration vers la gauche
     if x > 0:
          if m[y][x-1] >= 1:
               cherche_chemin(m, x-1, y)
     
     # exploration vers la droite
     if x < len(m)-1:
          if m[y][x+1] >= 1:
               cherche_chemin(m, x+1, y)

     # exploration vers le haut
     if y > 0:
          if m[y-1][x] >= 1:
               cherche_chemin(m, x, y-1)
     
     # exploration vers le bas
     if y < len(m)-1:
          if m[y+1][x] >= 1:
               cherche_chemin(m, x, y+1)


cherche_chemin(m, 0, 0)
          






