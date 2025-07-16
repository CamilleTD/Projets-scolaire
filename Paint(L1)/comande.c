#include "comande.h"
#include "area.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define AREA 25

// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier COMANDE C est le fichier ou les fonctions pour créer le main sont écrite.
// créer une variable de type commande
Command *create_commande() {
  Command *cmd = (Command *)malloc(sizeof(Command)); // alloue de la mémoire
  cmd->int_size = 0; // initialise paramètre entier =0
  cmd->str_size = 0; // initialise paramètre caractère =0
  return cmd;
}

// ajoute une paramètre de chaine de caractère à la structure
void add_str_param(Command *cmd, char *p) {
  cmd->str_params[cmd->str_size] =
      strdup(p);   // dublique la chaine pour = str_param
  cmd->str_size++; // incrémente paramètre
}

// ajoute un paramètre entier à la structure
void add_int_param(Command *cmd, int p) {
  cmd->int_params[cmd->int_size] = p; // assigne p au tanleau
  cmd->int_size++;                    // incrémente la taille de paramètre
}

// supprimer une command donné en paramètre et libérer l’espaces occupé
void free_cmd(Command *cmd) {
  for (int i = 0; i < cmd->str_size; i++) {
    free(cmd->str_params[i]); // libère mémoire paramètre
  }
  free(cmd); // libère mémoire commande
}

// exécuter la commande saisie par l’utilisateur
int read_exec_command(Command *cmd, Area *area) {
  // Retournez 0 si la commande s'est exécutée avec succès, sinon retournez un
  // code d'erreur.
  if (strcmp(cmd->name, "clear") == 0) {
    system("clear"); // efface écran
    clear_area(area);
    draw_area(area);                           // dessine écran
    print_area(area);                          // affiche écran
  } else if (strcmp(cmd->name, "exit") == 0) { // exit quitter
    return 1; // Retourne 1 pour indiquer que le programme doit se terminer
    system("clear");
  } else if (strcmp(cmd->name, "line") == 0) { // ligne
    if (cmd->int_params[0] > AREA || cmd->int_params[0] < 0 ||
        cmd->int_params[1] > AREA || cmd->int_params[1] < 0 ||
        cmd->int_params[2] > AREA || cmd->int_params[2] < 0 ||
        cmd->int_params[3] > AREA ||
        cmd->int_params[3] < 0) // verifier que les 4 param ecrit sont en dehors
                                // des bornes de l'aire et 0
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher la ligne et la dessiner
      system("clear");
      Shape *line = create_line_shape(cmd->int_params[0], cmd->int_params[1],
                                      cmd->int_params[2], cmd->int_params[3]);
      add_shape_to_area(area, line);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "rectangle") == 0) { // rectangle
    if (cmd->int_params[0] > AREA || cmd->int_params[0] < 0 ||
        cmd->int_params[1] > AREA ||
        cmd->int_params[1] < 0) // verifier que les 4 param ecrit sont en dehors
                                // des bornes de l'aire et 0
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher le rectangle et la dessiner
      system("clear");
      Shape *rectangle =
          create_rectangle_shape(cmd->int_params[0], cmd->int_params[1],
                                 cmd->int_params[2], cmd->int_params[3]);
      add_shape_to_area(area, rectangle);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "square") == 0) { // carré
    if (cmd->int_params[0] > AREA || cmd->int_params[0] < 0 ||
        cmd->int_params[1] > AREA ||
        cmd->int_params[1] < 0) // verifier que les 3 param ecrit sont en dehors
                                // des bornes de l'aire et 0
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher le carré et la dessiner
      system("clear");
      Shape *square = create_square_shape(
          cmd->int_params[0], cmd->int_params[1], cmd->int_params[2]);
      add_shape_to_area(area, square);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "circle") == 0) { // cercle
    if (cmd->int_params[0] > AREA || cmd->int_params[0] < 0 ||
        cmd->int_params[1] > AREA ||
        cmd->int_params[1] < 0) // verifier que les 2 param ecrit sont en dehors
                                // des bornes de l'aire et 0
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher le cercle et la dessiner
      system("clear");
      Shape *circle = create_circle_shape(
          cmd->int_params[0], cmd->int_params[1], cmd->int_params[2]);
      add_shape_to_area(area, circle);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "point") == 0) { // point
    if (cmd->int_params[0] > AREA || cmd->int_params[0] < 0 ||
        cmd->int_params[1] > AREA ||
        cmd->int_params[1] < 0) // verifier que les 2 param ecrit sont en dehors
                                // des bornes de l'aire et 0
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher le point et la dessiner
      system("clear");
      Shape *point = create_point_shape(cmd->int_params[0], cmd->int_params[1]);
      add_shape_to_area(area, point);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "polygon") == 0) {
    int j = 0;
    for (int i = 1; i <= cmd->int_size;
         i++) // verifier que les i param ecrit sont en dehors des bornes de
              // l'aire et 0
      if (cmd->int_params[i] > AREA || cmd->int_params[i] < 0)
        j = 1;
    if (j != 0)
      return 2; // si condition vérifier alors renvoyé 2 qui signifie que les
                // coordonnée sont en dehors de l'aire
    else { // sinon afficher le polygon et la dessiner
      system("clear");
      Shape *polygon = create_polygon_shape(cmd->int_params, cmd->int_size);
      add_shape_to_area(area, polygon);
      draw_area(area);
      print_area(area);
    }
  } else if (strcmp(cmd->name, "plot") ==
             0) { // plot affiche l'écran tel qu'avant si on a été sur règle
                  // liste ou autre
    system("clear");
    draw_area(area);
    print_area(area);
  } else if (strcmp(cmd->name, "list") == 0) {
    system("clear");
    printf("===================\n");
    printf("====  L I S T  ====\n");
    printf("===================\n");
    printf("\n");
  } else if (strcmp(cmd->name, "help") == 0) { // Affiche l'aide du programme
    system("clear");
    printf("**************************************************\n");
    printf("****         VECTOR TEXT-BASED EDITOR         ****\n");
    printf("**************************************************\n");
    printf("==== Control ====\n");
    printf("clear : clear screen\n");
    printf("exit : exit the program\n");
    printf("help : print this help\n");
    printf("plot : draw dcreen\n");
    printf("==== Draw shapes ====\n");
    printf("point x1 y1 : create point a position (x1, y1)\n");
    printf("line x1 y1 x2 y2 : draw line from (x1, y1) to (x2, y2)\n");
    printf("square x1 y1 l : draw square (x1, y1)  length\n");
    printf("rectangle x1 y1 w h : draw square (x1, y1)  width height\n");
    printf("circle x y r : center at (x, y) radius r\n");
    printf("polygon x1 y1 x2 y2 ... : draw polygon\n");
    printf("==== Draw manager ====\n");
    printf("list : all command\n");
    printf("\n");
  }
  return 0;
}

