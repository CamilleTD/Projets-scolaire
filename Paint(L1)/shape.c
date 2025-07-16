#include "shape.h"
#include <stdio.h>
#include <stdlib.h>
// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier C est le fichier où les fonctions sont définies.

// Fonction pour créer un point en mémoire par le biais de l'allocation dynamique
Point *create_point(int px, int py) {
    Point *point = (Point *)malloc(sizeof(Point));//alocation de la mémoire
    point->pos_x = px;//position x
    point->pos_y = py;//position y
    return point;
}

// Fonction pour supprimer un point de la mémoire
void delete_point(Point *point) { free(point); }//libère mémoire

// Fonction pour afficher un point
void print_point(Point *p) { printf("(%lf, %lf)\n", p->pos_x, p->pos_y); }//Affichage

// Fonction pour créer une line en mémoire par le biais de l'allocation
// dynamique
Line *create_line(Point *p1, Point *p2) {
    Line *line = (Line *)malloc(sizeof(Line));//aloue mémoire
    line->p1 = p1;//départ 
    line->p2 = p2;//arrivé
    return line;
}

// Fonction pour supprimer une line de la mémoire
void delete_line(Line *line) {
    delete_point(line->p1);//suppression départ arrivé
    delete_point(line->p2);
    free(line);
}

// Fonction pour afficher une line
void print_line(Line *line) {
    printf("line de ");
    print_point(line->p1);
    printf(" à ");
    print_point(line->p1);
    printf("\n");
}

// Fonction pour créer un square en mémoire par le biais de l'allocation
// dynamique
Square *create_square(Point *point, int length) {
    Square *square = (Square *)malloc(sizeof(Square));//allocation mémoire
    square->point = point;//point x et y
    square->length = length;//logngueur
    return square;
}

// Fonction pour supprimer un square de la mémoire
void delete_square(Square *square) {
    delete_point(square->point);//appelle suprime point
    free(square);//libère memoire
}

// Fonction pour afficher un square
void print_square(Square *square) {
    printf("square de coin ");
    print_point(square->point);
    printf("de côté %lf\n", square->length);
}

// Fonction pour créer un rectangle en mémoire par le biais de l'allocation
// dynamique
Rectangle *create_rectangle(Point *point, int height, int width) {
    Rectangle *rectangle = (Rectangle *)malloc(sizeof(Rectangle));//Allcoation mémoire
    rectangle->point = point;//point x et y
    rectangle->height = height;//hauteur
    rectangle->width = width;//largeur
    return rectangle;
}

// Fonction pour supprimer un rectangle de la mémoire
void delete_rectangle(Rectangle *rectangle) {
    delete_point(rectangle->point);//appelle point pour supprimer 
    free(rectangle);//libère mémoire
}

// Fonction pour afficher un rectangle
void print_rectangle(Rectangle *rectangle) {
    printf("rectangle de coin ");
    print_point(rectangle->point);
    printf("de longueur %f et de largeur %f\n", rectangle->height,
           rectangle->width);
}

// Fonction pour créer un circle en mémoire par le biais de l'allocation
// dynamique
Circle *create_circle(Point *center, int radius) {
    Circle *circle = (Circle *)malloc(sizeof(Circle));//allocation mémoire
    circle->center = center;//centre
    circle->radius = radius;//rayon
    return circle;
}

// Fonction pour supprimer un circle de la mémoire
void delete_circle(Circle *circle) {
    delete_point(circle->center);//appelle fonction pour suprimer
    free(circle);
}

// Fonction pour afficher un circle
void print_circle(Circle *circle) {
    printf("circle de center ");
    print_point(circle->center);
    printf("et de rayon %lf\n", circle->radius);
}

// Fonction pour créer un polygon en mémoire par le biais de l'allocation
// dynamique
Polygon *create_polygon(int n, Point **tab) {
    Polygon *polygon = (Polygon *)malloc(sizeof(Polygon));//alloue mémoire
    polygon->n = n;//Adapte nb point
    polygon->points = (Point **)malloc(n * sizeof(Point *));
    for (int i = 0; i < n; i++) {//parcourt nombre de point
        polygon->points[i] = (Point *)malloc(sizeof(Point));
        polygon->points[i]->pos_x = tab[i]->pos_x;//affecte x
        polygon->points[i]->pos_y = tab[i]->pos_y;//Affecte y
    }
    return polygon;
}

// Fonction pour supprimer un polygon de la mémoire
void delete_polygon(Polygon *polygon) {
    for (int i = 0; i < polygon->n; i++) {//suprimer chaque point en parcourant liste
        delete_point(polygon->points[i]);
    }
    free(polygon);
}

