
#include "area.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//le "?" permet de comparer les deux valeurs et renvoyer si c'est le cas permet d'eviter répetition
#define min(i, j) (((i) < (j)) ? (i) : (j))
#define max(i, j) (((i) > (j)) ? (i) : (j))

// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier AREA C est le fichier ou les fonctions pour dessiner sont définies.

// permet de créer une zone area retournant un pointeur
Area *create_area(unsigned int width, unsigned int height) {
    Area *area = (Area *)malloc(sizeof(Area)); //allocation de la mémoire pour area
    area->width = width;//défini largeur
    area->height = height;//défini auteur
    area->nb_shape = 0;//nb de forme = 0 au début

    area->mat = (BOOL **)malloc(height * sizeof(BOOL *));//mémoire pour la matrice
    for (int i = 0; i < width; i++) {
        area->mat[i] = (BOOL *)calloc(width, sizeof(BOOL));//mémoire pour les ligne
    }
    return area;
}

// ajoute une forme à la zone de dessin
void add_shape_to_area(Area *area, Shape *shape) {
    if (area->nb_shape < SHAPE_MAX) {
        area->shapes[area->nb_shape] = shape;//ajoute forme a la l'area
        area->nb_shape++;//compte nombre de forme ajouter à l'area
    } else {
        printf("Erreur : nombre maximum de formes atteint.\n");//message si plus de forme possible
    }
}

// initialise tous les pixel à 0
void clear_area(Area *area) {
    for (int i = 0; i < area->height; i++) {
        for (int j = 0; j < area->width; j++) {
            area->mat[i][j] = 0;//Initialise chaque pixel à 0
        }
    }
    area->nb_shape = 0;//réinitialise le nombre de formes à 0
}

// supprime toutes les formes dessinées
void erase_area(Area *area) {
    for (int i = 0; i < area->nb_shape; i++) {
        free(area->shapes[i]);//libère la mémoire
        area->shapes[i] = NULL;// pointeur à nulle
    }
    area->nb_shape = 0;
}

// supprime une zone de dessin avec l’ensemble des formes associées
void delete_area(Area *area) {
    erase_area(area);// appelle fonction prédeente 
    for (int i = 0; i < area->height; i++) {
        free(area->mat[i]);//libère mémoire ligne
    }
    free(area->mat);//libère mémoire matrice
    free(area);//libère mémoire area
}

// dessiner une forme dans la zone de dessin
void draw_area(Area *area) {
    for (int i = 0; i < area->nb_shape; i++) {
        Shape *shape = area->shapes[i];
        int nb_pixel;
        Pixel **pixels = create_shape_to_pixel(shape, &nb_pixel);

        // matrice avec les pixels de la forme
        for (int j = 0; j < nb_pixel; j++) {
            int x = pixels[j]->px;
            int y = pixels[j]->py;
            if (x >= 0 && x < area->width && y >= 0 && y < area->height) {
                area->mat[x][y] = 1;
            }
        }
        free(pixels);
    }
}

//’afficher à l’écran les pixels de la matrice mat à l’aide de la fonction printf()
void print_area(Area *area) {
    for (int i = 0; i < area->height; i++) {//parcourt hauteur
        for (int j = 0; j < area->width; j++) {//parcourt largeur
            printf("%c ", area->mat[i][j] ? '#' : '.');// affiche point pour l'area # les forme
        }
        printf("\n");
    }
}

//’allouer un espace mémoire de type Pixel
Pixel *create_pixel(int px, int py) {
    Pixel *new_pixel = (Pixel *)malloc(sizeof(Pixel));//allocation pixel 
    new_pixel->px = px;//initialise coordonnée px
    new_pixel->py = py;//initialise coordonnée py
    return new_pixel;
}

// libérer l'espace de la mémoire
void delete_pixel(Pixel *pixel) { free(pixel); }

// stocke info pour dessiner point
void pixel_point(Shape *shape, Pixel ***pixel_tab, int *nb_pixels) {
    Point *pt = (Point *)shape->ptrShape;
    *pixel_tab = (Pixel **)malloc(sizeof(Pixel *));//alloue de la mémoire
    *pixel_tab[0] = create_pixel(pt->pos_x, pt->pos_y);//crée pixel avec coordonnée
    *nb_pixels = 1;//mettre à jour pixel
}

