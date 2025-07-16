-- Appel des différentes tables ou des contraintes de validations sont nécessaires
describe LIVRABLE;
describe EMPLOYE;
describe CONTRAT;

-- tables LIVRABLE ajout d'une contrainte de dates
alter table LIVRABLE 
add constraint ck_datelivraison
check (date_livraison between '2024-01-01' and '2026-12-31');

-- tables EMPLOYE ajout d'une contrainte de dates
alter table EMPLOYE
add constraint ck_dateembauche
check (date_embauche between '2022-01-01' and '2026-12-31');

-- tables EMPLOYE ajout d'une contrainte pour que la commission soit au moins positive
alter table EMPLOYE
add constraint ck_comission
check (commission >= 0);

-- tables EMPLOYE ajout d'une contrainte pour que le salaire soit au moins positif
alter table EMPLOYE
add constraint ck_salaire
check (salaire >= 0);

-- tables CONTRAT ajout d'une contrainte de dates
alter table CONTRAT
add constraint ck_datedebut
check (date_debut between '2024-01-01' and '2026-12-31');

-- tables CONTRAT ajout pour que le tarif soit au moins positif
alter table CONTRAT
add constraint ck_tarif
check (tarif >= 0);