// Fonction pour afficher un polygon
void print_polygon(Polygon *polygon) {
    printf("polygon de %d points :\n", polygon->n);
    for (int i = 0; i < polygon->n; i++) {
        printf("\t");
        print_point(polygon->points[i]);
    }
}

/* alloue la zone mémoire qui contiendra un type de forme donné en paramètre */
Shape *create_empty_shape(SHAPE_TYPE shape_type) {
    Shape *shp = (Shape *)malloc(sizeof(Shape));//aloue mémoire
    shp->ptrShape = NULL;
    shp->id = 1; // plus tard on appelera get_next_id();
    shp->shape_type = shape_type;
    return shp;
}

// créer une fonction générique pour chaque type de forme
Shape *create_point_shape(int px, int py) {
    Shape *shp = create_empty_shape(POINT);//appelle fonction qui prend en paramètre la forme
    Point *p = create_point(px, py);//appelle point
    shp->ptrShape = p;
    return shp;
}

Shape *create_line_shape(int px1, int py1, int px2, int py2) {
    Shape *shp = create_empty_shape(LINE);//appelle fonction qui prend en paramètre la forme
    Line *l = create_line(create_point(px1, py1), create_point(px2, py2));//appelle ligne
    shp->ptrShape = l;
    return shp;
}

Shape *create_square_shape(int px, int py, int length) {
    Shape *shp = create_empty_shape(SQUARE);//appelle fonction qui prend en paramètre la forme
    Square *s = create_square(create_point(px, py), length);//appelle carré
    shp->ptrShape = s;
    return shp;
}

Shape *create_rectangle_shape(int px, int py, int width, int height) {
    Shape *shp = create_empty_shape(RECTANGLE);//appelle fonction qui prend en paramètre la forme
    Rectangle *r = create_rectangle(create_point(px, py), width, height);//appelle rectangle
    shp->ptrShape = r;
    return shp;
}

Shape *create_circle_shape(int px, int py, int radius) {
    Shape *shp = create_empty_shape(CIRCLE);//appelle fonction qui prend en paramètre la forme
    Circle *c = create_circle(create_point(px, py), radius);//appelle cercle
    shp->ptrShape = c;
    return shp;
}

Shape *create_polygon_shape(int liste_coords[], int n) {
    // on vérifie que l'ensemnle des coordonnées est paire (ensemble de points)
    if (n % 2 != 0) {
        printf("Erreur : le nombre de points doit être un multiple de deux.\n");
        return NULL;
    }
    // création d'une shape vide
    Shape *shp = create_empty_shape(POLYGON);
    int nb_points = n / 2;
    Point **liste_points = malloc(nb_points * sizeof(Point));

   
    for (int i = 0; i < n; i += 2) {// les deux premières coordonnées sont utilisées pour créer le reste des points
        liste_points[i / 2] = create_point(liste_coords[i], liste_coords[i + 1]);
    }
    Polygon *p = create_polygon(nb_points, liste_points);//appelle fonction polynome
    shp->ptrShape = p;
    return shp;
}

//fonction pour supprimer une forme 
void delete_shape(Shape *shape) {
    if (shape != NULL) {
        if (shape->ptrShape != NULL) {
            free(shape->ptrShape);
        }
        free(shape);//libère la mémoire
    }
}

//fonction pour afficher chaque forme
void print_shape(Shape *shape) {
    printf("id: %d, type: %d\n", shape->id, shape->shape_type);
    switch (shape->shape_type) {
        case POINT://cas point
            print_point((Point *)shape->ptrShape);
            break;
        case LINE://cas ligne
            print_line((Line *)shape->ptrShape);
            break;
        case SQUARE://cas carré
            print_square((Square *)shape->ptrShape);
            break;
        case RECTANGLE://cas rectangle
            print_rectangle((Rectangle *)shape->ptrShape);
            break;
        case CIRCLE://cas cercle
            print_circle((Circle *)shape->ptrShape);
            break;
        case POLYGON://cas polygone
            print_polygon((Polygon *)shape->ptrShape);
            break;
        default://cas si forme inexistante
            printf("Erreur : type de forme non reconnu.\n");
            break;
    }
}

int isinteger(char *n) {
  int i=0;
  int a=0;
  for(i = 0; n[i] != 0; i++) 
    if(n[i]  >= '0' &&  n[i] <= '9') 
      a++;
  return a / strlen(n);
}
