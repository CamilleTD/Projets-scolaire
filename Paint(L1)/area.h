#ifndef AREA_H
#define AREA_H
#include "shape.h"
#define SHAPE_MAX 100 // Nombre maximum de formes
#define BOOL int

// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier AREA H est le fichier qui nous permet denoncer les differents prototypes pour dessiner les formes 

typedef struct {
    unsigned int
            width; // Nombre de pixels en largeur ou nombre de colonnes (axe y)
    unsigned int
            height; // Nombre de pixels en hauteur ou nombre de lignes (axe x)
    BOOL **mat; // Matrice des pixels de taille (width * height)
    Shape *shapes[SHAPE_MAX]; // Tableau des formes;
    int nb_shape; // Nombre de formes dans le tableau shapes (taille logique)
} Area;

//déclaration fonction area
Area *create_area(unsigned int width, unsigned int height);
void add_shape_to_area(Area *area, Shape *shape);
void clear_area(Area *area);
void erase_area(Area *area);
void delete_area(Area *area);
void draw_area(Area *area);
void print_area(Area *area);

typedef struct {
    int px;
    int py;
}Pixel;


//déclaration pixel
Pixel* create_pixel(int px, int py);
void delete_pixel(Pixel *pixel);

void pixel_forme(Shape* shape, Pixel** pixel, int* nb_pixels);
void pixel_point(Shape* shape, Pixel*** pixel_tab, int* nb_pixels);
void pixel_line(Shape* shape, Pixel*** pixel_tab, int* nb_pixels);
void pixel_circle(Shape* shape, Pixel*** pixel_tab, int *nb_pixels);
void pixel_square(Shape* shape, Pixel ***pixel, int *nb_pixels);
void pixel_rectangle(Shape* shape, Pixel ***pixel, int *nb_pixels);
void pixel_polygon(Shape* shape, Pixel*** pixel, int* nb_pixels);

Pixel **create_shape_to_pixel(Shape *shape, int *nb_pixels);
void delete_pixel_shape(Pixel **pixel, int nb_pixels);


#endif