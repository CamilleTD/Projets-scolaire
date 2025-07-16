from math import sqrt
from os import system, remove
from random import choice
from time import sleep

BLOCS_COMMUN = [
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
    [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0]]
]

BLOC_CERCLE = [[[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
               [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]],
               [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
               [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],
               [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]]]

BLOC_LOSANGE = [[[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]],
                [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]],
                [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]]


BLOC_TRIANGLE = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]],
                 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0]]]


BLOC_VIDE = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

CERCLE = 3
LOSANGE = 4
TRIANGLE = 5




bloc_list = []
losange_list = []
cercle_list = []
triangle_list = []
board = []

#-----------------------------------------------------------------------------------------------------------------------

def check_input(text, maxi):
    """
    Fonction permettant de vérifier si les valeurs saisies par l'utilisateur sont correctes
    :param text: valeur(s) saisie(s) par l'utilisateur
    :param maxi: intervalle de valeurs autorisées
    :return: /
    """
    while 1:
        try:
            input_val = input(text)
            if 0 < int(input_val) <= maxi:
                return input_val
            else:
                print("Veuillez vérifier la valeur entrée\n")
        except ValueError:
            print(f"Veuillez entrer DES CHIFFRES entre 1 et {maxi}\n")

#-----------------------------------------------------------------------------------------------------------------------

def rules():
    """
    Fonction permettant d'afficher les règles du jeu à la demande de l'utilisateur avec une ligne de code dans le 'main'
    :return: rules
    """
    print("----------------------------------------------------------------\n"
          "|                        Regles du jeu :                       |\n"
          "|  Tetris est un jeu qui met le joueur au defi de realiser des |\n"
          "|       lignes completes en deplacant des pieces de formes     |\n"
          "|    differentes, les tetrominos, qui defilent depuis le haut  |\n"
          "| jusqu'au bas de l'ecran. Les lignes completees disparaissent |\n"
          "|  tout en rapportant des points et le joueur peut de nouveau  |\n"
          "|                  remplir les cases liberees.                 |\n"
          "|    Attention ! Une fois le plateau est rempli en hauteur,    |\n"
          "| tu as perdu. A chaque etape, tu disposeras de suggestions de |\n"
          "|     plusieurs blocs que tu pourras placer selon ton choix.   |\n"
          "|                       BONNE CHANCE !!                        |\n"
          "---------------------------------------------------------------\n")

#-----------------------------------------------------------------------------------------------------------------------


def number(valeur_test, val_retourner):
    """
    Fonction permettant de vérifier si la valeur entrée est un chiffre
    :param valeur_test: test
    :param val_retourner: valeur retournée
    :return:
    """
    if valeur_test.isnumeric():
        return int(valeur_test)
    else:
        return val_retourner
#-----------------------------------------------------------------------------------------------------------------------

def load_files(files_name):
    """
    Fonction permettant de sauvergarder et chercher un fichier
    :param files_name: nom des fichiers
    :return: Booléen
    """
    try:
        with open(files_name, "r") as r:
            r.read()
        return True
    except:
        return False
#-----------------------------------------------------------------------------------------------------------------------


def read_grid(path):
    """
    Fonction permettant de lire un fichier et d'y retourner le contenu du fichier lu dans une liste 2D
    :param path: fichier
    :return: grid qui retourne le contenu du fichier
    """
    with open(path, "r") as f:
        inside = f.readlines()
        grid = []
        for i in range(len(inside)):
            line_ = []
            for j in range(len(inside[i])):
                if inside[i][j] != " " and inside[i][j] != "\n":
                    line_.append(int(inside[i][j]))
            grid.append(line_)
        return grid
#-----------------------------------------------------------------------------------------------------------------------




def save_grid(path, grid):
    """
    Fonction permettant de sauvegarderla grille grid dans un fichier path
    :param path: fichier couvrant la grille
    :param grid: grille
    :return: /
    """
    with open(path,"w") as f:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                f.write(str(grid[i][j]))
                if j == len(grid[i]) - 1:
                    f.write("\n")
                else:
                    f.write(" ")

#-----------------------------------------------------------------------------------------------------------------------


def select_blocs(forms):
    """
    Fonction permettant de renvoyer les blocs en fonction du choix de l'utilisateur
    :param forms: la forme des blocs
    :return: 11, 12 en fonction du plateau
    """
    if forms == CERCLE:
        return 11
    elif forms == LOSANGE:
        return 12
    else:
        return 11

#-----------------------------------------------------------------------------------------------------------------------

