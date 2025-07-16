#include "shape.h"
#include "area.h"
#include "comande.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier MAIN C est le fichier du programme principal: Appel des fonctions.


#define AREA 25
int main() {

  // création d'une zone de dessin de 25 d'après la constante AREA
  Area* area = create_area(AREA,AREA);

  //Initialiser les formes utiliser dans le code
  Shape * line;
  Shape * rectangle;
  Shape * circle;
  Shape * point;
  Shape * square;
  Shape * polygon;

  //affiche zone de dessin en appelant area
  draw_area (area);
  print_area(area);
  
  int continuer =1;
  // Revenir à l'étape 1 (la boucle 'while' s'en charge)
    while (continuer) {
      
        // Etape 1 : Afficher un prompt
        printf("» ");

        // Etape 2 : Lire l'entrée de l'utilisateur
        Command* cmd = create_commande();
        read_from_stdin(cmd);

        // Etape 4 : Vérifier si la commande est correcte
       if (is_command_valid(cmd)) {
            // Etape 5 : Exécuter la commande de l'utilisateur
            switch (read_exec_command(cmd, area)) {
              // commande existante et réaliser
              case 0:
                printf("Command executed successfully.\n");
                break;
              //commande exit permet de quitter et donc message affiché
              case 1 :
                printf("Au revoir!");
                continuer = 0;
                break;
              // cas si les coordonné donné ne permette pas d'afficher la forme
              case 2:
                printf("Des coordonnées sont en dehors de l'aire\n");
                break;
              // si la commande existe mais mal utilise exemple ligne avec 2 arg au lieu de 4
              default:
                printf("Error executing command.\n");
                break;
            }
       }
         //si la commande n'existe pas
      else {
        printf("Invalid command.\n");
      }

        // Etape 6 : Libérer la mémoire allouée pour la structure 'cmd'
        free_cmd(cmd);
    }
    return 0;
}