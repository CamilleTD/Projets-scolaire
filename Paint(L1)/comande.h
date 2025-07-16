#ifndef COMANDE_H
#define COMANDE_H
#include "area.h"

// Vector Text-based Editor//Fait par Marielle Dieuboue, Camille Tura-Durand et Manon Reny // le fichier COMANDE H est le fichier ou les fonctions sont énnoncé pour le main.
//définition de la structure commande 
struct command {
char name[50];
int int_size;
int int_params[10];
int str_size;
char* str_params[10];
}; typedef struct command Command;

//création fonction pour créer le main de facon optimisé
Command* create_commande();
void add_str_param(Command* cmd, char* p);
void add_int_param(Command* cmd, int p);
void free_cmd(Command* cmd);
int read_exec_command(Command* cmd, Area* area);
void read_from_stdin(Command* cmd);
int is_command_valid(Command* cmd);

#endif