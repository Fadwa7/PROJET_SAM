# SAM-PROJECT
## SAM PROJET FOR UE HAI724I
Hi , welcome to our project. 😊

__Presentation :__  
SAMSUN est un script python qui permet à ses utilisateurs de manipuler les fichiers de type SAM (Section Alignement/Map format). SAM est  un fichier de format de texte délimité par des tabulations composé d'une section Header, et une section d'alignement comportant 11 sections dont les sections FLAG et CIGAR. SAMSUN permet d'extraire les informations contenues dans les FLAG et CIGAR.

__Authors:__ 

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

__Pré-requis__ :

❗❗ Python3 est nécessaire pour le lancement du script. 
Si vous n'en avez pas, vous pouvez l'installer via le lien suivant https://www.python.org/downloads/

❗❗ Ce script fonctionne bien sur Linux, mais nous ne sommes pas sûres qu'il fonctionne également sur Windows ou sur Mac. 

❗❗ Ce script ne prend en compte que les fichiers SAM non erronés et contenant impérativement une section Header. Merci de vérifier vos fichiers SAM à analyser avant de lancer le script. 
❗❗ Le script ne lit qu'un fichier SAM à la fois.

❗❗ Il n'ya pas de librairies spécifiques à télécharger.

__Installation and script running:__

❗ __Pour le bon usage de script, nous vous proposons les étapes ci-dessous, MAIS, vous pouvez lancer le script selon vos préférences__ ❗

🔴 Première étape : 

 - Télécharger le script python "SAMSUN.py" via le lien https://github.com/Fadwa7/PROJET_SAM.git, et déposer le dans un répertoire contenant également le fichier SAM que vous souhaiter traité.

🔴 Deuxième étape : 

- Ouvrir le terminal à partir du répertoire contenant vos fichiers.

🔴 Troisième étape: 

- Lancer le script. Nous vous recommandons la commande suivante : nohup python3 SAMSUN.py <__nomFichier.sam__>

🔴 Quatrième Etape: 

- l'Output de cette commande, est un total de 5 fichiers décrits ci dessous: 

*noHup.out* : C'est un fichier contenant la lecture de votre fichier SAM, ensuite une liste de la colonne FLAG suivie de son écriture binaire, et finalement le CIGAR.

*summary_unmapped.txt* : Un fichier texte contenant le sommaire des reads non mappés. 

*summary_partially_mapped.txt* : Un fichier texte contenant le sommaire des reads partiellement mappés.

*only_unmapped.sam* : Un fichier FASTA contenant les reads non mappés. 

*only_partially_mapped.sam* : Ce fichier FASTA contient un read (read 1 ou read 2) qui est mappée et l'autre (read 1 ou read 2) qui est partiellement mappée.



__FAQ:__: 

🔷 __Quelle est la durée moyenne du traitement d'un seul fichier ?__
  
  *La durée moyenne de traitement d'un fichier SAM par SAMSUN varie entre 5 à 15 minutes, selon la taille du fichier SAM traité*
  
🔷 __Pourquoi recommandez-vous d'utiliser nohup ?__ 
 
 *Nohup est une commande qui permet de lancer un processus qui restera actif même après la déconnexion de l'utilisateur, notre choix s'est porté sur cette commande, car la console de python, ne permet pas d'afficher tous les résultats de traitement, mais Nohup permet d'affichier le script entier en fichier externe. Si vous choisissez d'utiliser Nohup, nous vous conseillons de renommer vos fichiers de sortie nohup.out de la façon suivante : nohup python3 SAMSUN.py NomFichier.sam  >  Nom.out*
 
__BYE__ ✨ 
 







 
       