// stocke info pour dessiner ligne
void pixel_line(Shape *shape, Pixel ***pixel_tab, int *nb_pixels) {
  Line *pt = (Line *)shape->ptrShape;

  int xA = pt->p1->pos_x, yA = pt->p1->pos_y;
  int xB = pt->p2->pos_x, yB = pt->p2->pos_y;

  if (xA < xB) { // on trace vers la droite
    int dx = xB - xA;
    int dy = yB - yA;
    int dmin = min(dx, abs(dy));
    int dmax = max(dx, abs(dy));

    Pixel **tmp_tab = (Pixel **)malloc((dmax + 1) * sizeof(Pixel *));//alloue de la mémoire pour tableau temporaire

    int nb_segs = dmin + 1;
    int taille_segment = (dmax + 1) / (dmin + 1);
    int restants = (dmax + 1) % (dmin + 1);

    int segments[nb_segs];
    for (int i = 0; i < nb_segs; i++) {
      segments[i] = taille_segment;
    }

    int *cumuls = (int *)malloc(nb_segs * sizeof(int));
    cumuls[0] = 0;

    for (int i = 2; i < nb_segs + 1; i++) {
      cumuls[i - 1] =
          ((i * restants) % (dmin + 1) < ((i - 1) * restants) % (dmin + 1));
    }

    for (int i = 0; i < nb_segs; i++) {
      segments[i] = segments[i] + cumuls[i];
    }

    if (dy < 0) {         // on trace vers le bas
      if (dx > abs(dy)) { // les segments sont horizontaux
        int tmpx = xA, tmpy = yA;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpx++;
          }
          tmpy--;
        }
      } else { // les segments sont verticaux
        int tmpx = xA, tmpy = yA;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpy--;
          }
          tmpx++;
        }
      }
    } else {         // on trace vers le haut
      if (dx > dy) { // les segments sont horizontaux
        int tmpx = xA, tmpy = yA;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpx++;
          }
          tmpy++;
        }
      } else { // les segments sont verticaux
        int tmpx = xA, tmpy = yA;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpy++;
          }
          tmpx++;
        }
      }
    }
    *pixel_tab = tmp_tab;
  } else { // on trace vers ma gauche
    int dx = xA - xB;
    int dy = yA - yB;
    int dmin = min(dx, abs(dy));
    int dmax = max(dx, abs(dy));

    Pixel **tmp_tab = (Pixel **)malloc((dmax + 1) * sizeof(Pixel *));

    int nb_segs = dmin + 1;
    int taille_segment = (dmax + 1) / (dmin + 1);
    int restants = (dmax + 1) % (dmin + 1);

    int segments[nb_segs];
    for (int i = 0; i < nb_segs; i++) {
      segments[i] = taille_segment;
    }

    int *cumuls = (int *)malloc(nb_segs * sizeof(int));
    cumuls[0] = 0;

    for (int i = 2; i < nb_segs + 1; i++) {
      cumuls[i - 1] =
          ((i * restants) % (dmin + 1) < ((i - 1) * restants) % (dmin + 1));
    }

    for (int i = 0; i < nb_segs; i++) {
      segments[i] = segments[i] + cumuls[i];
    }

    if (dy < 0) {         // on trace vers le bas
      if (dx > abs(dy)) { // les segments sont horizontaux
        int tmpx = xB, tmpy = yB;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpx++;
          }
          tmpy--;
        }
      } else { // les segments sont verticaux
        int tmpx = xB, tmpy = yB;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpy--;
          }
          tmpx++;
        }
      }
    } else {         // on trace vers le haut
      if (dx > dy) { // les segments sont horizontaux
        int tmpx = xB, tmpy = yB;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpx++;
          }
          tmpy++;
        }
      } else { // les segments sont verticaux
        int tmpx = xB, tmpy = yB;
        for (int i = 0; i < nb_segs; i++) {
          for (int j = 0; j < segments[i]; j++) {
            tmp_tab[*nb_pixels] = create_pixel(tmpx, tmpy);
            (*nb_pixels)++;
            tmpy++;
          }
          tmpx++;
        }
      }
    }
    *pixel_tab = tmp_tab;
  }
}

