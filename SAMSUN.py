import os
import sys
import re


def flagBinary(flag) : #fonction : convertion du FLAG en binaire

    flagB = bin(int(flag)) # Transform the integer into a binary.
    flagB = flagB[2:] # Remove '0b' Example: '0b1001101' > '1001101'
    flagB = list(flagB) 
    if len(flagB) < 12: # Size adjustement to 12 (maximal flag size)
        add = 12 - len(flagB) # We compute the difference between the maximal flag size (12) and the length of the binary flag.
        for t in range(add): 
            flagB.insert(0,'0') # We insert 0 to complete until the maximal flag size.
    return flagB
                
def unmapped(line): # fonction comptage des reads non mappés
    
    unmapped_count = 0
    with open ("only_unmapped.sam", "a+") as unmapped_sam, open("summary_unmapped.txt", "w") as summary_file:
        col_line = line.split("\t")
        print(col_line)
        flag = flagBinary(col_line[1])

        if int(flag[-3]) == 1:
            unmapped_count += 1
            unmapped_sam.write(line)

        summary_file.write("Total unmapped reads: " + str(unmapped_count) + "\n") 
    return unmapped_count

def partiallyMapped(line): # fonction de comptage des reads partiellement mappés
    
    partially_mapped_count = 0

    with open ("only_partially_mapped.sam", "a+") as partillay_mapped_sam, open("summary_partially_mapped.txt", "w") as summary_file:
        col_line = line.split("\t")
        flag = flagBinary(col_line[1]) # We compute the same 

        if int(flag[-2]) == 1: 
            if col_line[5] != "100M":
                partially_mapped_count += 1
                partillay_mapped_sam.write(line)

        summary_file.write("Total partially mapped reads: " + str(partially_mapped_count) + "\n") 
    return partially_mapped_count

def main() :   #fonction d'execution du script de lecture, stockage et analyse d'un fichier SAM
    print(sys.argv[0])
    print(sys.argv[1])
    file = sys.argv[1]

    flag = []
    cigar = []
    separedLines = []

    extension = os.path.splitext(sys.argv[1])

    if os.path.isfile(file):  # vérifier que c'est bien un fichier

        if os.path.getsize(file) > 0:  # vérifier que le fichier n'est pas vide
            print(extension)
            if ".sam".__eq__(extension[1]):  # vérifier que le fichier est bien un SAM

                # lecture du fichier et stockage de la section header dans une liste
                Header = []
                with open(file, "r") as f:
                    contenu = f.readlines()
                    for line in contenu:
                        if line.startswith("@"):
                            Header.append(line)
                            print("-----------------Header------------- : ", Header)
                        else:                                                       
                            if len(Header) == 0: # verifier que la section header existe
                                print("SAM ERRONE : ce fichier SAM ne contient pas de section HEADER")
                                exit()
                            else :
                                unmapped(line)
                                partiallyMapped(line)
                                separedLines = line.split("	")
                                flag.append(separedLines[1]) #insérer le contenu du flag dans la liste flag
                                cigar.append(separedLines[5]) #insérer le contenu du cigar dans la liste cigar
                
                print("------------------------------------------------------- FLAG -------------------------------------------------------")
                if len(flag)==0 : #vérifier que la liste FLAG existe bien
                    print("SAM ERRONE: le FLAG est vide")
                else :

                    print(flag)  

                for f in flag:

                    print("binary flag ", flagBinary(f))

                print("------------------------------------------------------- CIGAR --------------------------------------------------------")
                if len(cigar)==0 : #vérifier que la liste CIGAR existe bien
                    print ("SAM ERRONE : le CIGAR est vide")
                else : 
                    
                    print(cigar)

            else:
                print("ERROR, le fichier n'est pas de type SAM")
                exit()
        else:
            print("ERROR, le fichier est vide")
            exit()
    else:
        print("ERROR, ce n'est pas un fichier")
        exit()


def main() :  # main d'exécution du script
   




main()


