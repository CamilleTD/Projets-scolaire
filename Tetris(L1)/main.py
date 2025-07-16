from functions import *
import time

class bcolors:
  OK = '\033[92m'  # GREEN
  WARNING = '\033[93m'  # YELLOW
  FAIL = '\033[91m'  # RED
  RESET = '\033[0m'  # RESET COLOR


if __name__ == "__main__":
  sortie = 0
  while sortie == 0:

    print("      /$$$$$$$$  /$$$$$$$$  /$$$$$$$$  /$$$$$$$   /$$$$$$   $$$$$$$$/    \n"
          "     |__  $$__/ | $$_____/ |__  $$__/ | $$__  $$ |_  $$_/  |$$|   \n"
          "        | $$    | $$          | $$    | $$  \ $$   | $$    |$$|         \n"
          "        | $$    | $$$$$       | $$    | $$$$$$$/   | $$    |$$$$$$$$\    \n"
          "        | $$    | $$__/       | $$    | $$__  $$   | $$          |$$|          \n"
          "        | $$    | $$          | $$    | $$  \ $$   | $$          |$$|    \n"
          "        | $$    | $$$$$$$$    | $$    | $$  | $$  /$$$$$$| /$$$$$$$$$  \n"
          "        |__/    |________/    |__/    |__/  |__/ |______/ \_________/   \n")
    print(bcolors.FAIL + "                               BONJOUR ! \n"
                         "                   Bienvenue sur notre jeu TETRIS.\n"
                         "Il est important de vous preciser que vous taperez les chiffres correspondants\n"
                         "                  aux rubriques pour faire vos  choix !  🙂      \n" + bcolors.RESET)
    choice = int(check_input(bcolors.OK + "                 1- Commencer a jouer   \n"
                                          "                 2- Afficher les regles du jeu (20 secondes pour lire)\n"
                                          "                 3- Quitter le jeu 😦 \n"
                                          "                 Que voulez-vous faire (1, 2 ou 3) ? \n" + bcolors.RESET,
                             3))
    taille = 0
    forme = 0
    if choice == 2:
      choice_rules = 0
      while choice_rules == 0:
        rules()
        time.sleep(20)
        backm = int(check_input("Souhaitez-vous revenir au menu principal ou relire les règles :\n"
                                "1-Revenir au menu principal\n"
                                "2-Relire les règles\n", 2))
        if backm == 1:
          choice_rules = 5
        if backm == 2:
          backm = 0

    if choice == 3:
      print(bcolors.WARNING + "Au revoir et peut etre a bientot !" + bcolors.RESET)
      sortie = 2


  #commencons la création du jeu par la taille et la forme
    if choice == 1:
      delete_consol()
      print("   ┌─────────────┐\n" + "   │ MODE DE JEU │\n" +
            "   └─────────────┘\n")
      while (forme != CERCLE) and (forme != LOSANGE) and (forme != TRIANGLE):
        test = input("Quelle est la forme du plateau que vous souhaitez: \n" +
                     "Si vous souhaitez le cercle merci d'appuyer sur " +
                     str(CERCLE) + " \n" +
                     "Si vous souhaitez le losange merci d'appuyer sur " +
                     str(LOSANGE) + " \n" +
                     "Si vous souhaitez le triangle merci d'appuyer sur " +
                     str(TRIANGLE) + " \n")

        forme = number(test, 0)
      print()
      #######################Initialisation des différents fichiers selon la forme choisie###############

      #Avec chargement on cherche si une sauvegarde existe déjà

      #Le joueur choisit alors de soit charger la sauvegarde soit de créer une nouvelle partie

      if forme == CERCLE:
        path = "cercle.txt"
        nom_score = "cercle.score.txt"
        nom_bloc = "cercle.bloc.txt"
        chargement = load_files("cercle.txt")
        if chargement:
          print("Une sauvegarde a été trouvé voulez-vous la charger ?")
          print("Appuyez sur 1 pour oui \nAppuyez sur 2 pour non")
          choix = -1
          while choix != 1 and choix != 2:
            test = input("")
            choix = number(test, -1)
          print()
          if choix == 2:
            chargement = False
          else:
            grid = read_grid(path)

      if forme == LOSANGE:
        path = "losange.txt"
        nom_score = "losange.score.txt"
        nom_bloc = "losange.bloc.txt"
        chargement = load_files("losange.txt")
        if chargement:
          print("une sauvegarde a été trouvé voulez-vous la charger ?")
          print("1) Oui, 2) Non")
          choix = -1
          while choix != 1 and choix != 2:
            test = input("")
            choix = number(test, -1)
          if choix == 2:
            chargement = False
          else:
            grid = read_grid(path)

      if forme == TRIANGLE:
        path = "triangle.txt"
        nom_score = "triangle.score.txt"
        nom_bloc = "triangle.bloc.txt"
        chargement = load_files("triangle.txt")
        if chargement:
          print("une sauvegarde a été trouvé voulez-vous la charger ?")
          print("1) Oui, 2) Non")
          choix = -1
          while choix != 1 and choix != 2:
            test = input("")
            choix = number(test, -1)
          if choix == 2:
            chargement = False
          else:
            grid = read_grid(path)

  ##############################Création des différents plateaux de jeu##############################

  #Choix de la taille si le joueur décide de créer une nouvelle partie

      if not (chargement):
        while taille < 21 or taille > 26 or taille % 2 == 0:
          print(
            "Quelle dimmension souhaitez vous pour votre plateau, elle doit être supérieure ou égale à 21 et inférieure égale à 26 et doit être impaire: "
          )
          test = input("")
          taille = number(test, 0)

      ##clear_console()
      print()
      """Cas si le joueur choisi une grille en forme de cercle"""

      if (forme == CERCLE):
        if not (chargement):
          grid = grid_begin(forme, taille)
        """ Initialisation de la liste qui contient tous les blocs commun aux trois grilles
      Ainsi que les blocs propre à la grille cercle"""

        for i in range(len(BLOCS_COMMUN)):
          bloc_list.append(BLOCS_COMMUN[i])
          cercle_list.append(i)
        for i in range(len(BLOC_CERCLE)):
          bloc_list.append(BLOC_CERCLE[i])
          cercle_list.append(i + len(BLOCS_COMMUN))
          """ Fin de l'initialisation """
          """ Cas si le joueur choisi une grille en forme de losange"""

      elif (forme == LOSANGE):
        if not (chargement):
          grid = grid_begin(forme, taille)
        """ Initialisation de la liste qui contient tous les blocs commun aux trois grilles         
        Ainsi que les blocs propre à la grille losange"""

        for i in range(len(BLOCS_COMMUN)):
          bloc_list.append(BLOCS_COMMUN[i])
          losange_list.append(i)
        for i in range(len(BLOC_LOSANGE)):
          bloc_list.append(BLOC_LOSANGE[i])
          losange_list.append(i + len(BLOCS_COMMUN))
        """ Fin de l'initialisation"""
        """ Cas si le joueur choisi une grille en forme de triangle """

      elif (forme == TRIANGLE):
        if not (chargement):
          grid = grid_begin(forme, taille)
        for i in range(len(BLOCS_COMMUN)):
          bloc_list.append(BLOCS_COMMUN[i])
          triangle_list.append(i)
        for i in range(len(BLOC_TRIANGLE)):
          bloc_list.append(BLOC_TRIANGLE[i])
          triangle_list.append(i + len(BLOCS_COMMUN))

      print(
        "Les dimensions du plateau que vous avez choisi sont de " +
        str(len(grid[0])) + "x" + str(len(grid))
      )  #mettre après l'initialisation de la grille pour qu'elle s'adapte au plateau
  ####################################################################   Partie jeu  ###########################################################

  #Si le joueur choisit de charger une sauvegarde, on récupère alors toutes les données
    if chargement:
      with open(nom_score, "r") as r:
        Score = int(r.readline())
        essai_restant = int(r.readline())
        taille = int(r.readline())
        politique_choisie = int(r.readline())

    else:
      Score = 0
      essai_restant = 3
      politique_choisie = -1
      while politique_choisie != 1 and politique_choisie != 2:
        print(
          "Veuillez choisir votre mode de jeu :\nAppuyez sur 1 pour le mode aléatoire\nAppuyez sur 2 pour le mode libre"
        )
        test = input("")
        politique_choisie = number(test, -1)
    sortie = False  #variable permettant de terminer le programme si une condition de sortie est remplie

    ############################################################Partie affichage des blocs proposés###############################################
    fill_board(grid, Score, essai_restant, " ", " ", " ", " ",
                    " ")  #on remplit le plateau vierge
    while sortie == False:
      if politique_choisie == 1:  #Si le joueur choisit le mode aléatoire, soit on charge les anciens blocs si le jeu est chargé depuis une sauvegarde soit on en génère de nouveaux
        new_bloc = []
        if chargement:
          blocs_sauvegarde = []
          with open(nom_bloc, "r") as r:
            liste = r.readlines()
            for i in range(3):
              blocs_sauvegarde.append([])
              indice = -1
              for y in liste[i][1:]:
                if y == '[':
                  blocs_sauvegarde[i].append([])
                  indice += 1
                try:
                  blocs_sauvegarde[i][indice].append(int(y))
                except:
                  pass
          for i in range(3):  #On récupère les anciens blocs de la sauvegarde
            for j in range(len(bloc_list)):
              if blocs_sauvegarde[i][0] == bloc_list[j][0]:
                if blocs_sauvegarde[i][1] == bloc_list[j][1]:
                  if blocs_sauvegarde[i][2] == bloc_list[j][2]:
                    if blocs_sauvegarde[i][3] == bloc_list[j][3]:
                      if blocs_sauvegarde[i][4] == bloc_list[j][4]:
                        new_bloc.append(j)
          chargement = not (chargement)
        else:
          new_bloc = select_bloc(
            forme
          )  #créer une liste contenant 3 blocs aléatoires qui seront proposés au joueur
        bloc_1 = new_bloc[0]
        bloc_2 = new_bloc[1]
        bloc_3 = new_bloc[2]
        print_blocs(bloc_list[bloc_1], board, 12, grid)
        print_blocs(bloc_list[bloc_2], board, 19, grid)
        print_blocs(bloc_list[bloc_3], board, 26, grid)
      if politique_choisie == 2:  #Cas si le joueur choisit le mode libre
        new_bloc = []
        page_maxi = select_blocs(forme)
        page = 1
        for i in range(len(bloc_list)):
          new_bloc.append(i)
        bloc_1 = new_bloc[0 + (page - 1) * 3]
        bloc_2 = new_bloc[1 + (page - 1) * 3]
        bloc_3 = new_bloc[2 + (page - 1) * 3]
        print_blocs(bloc_list[bloc_1], board, 12, grid)
        print_blocs(bloc_list[bloc_2], board, 19, grid)
        print_blocs(bloc_list[bloc_3], board, 26, grid)
        print_param(board, "sélectionnez la page", grid, 20, 11)
        print_param(board, "en entrant un nombre", grid, 21, 11)
        print_param(board, "entre 1 et ", grid, 22, 11)
        print_param(board, page_maxi, grid, 22, 22)
        print_blocs(bloc_list[bloc_1], board, 12, grid)
        print_blocs(bloc_list[bloc_2], board, 19, grid)
        print_blocs(bloc_list[bloc_3], board, 26, grid)
        page = -1
        while page < 0 or page > page_maxi:
          print_grid(board)
          test = input("")
          page = number(test, -1)
        derniere_page_entre = 1
        while page != 0:  #Le joueur choisit la page de bloc qu'il veut consulter
          if page > 0 and page < page_maxi:
            derniere_page_entre = page
          if page > page_maxi or page < 0:
            page = 1
          relate_param(board, grid, 20)
          relate_param(board, grid, 21)
          relate_param(board, grid, 22)
          print_param(board, "Page", grid, 20, 11)
          print_param(board, page, grid, 20, 17)
          print_param(board, "sur", grid, 21, 11)
          print_param(board, page_maxi, grid, 21, 16)
          print_param(board, "(0 pour valider)", grid, 22, 11)
          if page == page_maxi:  #Si le joueur veut voir la page maximale
            bloc_1 = new_bloc[0 + (page_maxi - 1) * 3]
            print_blocs(bloc_list[bloc_1], board, 12, grid)
            if forme == CERCLE:  #Comme on affiche les blocs 3 par 3, afin d'éviter une erreur de débordement, on fait en sorte à ce que s'il n'existe plus de bloc, on affiche les premiers
              bloc_3 = new_bloc[0]
              bloc_2 = new_bloc[1 + (page_maxi - 1) * 3]
              print_blocs(bloc_list[bloc_2], board, 19, grid)
              print_blocs(bloc_list[bloc_3], board, 26, grid)
            else:
              bloc_2 = new_bloc[0]
              bloc_3 = new_bloc[1]
              print_blocs(bloc_list[bloc_2], board, 19, grid)
              print_blocs(bloc_list[bloc_3], board, 26, grid)
          else:
            bloc_1 = new_bloc[
              0 + (derniere_page_entre - 1) *
              3]  #Si le joueur choisit 0 alors la page devient 0, afin d'éviter les problèmes d'indices on créer une variable enregiistrant l'ancienne valeur fournie afin qu'elle puisse être utillisé à la place du 0.
            bloc_2 = new_bloc[1 + (derniere_page_entre - 1) * 3]
            bloc_3 = new_bloc[2 + (derniere_page_entre - 1) * 3]
            print_blocs(bloc_list[bloc_1], board, 12, grid)
            print_blocs(bloc_list[bloc_2], board, 19, grid)
            print_blocs(bloc_list[bloc_3], board, 26, grid)
          page = -1
          while page < 0 or page > page_maxi:
            print_grid(board)
            test = input("")
            page = number(test, -1)
      save_bloc(forme, str(bloc_list[bloc_1]), str(bloc_list[bloc_2]),
                str(bloc_list[bloc_3]))
      save_grid(path, grid)
      save_score(forme, Score, essai_restant, taille, politique_choisie)

      piece = -1
      relate_param(board, grid, 21)
      print_param(board, "Pièce à déplacer : ", grid, 21, 11)
      relate_param(board, grid, 22)
      print_param(board, "(0 pour quitter)", grid, 22, 11)
      relate_param(board, grid, 20)
      print(board)
      """ Choix de la pièce par le joueur """

      ############################################################Partie choix de la pièce##########################################################

      while piece < 0 or piece > 3:
        print_grid(board)
        test = input("")
        piece = number(test, -1)
        if piece == 0:  #Cas où le joueur veut quitter la partie
          relate_param(board, grid, 21)
          relate_param(board, grid, 20)
          relate_param(board, grid, 22)
          print_param(board, "**** A bientôt ****", grid, 21, 11)
          print_grid(board)
          sortie = True
        elif piece == 1:
          choix_bloc = bloc_1
        elif piece == 2:
          choix_bloc = bloc_2
        else:
          choix_bloc = bloc_3
  #code pour placer les blocs à l'endroit souhaiter par l'utilisateur Plus retrait d'essaie si emplacment impossible
      if sortie == False:
        est_valide = True
        while est_valide:
          lig = 0
          while lig < ord("A") or lig >= (
              ord("A") + len(grid)
          ):  # pour les emplacement dans le tableau, >=permet d'exclure le len pour ne pas sortir du cadre
            relate_param(board, grid, 21)
            relate_param(board, grid, 22)
            print_param(board, "Ligne cible : ", grid, 21,
                        11)  #le joueur sélectionne la ligne
            print_grid(board)
            coordonnee_choisie = input("")
            if len(coordonnee_choisie) != 1:
              lig = 0
            else:
              lig = ord(coordonnee_choisie)
          col = 0
          while col < ord("a") or col >= (ord("a") + len(
              grid[0])):  # >=permet d'exclure le len pour ne pas sortir du cadre
            relate_param(board, grid, 21)
            print_param(board, "Colonne cible : ", grid, 21,
                        11)  #le joueur sélectione la colonne
            print_grid(board)
            coordonnee_choisie = input("")
            if len(coordonnee_choisie) != 1:
              col = 0
            else:
              col = ord(coordonnee_choisie)
          # vérification de la position si celle ci est valide
          if verif_valid(
              grid, bloc_list[choix_bloc], lig - ord("A"),
              col - ord("a")) != True:  #vérifier si les blocs sont positionnable
            essai_restant -= 1  #retrait d'un essai par faute
            print_param(board, essai_restant, grid, 5, 25)
            if essai_restant == 0:
              relate_param(board, grid, 21)
              relate_param(board, grid, 20)
              relate_param(board, grid, 22)
              print_param(board, "**** GAME OVER ****", grid, 21,
                          11)
              print_grid(board)
              remove(path)
              remove(nom_score)
              remove(nom_bloc)
              sortie = True
              est_valide = False
          else:
            est_valide = False

            # si bloc bien positionné recommencer avec un autre blocs
            #réindenter les 10 lignes du dessous pour qu'elle soit dans le else
            grid = place_bloc(grid, bloc_list[choix_bloc], lig - ord("A"),
                              col - ord("a"))
            grid_(board, grid, 4)
            print_blocs(BLOC_VIDE, board, 12, grid)
            print_blocs(BLOC_VIDE, board, 19, grid)
            print_blocs(BLOC_VIDE, board, 26, grid)
            relate_param(board, grid, 21)
            relate_param(board, grid, 22)
            print_grid(
              board
            )  #oublie d'afficher le plateau donc nécessité d'ajouter cette lignes
            sleep(1.5)
            doit_sortir = True
        #############################################################

        #boucle pour l'affichage des score et l'effacement de ligne colonne si complete plus remonté les lignes quand l'une est complète
        if sortie == False:
          verifier = True
          while verifier:
            #initialiser les deux tableau
            lig_eff = []
            col_eff = []
            for i in range(
                len(grid) - 1, -1, -1
            ):  #parcourt des lignes pour supprimer celle pleine et remonter celle d'en dessous
              '''for i in range(len(grid)):'''
              if row_state(grid, i):
                lig_eff.append(i)
            for y in range(len(grid[0])):
              if col_state(
                  grid, y):  #parcourt les colonnes pour supprimer celle pleine
                col_eff.append(y)
            if len(lig_eff) != 0:
              for i in range(len(lig_eff)):
                Score += row_clear(grid, lig_eff[i])
            if len(col_eff) != 0:
              for j in range(len(col_eff)):
                Score += col_clear(grid, col_eff[j])
            if len(lig_eff) + len(col_eff) == 0:
              verifier = False
          grid_(board, grid, 4)
          print_score(board, Score, grid, 5, 14)
          print_blocs(BLOC_VIDE, board, 12, grid)
          print_blocs(BLOC_VIDE, board, 19, grid)
          print_blocs(BLOC_VIDE, board, 26, grid)
          relate_param(board, grid, 21)
          relate_param(board, grid, 22)
          essai_restant = 3
          print_param(board, essai_restant, grid, 5, 25)