// stocke info pour dessiner cercle
void pixel_circle(Shape* shape, Pixel*** pixel_tab, int* nb_pixels){

    Circle* cercle = (Circle*) shape->ptrShape;
    Pixel** tmp_tab = (Pixel**) malloc ((cercle->radius+1)*8 *sizeof (Pixel*));
    int x = 0;
    int y = cercle->radius;
    int d = cercle->radius - 1;
    Pixel* pix = NULL;
    while (y >= x){
        // octant 1
      // Ajouter le point pour le premier octant
        pix = create_pixel(cercle->center->pos_x + x, cercle->center->pos_y + y);
        tmp_tab[(*nb_pixels)++] = pix;
        // Ajouter le point pour l’octant d’en face
        pix = create_pixel(cercle->center->pos_x + y, cercle->center->pos_y + x);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 3
        pix = create_pixel(cercle->center->pos_x - x, cercle->center->pos_y + y);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 4
        pix = create_pixel(cercle->center->pos_x - y, cercle->center->pos_y + x);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 5
        pix = create_pixel(cercle->center->pos_x + x, cercle->center->pos_y - y);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 6
        pix = create_pixel(cercle->center->pos_x + y, cercle->center->pos_y - x);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 7
        pix = create_pixel(cercle->center->pos_x - x, cercle->center->pos_y - y);
        tmp_tab[(*nb_pixels)++] = pix;
        // octant 8
        pix = create_pixel(cercle->center->pos_x - y, cercle->center->pos_y - x);
        tmp_tab[(*nb_pixels)++] = pix;

        if (d >= 2 * x){
            d -= 2 * x + 1;
            x++;
        }else if (d <= 2 * (cercle->radius - y)){
            d += 2 * y - 1;
            y--;
        }else{
            d += 2 * (y - x - 1);
            x++;
            y--;
        }
    }
    *pixel_tab = tmp_tab;
}

// stocke info pour dessiner carré
void pixel_square(Shape *shape, Pixel ***pixel, int *nb_pixels) {
    Square* square = shape->ptrShape;//déclare pointeur
    int px = square->point->pos_x;//position x
    int py = square->point->pos_y;//position y
    int length = square->length;//coté
    Pixel *tmp_tab[4 * length];//tableau pour 4 coté
    int tmp_nb_pixels = 0;

    for (int i = 0; i < length; i++) {//bouvcle pour désiner 4 coté
        tmp_tab[tmp_nb_pixels++] = create_pixel(px + i, py);
        tmp_tab[tmp_nb_pixels++] = create_pixel(px + i, py + length - 1);
        tmp_tab[tmp_nb_pixels++] = create_pixel(px, py + i);
        tmp_tab[tmp_nb_pixels++] = create_pixel(px + length - 1, py + i);
    }

    *nb_pixels = tmp_nb_pixels;//affecte tableau
    *pixel = (Pixel**)malloc(tmp_nb_pixels * sizeof(Pixel*));//alloue mémoire
    memcpy(*pixel, tmp_tab, tmp_nb_pixels * sizeof(Pixel*));
}

//stocke info pour dessiner rectangle
void pixel_rectangle(Shape *shape, Pixel ***pixel, int *nb_pixels) {
  Rectangle* rectangle = shape->ptrShape;//déclare pointeur
  int px = rectangle->point->pos_x;//position x
  int py = rectangle->point->pos_y;//position y
  int width = rectangle->width;//largeur
  int height = rectangle->height;//hauteur

  Pixel *tmp_tab[2 * (width + height)];//dessin rectangle 2 2 coté
  int tmp_nb_pixels = 0;

  for (int i = 0; i < width; i++) {//dessiné hauteur
    tmp_tab[tmp_nb_pixels++] = create_pixel(px + i, py);
    tmp_tab[tmp_nb_pixels++] = create_pixel(px + i, py + height - 1);
  }

  for (int i = 1; i < height - 1; i++) { //dessiner largeur
    tmp_tab[tmp_nb_pixels++] = create_pixel(px, py + i);
    tmp_tab[tmp_nb_pixels++] = create_pixel(px + width - 1, py + i);
  }

    *nb_pixels = tmp_nb_pixels;//affecte tableau
    *pixel = (Pixel**)malloc(tmp_nb_pixels * sizeof(Pixel*));//alloue mémoire
    memcpy(*pixel, tmp_tab, tmp_nb_pixels * sizeof(Pixel*));
}

