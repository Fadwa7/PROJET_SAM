# SAM-PROJECT
## SAM PROJET FOR UE HAI724I
Hi , welcome to our project. 😊

__Présentation :__  
SAMREADER est un script python qui permet à ses utilisateurs de manipuler les fichiers de type SAM, et pouvoir en extraire les informations dont ils ont besoin.

__Auteurs:__ 
AICHOUNE WAFA, EL KHADDAR FADWA

__contact:__  
wafa.aichoune@etu.umontpellier.fr, fadwa.el-khaddar@etu.umontpellier.fr

__version:__ 

0.0.1

__date:__  
14/12/2021

__licence:__ 
"This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details

__Exigences:__ :

Python3 est nécessaire pour le lancement du script. 
Si vous n'en avez pas, vous pouvez l'installer via le lien suivant https://www.python.org/downloads/

❗ ❗ Ce script fonctionne bien sur Linux, mais nous ne sommes pas sûres qu'il fonctionne également sur Windows.

__Mode d'emploi:__ 

🔴 Première étape : 

 - Télécharger le script python "script.py" via le lien https://github.com/Fadwa7/PROJET_SAM.git, et déposer le dans votre fichier SAM dans un seul répertoire.

🔴 Deuxième étape : 

- Ouvrir le terminal à partir du répertoire contenant vos fichiers.

🔴 Troisième étape: 

- Lancer la commande suivante : nohup python3 script.py <__nomFichier.sam__>

🔴 Quatrième Etape: 

- l'Output de cette commande, est un total de 4 fichiers décrits ci dessous: 

*noHup.out* : C'est un fichier contenant la lecture de votre fichier SAM, ensuite une liste de la colonne FLAG suivie de son écriture binaire, et finalement le CIGAR.

*summary_unmapped.txt* : Un fichier texte contenant le sommaire des reads non mappés. 

*summary_partially_mapped.txt* : Un fichier texte contenant le sommaire des reads partiellement mappés.

*only_unmapped.fasta* : Un fichier FASTA contenant les reads non mappés. 

*only_partially_mapped.fasta* : Ce fichier FASTA contient un read (read 1 ou read 2) qui est mappée et l'autre (read 1 ou read 2) qui est partiellement mappée.


__Exemples:__ 








 
       