def grid_begin(forms, size):
    """
    Fonction permettant d'initialiser la grille.
    :param forms:forme du plateau
    :param size:taille du plateau
    :return: grille
    """
    grid = []
    if forms == CERCLE:
        for i in range(size):
            line = []
            for j in range(size):
                p = ""
                if round(sqrt(pow(abs((size - 1) / 2 - j), 2) + pow(abs((size - 1) / 2 - i), 2)), 2) > round((size - 1) / 2, 2):
                    p = 0
                else:
                    p = 1
                line.append(p)
            grid.append(line)
    if forms == LOSANGE:
        add = [(size // 2)]
        delete = [(size // 2)]
        for i in range(size):
            line = []
            for j in range(size):
                p = ''
                if j in add or j in delete:
                    p = 1
                else:
                    p = 0
                line.append(p)
            if i < size // 2:
                add.append(add[-1] + 1)
                delete.append(delete[-1] - 1)
            elif len(add) != 0:
                del add[-1]
                del delete[-1]
            grid.append(line)
    if forms == TRIANGLE:
        delete = [(size // 2)]
        add = [(size // 2)]
        for i in range((size // 2) + 1):
            line = []
            for j in range(size):
                p = ''
                if j in add or j in delete:
                    p = 1
                else:
                    p = 0
                line.append(p)
            add.append(add[-1] + 1)
            delete.append(delete[-1] - 1)
            grid.append(line)
    return grid

#-----------------------------------------------------------------------------------------------------------------------

def init_board(grid):
    """
    Fonction d'initialisation du plateau de jeu à partir de la grille
    :param grid: grille
    :return: plateau
    """
    line = []
    h = len(grid)
    l = len(grid[0])
    d = max(int((20 - (h + 3)) / 2), 0)
    for i in range(max(h, 17) +7):
        line = []
        for j in range(l + 34):
            line.append(" ")
        board.append(line)
    board[0][0] = "┌"
    for i in range(l + 5):
        board[0][i + 1] = "─"
    board[0][l + 6] = "┐"
    for i in range(max(h, 17) +5):
        board[i + 1][0] = "│"
        board[i + 1][l + 6] = "│"
    board[max(h, 17) + 6][0] = "└"
    for i in range(l + 5):
        board[max(h, 17) + 6][i + 1] = "─"
    board[max(h, 17) + 6][l + 6] = "┘"
    d = max(int((20 - (h + 3)) / 2), 0)
    for i in range(l):
        board[d + 2][i + 4] = chr(ord("a") + i)
    board[d + 3][3] = "┌"
    for i in range(l):
        board[d + 3][i + 4] = "─"
    board[d + 3][l + 4] = "┐"
    for i in range(h):
        board[d + i + 4][2] = chr(ord("A") + i)
        board[d + i + 4][3] = "│"
        board[d + i + 4][l + 4] = "│"
    board[d + h + 4][3] = "└"
    for i in range(l):
        board[d + h + 4][i + 4] = "└"
    board[d + h + 4][l + 4] = "┘"
    i = 0
    for c in "┌───────────────────┐":
        board[0][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│                   │":
        board[1][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│           ESSAIS  │":
        board[2][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│  SCORE:  RESTANTS:│":
        board[3][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│ ┌─────┐    ┌─┐    │":
        board[4][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│ │     │    │ │    │":
        board[5][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│ └─────┘    └─┘    │":
        board[6][l + 11 + i] = c
        i += 1
    i = 0
    for c in "│                   │":
        board[7][l + 11 + i] = c
        i += 1
    i = 0
    for c in "└───────────────────┘":
        board[8][l + 11 + i] = c
        i += 1
    i = 0
    for c in "┌───────────────────────┐":
        board[10][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ ┌─────┐┌─────┐┌─────┐ │":
        board[11][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ │     ││     ││     │ │":
        board[12][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ │     ││     ││     │ │":
        board[13][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ │     ││     ││     │ │":
        board[14][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ │     ││     ││     │ │":
        board[15][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ │     ││     ││     │ │":
        board[16][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│ └─────┘└─────┘└─────┘ │":
        board[17][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│   -1-    -2-    -3-   │":
        board[18][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│───────────────────────│":
        board[19][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│                       │":
        board[20][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│                       │":
        board[21][l + 9 + i] = c
        i += 1
    i = 0
    for c in "│                       │":
        board[22][l + 9 + i] = c
        i += 1
    i = 0
    for c in "└───────────────────────┘":
        board[23][l + 9 + i] = c
        i += 1
    return board

#-----------------------------------------------------------------------------------------------------------------------

def print_bloc(form):
    """
    Fonction affichant tous les blocs correspondant à la forme
    :param form:forme des blocs en fonction de la forme du plateau
    :return: /
    """
    if form == CERCLE:
        f = cercle_list
    elif form == LOSANGE:
        f = losange_list
    elif form == TRIANGLE:
        f = triangle_list
    for k in range(len(bloc_list[f[0]])):
        for i in range(len(f)):
            for j in range(len(bloc_list[f[i]][k])):
                if bloc_list[f[i]][k][j] == 0:
                    print(" ", end=" ")
                elif bloc_list[f[i]][k][j] == 1:
                    print("■", end=" ")
            print("  ", end=" ")
        print()

#-----------------------------------------------------------------------------------------------------------------------

def select_bloc(form):
    """
    Fonction pour séléctionner 3 blocs selon la forme  choisie et renvoie une liste contenant des indices pris aléatoirement dans les listes
    :param form: forme des blocs pour jouer
    :return: fichier des formes
    """
    f = []
    if form == CERCLE:
        for i in range(3):
            f.append(choice(cercle_list))
    elif form == LOSANGE:
        for i in range(3):
            f.append(choice(losange_list))
    elif form == TRIANGLE:
        for i in range(3):
            f.append(choice(triangle_list))
    return f

#-----------------------------------------------------------------------------------------------------------------------

def verif_valid(grid, bloc, i, j):
    """
    Fonction vérifiant que la case sur le plateau est vide
    :param grid: grille
    :param bloc: bloc
    :param i: indice pour parcourir les listes 2D
    :param j: indice pour parcourir les listes 2D
    :return: booléen, True si la case est vide sinon False
    """
    for k in range(len(bloc)):
        for l in range(len(bloc[k])):
            if bloc[k][l] == 1:
                if (i - len(bloc) + 1 + k) < 0 or (j + l) > len(grid[0]):
                    return False
                elif grid[i - len(bloc) + 1 + k][j + l] != 1:
                    return False
    return True

#-----------------------------------------------------------------------------------------------------------------------

def place_bloc(grid, bloc, i, j):
    """
    Fonction permettant de placer le bloc àl'endroit choisi par l'utilisateur
    :param grid: grille
    :param bloc: bloc
    :param i: indice pour parcourir les listes 2D
    :param j: indice pour parcourir les listes 2D
    :return:
    """
    for k in range(len(bloc)):
        for l in range(len(bloc[k])):
            if bloc[k][l] == 1:
                grid[i - len(bloc) + 1 + k][j + l] = 2
    return grid


#-----------------------------------------------------------------------------------------------------------------------

def row_state(grid, i):
    """
    Fonction vérifiant si une ligne est pleine ou non
    :param grid: grille
    :param i: indice permettant de parcourir la ligne
    :return: True si elle est pleine, sinon False
    """
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            return False
    return True



#-----------------------------------------------------------------------------------------------------------------------

def col_state(grid, j):
    """
    Fonction vérifiant si une colonne est pleine ou non
    :param grid: grille
    :param j: idnice parcourant la colonne
    :return: True si elle est pleine, sinon False
    """
    for i in range(len(grid)):
        if grid[i][j] == 1:
            return False
    return True

#-----------------------------------------------------------------------------------------------------------------------

def row_clear(grid, i):
    """
    Fonction permettant de supprimer la ligne si elle est pleine et comptabiliser le score en fonction de celle-ci
    :param grid: grille
    :param i: indice parcourant la ligne
    :return: score de l'utilisateur en fonction du nombre de cases supprimées
    """
    score = 0
    for j in range(len(grid[i])):
        if grid[i][j] == 2:
            score += 1
            for k in range(i, len(grid)):
                if grid[k][j] != 0:
                    if k + 1 == len(grid):
                        grid[k][j] = 1
                    else:
                        if grid[k + 1][j] == 0:
                            grid[k][j] = 1
                        else:
                            grid[k][j] = grid[k + 1][j]
    return score


#-----------------------------------------------------------------------------------------------------------------------



def col_clear(grid, j):
    """
    Fonction permettant de supprimer la colonne si elle est pleine et comptabiliser le score en fonction de celle-ci
    :param grid: grille
    :param j: indice parcoutant la colonne
    :return: score de l'utilisateur en fonction du nombre de cases supprimées
    """
    S = 0
    for i in range(len(grid)):
        if grid[i][j] == 2:
            grid[i][j] = 1
            S += 1
    return S
#-----------------------------------------------------------------------------------------------------------------------

def delete_consol():
    system("cls")

#-----------------------------------------------------------------------------------------------------------------------

def print_blocs(bloc, board, quirky, grid):
    """
    Fonction affichant les blocs à l'utilisateur
    :param bloc: bloc
    :param board: plateau
    :param quirky: décalage des blocs
    :param grid: grille
    :return: /
    """
    l = len(grid[0])
    for i in range(len(bloc)):
        for j in range(len(bloc[i])):
            if bloc[i][j] == 1:
                board[i + 12][j + l + quirky] = "◼"
            elif bloc[i][j] == 0:
                board[i + 12][j + l + quirky] = " "

#-----------------------------------------------------------------------------------------------------------------------

def print_score(board, score, grid, line, quirky):
    """
    Fonction affichant le score de l'utilisateur
    :param board: plateau
    :param score: score
    :param grid: grille
    :param line: ligne
    :param quirky: décalage de blocs
    :return: /
    """
    l = len(grid[0])
    for i in range(len(str(score))):
        board[line][quirky + l + i + line - len(str(score))] = str(score)[i]

#-----------------------------------------------------------------------------------------------------------------------

def print_param(board, params, grid, line, quirky):
    """
    Fonction permettant d'afficher l'interface intégrale du jeu à l'utilisateur
    :param board: plateau
    :param info: interface
    :param grid: grille
    :param line: ligne
    :param quirky: décalage de blocs
    :return:/
    """
    l = len(grid[0])
    for i in range(len(str(params))):
        board[line][quirky + l + i] = str(params)[i]

#-----------------------------------------------------------------------------------------------------------------------

def grid_(board, grid, d):
    """
    Fonction permettant d'afficher la grille
    :param board: plateau
    :param grid: grille
    :param d: décalage de blocs
    :return: /
    """
    quirky = max(int((20 - (len(grid) + 3)) / 2), 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                board[quirky + i + quirky][j + quirky] = "."
            elif grid[i][j] == 2:
                board[quirky + i + quirky][j + quirky] = "◼"
            else:
                board[quirky + i + quirky][j + quirky] = " "

#-----------------------------------------------------------------------------------------------------------------------

def relate_param(board, grid, line):
    """
    Fonction réinistialisant les paramètres de l'utilisateur
    :param board: plateau
    :param grid: grille
    :param line: ligne
    :return: /
    """
    l = len(grid[0])
    i = l + 10
    for j in board[line][l + 10:-1]:
        board[line][i] = " "
        i += 1

#-----------------------------------------------------------------------------------------------------------------------

def print_grid(grid):
    """
    Affichage de la grille
    :param grid: grille
    :return:
    """
    delete_consol()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()

#-----------------------------------------------------------------------------------------------------------------------

def fill_board(grid, score, try_, q, params, bloca, blocb, blocc):
    """
    Fonction permettant de remplir le tableau
    :param grid: grille
    :param score: score
    :param try_: essai
    :param q:
    :param params: paramètre utilisateur
    :param bloca: bloc n°1
    :param blocb: bloc n°2
    :param blocc: bloc n°3
    :return: plateau
    """
    global board
    board = init_board(grid)
    grid_(board, grid, 4)
    print_param(board, try_, grid, 5, 25)
    print_param(board, params, grid, 22, 11)
    print_param(board, q, grid, 21, 11)
    print_score(board, score, grid, 5, 14)
    print_blocs(bloca, board, 12, grid)
    print_blocs(blocb, board, 19, grid)
    print_blocs(blocc, board, 26, grid)
    return board

#-----------------------------------------------------------------------------------------------------------------------

def save_score(form, score, try_, size, r):
    """
    Fonction permettant de comptabiliser et sauvegarder le score de l'utilisateur
    :param form: forme du plateau
    :param score: score
    :param try_: essai
    :param size: taille
    :param r:
    :return: /
    """
    if form == CERCLE:
        path = "cercle.score.txt"
    elif form == LOSANGE:
        path = "losange.score.txt"
    elif form == TRIANGLE:
        path = "triangle.score.txt"
    with open(path, "w") as f:
        f.write(str(score) + "\n")
        f.write(str(try_) + "\n")
        f.write(str(size) + "\n")
        f.write(str(r) + "\n")

#-----------------------------------------------------------------------------------------------------------------------

def save_bloc(form, bloca, blocb, blocc):
    """
    Fonction permettant d'enregistrer les blocs proposés et choisis par l'utilisateur
    :param form:
    :param bloca:
    :param blocb:
    :param blocc:
    :return:
    """
    if form == CERCLE:
        path = "cercle.bloc.txt"
    elif form == LOSANGE:
        path = "losange.bloc.txt"
    elif form == TRIANGLE:
        path = "triangle.bloc.txt"
    with open(path, "w") as f:
        f.write(bloca)
        f.write("\n")
        f.write(blocb)
        f.write("\n")
        f.write(blocc)
#-----------------------------------------------------------------------------------------------------------------------
