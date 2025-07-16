#ifndef SHAPE_H
#define SHAPE_H
// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier H est le Fichier entête contenant la déclaration des prototypes des fonctions, la déclaration des types.

// Définition des types
// Définition de la structure Point,
typedef struct {
    int pos_x;
    int pos_y;
} Point;

// Définition de la structure Ligne
typedef struct {
    Point *p1;
    Point *p2;
} Line;

// Définition de la structure Carre
typedef struct {
    Point *point;
    int length;
} Square;

// Définition de la structure Rectangle
typedef struct {
    Point *point;
    int height;
    int width;
} Rectangle;

//  Définition de la structure Cercle
typedef struct {
    Point *center;
    int radius;
} Circle;

// Définition de la structure Polygone
typedef struct {
    int n;
    Point **points; // tableau 1D dynamique de Point*
} Polygon;

// définition de l'énumération Shape_type
typedef enum { POINT, LINE, SQUARE, RECTANGLE, CIRCLE, POLYGON } SHAPE_TYPE;

// Définition de la structure Shape permettant d'associer à chaque forme géométrique un identifiant unique
typedef struct shape {
    int id;                // identifiant unique de la forme
    SHAPE_TYPE shape_type; // type de la forme pointé
    void *ptrShape;        // pointeur sur n'importe quelle forme
} Shape;

// Déclaration des fonctions des forme
//point
Point *create_point(int px, int py);
void delete_point(Point *point);
void print_point(Point *p);

//ligne
Line *create_line(Point *p1, Point *p2);
void delete_line(Line *line);
void print_line(Line *line);

//Carré
Square *create_square(Point *point, int lenght);
void delete_square(Square *square);
void print_square(Square *square);

//rectangle
Rectangle *create_rectangle(Point *point, int height, int width);
void delete_rectangle(Rectangle *rectangle);
void print_rectangle(Rectangle *rectangle);

//Cercle
Circle *create_circle(Point *center, int radius);
void delete_circle(Circle *circle);
void print_circle(Circle *circle);

//polygon
Polygon *create_polygon(int n, Point **tab);
void delete_polygon(Polygon *polygon);
void print_polygon(Polygon *polygon);

//déclaration fonction shape
Shape *create_empty_shape(SHAPE_TYPE shape_type);
Shape *create_point_shape(int px, int py);
Shape *create_line_shape(int px1, int py1, int px2, int py2);
Shape *create_square_shape(int px, int py, int length);
Shape *create_rectangle_shape(int px, int py, int width, int height);
Shape *create_circle_shape(int px, int py, int radus);
Shape *create_polygon_shape(int lst[], int n);
void delete_shape(Shape *shape);
void print_shape(Shape *shape);

int isinteger(char *n);

#endif