void pixel_polygon(Shape* shape, Pixel*** pixel_tab, int* nb_pixels){
    Polygon* poly = (Polygon*) shape->ptrShape;//déclare pointeur
    // recherche de la taille
    int taille_tot = 0;
    int nb_pixel_tmp = 0;

    for (int i = 0; i<poly->n-1;i++){

        Pixel** null_tab = NULL;
        Shape* tmp_L = create_line_shape(poly->points[i]->pos_x,poly->points[i]->pos_y,poly->points[i+1]->pos_x,poly->points[i+1]->pos_y);// crée des lignes par rapport au nombre de sommet choisit
        nb_pixel_tmp = 0;
        pixel_line(tmp_L,&null_tab,&nb_pixel_tmp);
        taille_tot += nb_pixel_tmp;
    }

    Pixel** null_tab = NULL;
    Shape* L = create_line_shape(poly->points[0]->pos_x,poly->points[0]->pos_y,poly->points[poly->n-1]->pos_x,poly->points[poly->n-1]->pos_y);
    nb_pixel_tmp = 0;
    pixel_line(L,&null_tab,&nb_pixel_tmp);
    taille_tot += nb_pixel_tmp;

    Pixel** tmp_tab_all = (Pixel**) malloc (taille_tot*sizeof (Pixel*));

    // remplissage du tableau
    for (int i = 0; i<poly->n-1;i++){

        Pixel** tmp_tab = NULL;
        Shape* tmp_L = create_line_shape(poly->points[i]->pos_x,poly->points[i]->pos_y,poly->points[i+1]->pos_x,poly->points[i+1]->pos_y);
        nb_pixel_tmp = 0;
        pixel_line(tmp_L,&tmp_tab,&nb_pixel_tmp);

        for (int j = 0;j<nb_pixel_tmp;j++) {
            tmp_tab_all[*nb_pixels] = tmp_tab[j];
            (*nb_pixels)++;
        }
    }

    Pixel** tmp_tab = NULL;
    Shape* tmp_L = create_line_shape(poly->points[0]->pos_x,poly->points[0]->pos_y,poly->points[poly->n-1]->pos_x,poly->points[poly->n-1]->pos_y);
    nb_pixel_tmp = 0;
    pixel_line(tmp_L,&tmp_tab,&nb_pixel_tmp);
    for (int j = 0;j<nb_pixel_tmp;j++) {
        tmp_tab_all[*nb_pixels] = tmp_tab[j];
        (*nb_pixels)++;
    }
    *pixel_tab = tmp_tab_all;
}

// fonction qui prend en paramètre une forme quelconque de type Shape et qui génère l’ensemble de pixels la constituant
Pixel **create_shape_to_pixel(Shape *shape, int *nb_pixels) {
    Pixel **pixel_tab;//déclare pointeur
    switch (shape->shape_type) {
        case POINT://cas point appeler point
            pixel_point(shape, &pixel_tab, nb_pixels);
            break;
        case LINE://cas ligne appeler ligne
            pixel_line(shape, &pixel_tab, nb_pixels);
            break;
       case RECTANGLE://cas rectangle appeler rectangle
            pixel_rectangle(shape, &pixel_tab, nb_pixels);
            break;
        case CIRCLE://cas cercle appeler cercle
            pixel_circle(shape, &pixel_tab, nb_pixels);
            break;
        case SQUARE://cas carré appeler carré
            pixel_square(shape, &pixel_tab, nb_pixels);
            break;
        case POLYGON://cas polygone appeler polygone
            pixel_polygon(shape, &pixel_tab, nb_pixels);
            break;
        default:
            // gérer les cas d'erreur ou de forme non reconnue
            break;
    }
    return pixel_tab;
}

// liberer la mémoire de pixel alouer
void delete_pixel_shape(Pixel **pixel, int nb_pixels) {
    for (int i = 0; i < nb_pixels; i++) {
        free(pixel[i]);//libère la mémoire
    }
    free(pixel);
}

