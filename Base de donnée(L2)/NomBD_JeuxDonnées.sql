-- ajout de 6 données dans la table DEPARTEMENT
INSERT INTO DEPARTEMENT (id_departement, nom)
VALUES (1, 'Marketing'),
       (2, 'Sales'),
       (3, 'Engineering'),
       (4, 'Human Resources'),
       (5, 'Finance'),
       (6, 'Customer Service');

-- ajout de 8 données dans la table JOB
INSERT INTO JOB (id_job, nom)
VALUES (1, 'Software Developer'),
       (2, 'Marketing Manager'),
       (3, 'Sales Representative'),
       (4, 'Human Resources Specialist'),
       (5, 'Account Manager'),
       (6, 'Business Analyst'),
       (7, 'Content Writer'),
       (8, 'User Experience (UX) Designer');

-- ajout de 6 données dans la table MISSION
INSERT INTO MISSION (id_mission, nom, description)
VALUES (1, 'Develop e-commerce platform', 'Create a user-friendly online store for a clothing retailer'),
       (2, 'Design marketing campaign', 'Develop a comprehensive marketing strategy to reach new customers'),
       (3, 'Implement CRM system', 'Set up a customer relationship management system for improved client interactions'),
       (4, 'Develop internal communication strategy', 'Create a plan to improve communication and collaboration within the company'),
       (5, 'Update company website', 'Redesign and update the company website to reflect the latest brand identity and improve user experience'),
       (6, 'Conduct market research', 'Gather data and insights on customer preferences, market trends, and competitor analysis');
       
-- ajout de 6 données dans la table LIVRABLE
INSERT INTO LIVRABLE (id_livrable, nom, description, date_livraison, id_mission)
VALUES (1, 'Backend development', 'Develop the server-side functionality of the e-commerce platform', '2024-04-30', 1),
       (2, 'Marketing materials', 'Create brochures, social media posts, and email campaigns', '2024-04-15', 2),
       (3, 'CRM system configuration', 'Set up user accounts, customize workflows, and integrate with existing systems', '2024-05-10', 3),
       (4, 'Content calendar', 'Develop a plan for creating and publishing content across various marketing channels', '2024-05-20', 4),
       (5, 'Wireframes and prototypes', 'Create low-fidelity and high-fidelity wireframes and prototypes for the new website design',	'2024-04-25', 5),
       (6, 'Market research report', 'Compile and analyze data from market research activities, presenting key findings and recommendations', '2024-06-15',6);

-- ajout de 4 données dans la table CLIENT
INSERT INTO CLIENT (id_client, nom, adresse)
VALUES (1, 'ABC Clothing', '123 Main Street, Anytown, CA 12345'),
       (2, 'Tech Solutions Inc.', '456 Elm Street, Springfield, NY 54321'),
       (3, 'GreenTech Solutions', '789 Oak Avenue, Sunnyvale, CA 94089'),
       (4, 'Medical Supplies Inc.', '45 High Street, Boston, MA 02110');

-- ajout de 8 données dans la table QUALIFICATION
INSERT INTO QUALIFICATION (id_qualification, nom)
VALUES (1, 'Software Engineering'),
       (2, 'Marketing'),
       (3, 'Sales'),
       (4, 'Human Resources Management'),
       (5, 'Project Management'),
       (6, 'Graphic Design'),
       (7, 'Copywriting'),
       (8, 'Data Analysis');

-- ajout de 4 données dans la table CONTRAT
INSERT INTO CONTRAT (id_contrat, description_intervenant, date_debut, tarif, id_qualification, id_client)
VALUES (1, 'Develop mobile app for fitness tracker', '2024-02-15', 12000.00, 1, 1),
       (2, 'Create social media marketing strategy', '2024-03-01', 8000.00, 2, 2),
       (3, 'Develop e-learning modules', '2024-03-15', 15000.00, 5, 3),
       (4, 'Design company logo and branding materials', '2024-04-01', 10000.00, 6, 4);

-- ajout de 7 données dans la table EMPLOYE
INSERT INTO EMPLOYE (id_employe, nom, date_embauche, commission, salaire, id_qualification, id_employe_1, id_job, id_departement)
VALUES (1, 'John Doe', '2023-01-01', 0.10, 80000.00, 1, NULL, 1, 1),
       (2, 'Jane Smith', '2022-06-15', 0.15, 75000.00, 2, 1, 2, 1),
       (3, 'Michael Lee', '2023-07-20', 0.05, 65000.00, 3, 2, 3, 2),
       (4, 'Alice Johnson', '2024-02-05', 0.20, 50000.00, 4, 3, 1, 3),
       (5, 'David Jones', '2023-05-12', 0.05, 70000.00, 3, NULL, 5, 2),
       (6, 'Sarah Rodriguez', '2024-01-10', 0.10, 60000.00, 7, 1, 7, 1),
       (7, 'Emily Williams', '2023-11-08', 0.00, 55000.00, 8, 5, 8, 3);

-- ajout de donnée aux 2 association car (1,N) de chaque coté 
INSERT INTO Effectue (id_employe, id_mission)
VALUES (1, 1); 

INSERT INTO Concerne (id_employe, id_contrat)
VALUES (1, 1);
