CREATE TABLE utilisateur(
id_utilisateur SERIAL PRIMARY KEY,
nom VARCHAR(50) NOT NULL,
prenom VARCHAR(50) NOT NULL,
telephone VARCHAR(50) NOT NULL UNIQUE,
image VARCHAR(50) NOT NULL,
login VARCHAR(50) NOT NULL UNIQUE,
mot_de_passe VARCHAR(100) NOT NULL,
role VARCHAR(50) NOT NULL
);

CREATE TABLE administrateur(
id_admin SERIAL PRIMARY KEY,
id_utilisateur INT NOT NULL,
FOREIGN KEY(id_utilisateur)
REFERENCES utilisateur(id_utilisateur)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE client(
id_client SERIAL PRIMARY KEY,
id_utilisateur INT NOT NULL,
FOREIGN KEY(id_utilisateur)
REFERENCES utilisateur(id_utilisateur)
ON DELETE CASCADE
ON UPDATE CASCADE
);


CREATE TABLE vehicule(
id_vehicule SERIAL PRIMARY KEY,
marque VARCHAR(50),
modele VARCHAR(50),
prix_par_jour REAL,
id_admin INT NOT NULL,
photo bytea,
FOREIGN KEY(id_admin)
REFERENCES administrateur(id_admin)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE reservation(
id_reservation SERIAL PRIMARY KEY,
date_reservation DATE,
id_admin INT,
id_client INT NOT NULL,
	
FOREIGN KEY(id_client)
REFERENCES client(id_client)
ON DELETE CASCADE
ON UPDATE CASCADE,
	
FOREIGN KEY(id_admin)
REFERENCES administrateur(id_admin)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE details_reservation(
id_vehicule INT,
id_reservation INT,
date_recuperation DATE,
date_retour DATE,
FOREIGN KEY(id_vehicule)
REFERENCES vehicule(id_vehicule)
ON DELETE CASCADE
ON UPDATE CASCADE,
	
FOREIGN KEY(id_reservation)
REFERENCES reservation(id_reservation)
ON DELETE CASCADE
ON UPDATE CASCADE
);