// demande à l’utilisateur de saisir une ligne au clavier
void read_from_stdin(Command *cmd) {
  char input[256];
  char cmd2[256];
  int i, l;
  fgets(input, 256, stdin); // Lit l'entrée utilisateur depuis stdin
  int arg = 1;              // compte argument
  int j = 0;
  cmd->int_size = 0; // reinitialise taille paramètre entier
  cmd->str_size = 0; // reinitialise taille paramètre caractère
  for (i = 0; input[i] != '\n'; ++i) {
    if (input[i] == ' ') { // si espace recontré fin de l'argument
      if (arg == 1)
        strcpy(cmd->name, cmd2); // copie la commande
      else {
        if (isinteger(cmd2) == 1) { // vérifie c'est un entier
          sscanf(cmd2, "%d", &l);
          add_int_param(cmd, l); // ajoute 1 paramètre
        } else {
          add_str_param(cmd, cmd2); // ajoute le paramètre comme un caractère
        }
      }
      arg++;
      j = 0;
    } else {
      if (input[i] >= 'A' && input[i] <= 'Z') // conversion en minuscule
        cmd2[j] = input[i] + ('a' - 'A');
      else
        cmd2[j] = input[i];
      cmd2[j + 1] = '\0';
      j++; // incrémente j
    }
  }
  if (j != 0) {
    if (arg == 1)
      strcpy(cmd->name, cmd2);
    else {
      if (isinteger(cmd2) == 1) {
        sscanf(cmd2, "%d", &l);
        add_int_param(cmd, l);
      } else {
        add_str_param(cmd, cmd2);
      }
    }
  }
}

// Vérifie si la commande et ses paramètres correspondent à des commandes
// valides
int is_command_valid(Command *cmd) {
  if (strcmp(cmd->name, "clear") == 0 && cmd->int_size == 0 &&
      cmd->str_size == 0) // 0 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "exit") == 0 && cmd->int_size == 0 &&
             cmd->str_size == 0) // 0 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "point") == 0 && cmd->int_size == 2 &&
             cmd->str_size == 0) // 2 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "line") == 0 && cmd->int_size == 4 &&
             cmd->str_size == 0) // 4 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "circle") == 0 && cmd->int_size == 3 &&
             cmd->str_size == 0) // 3 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "square") == 0 && cmd->int_size == 3 &&
             cmd->str_size == 0) // 3 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "rectangle") == 0 && cmd->int_size == 4 &&
             cmd->str_size == 0) // 4 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "polygon") == 0 && cmd->int_size >= 6 &&
             cmd->int_size % 2 == 0 &&
             cmd->str_size ==
                 0) // au moins 6 paramètre qui doivent être paire car x et y
  {
    return 1;
  } else if (strcmp(cmd->name, "plot") == 0 && cmd->int_size == 0 &&
             cmd->str_size == 0) // 0 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "list") == 0 && cmd->int_size == 0 &&
             cmd->str_size == 0) // 0 paramètre
  {
    return 1;
  } else if (strcmp(cmd->name, "help") == 0 && cmd->int_size == 0 &&
             cmd->str_size == 0) // 0 paramètre
  {
    return 1;
  }
  return 0;
}