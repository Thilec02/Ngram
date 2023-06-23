# N-Gram Program by Thilec02
# 2023 For Iris Robotics

def tuple_Ngram(n, liste_mots):
    """
    Crée des tuples avec les indices de liste_mots
    :param n: Taille du tuple
    :param liste_mots: liste des mots dans la phrase
    :return: liste de tuple pour le focus en position 0 et liste de tuple pour le focus en position n
    """
    liste_ngramav = []
    liste_ngramar = []

    for i in range(len(liste_mots) - (n-1)):
        groupeav = ()
        groupear = ()
        for j in range(n):
            groupeav += i+j,
            groupear += len(liste_mots) - (i + j) - 1,
        liste_ngramav.append(groupeav)
        liste_ngramar.append(groupear)

    return liste_ngramav, liste_ngramar


def Ngram(tupleav, tuplear, liste_mots):
    """
    Programme permettant de réaliser la sous séquence de taille n de la liste de mots donnée
    :param tupleav: liste contenant les indices des termes pour le focus en position 0
    :param tuplear: liste contenant les indices des termes pour le focus en position n
    :param liste_mots: Séquence sur laquelle il faut appliquer le N-Gram
    :return: Liste de tuple avec le focus en position 0 et liste de tuple avec le focus en position n
    """
    liste_motsav = []
    liste_motsar = []

    for tuple in tupleav:
        tuplemotsav = ()
        for i in tuple:
            tuplemotsav += liste_mots[i],
        liste_motsav.append(tuplemotsav)

    for tuple in tuplear:
        tuplemotsar = ()
        for i in tuple:
            tuplemotsar += liste_mots[i],
        liste_motsar.append(tuplemotsar)

    return liste_motsav, liste_motsar

# ---------------------------------------------------------------------------------------------------------------------
# Initialisation de la séquence sur laquelle réaliser le N-Gram
phrase = "La voie de la non-violence véritable exige beaucoup plus de courage que celle de la violence."
liste_mots = list(phrase.split())
# ---------------------------------------------------------------------------------------------------------------------
# Choix de la taille n du N-Gram
n = 0
while n <= 0:
    n = int(input("Choisissez la taille n du N-Gram : "))

# ---------------------------------------------------------------------------------------------------------------------
# N-Gram pour les indices avant [(0, 1, ..., n), (1, 2, ..., n), ... (n-k, n-k-1, ..., n)]
#                    et arrière [(n, n-1, ... n-k), (n-1, n-2, ... n-k), ... (n-k, ..., 1, 0)]
av , ar = tuple_Ngram(n, liste_mots)
# ---------------------------------------------------------------------------------------------------------------------
# N-Gram avec les mots de la séquence à partir des indices déterminées :
motsav, motsar = Ngram(av, ar, liste_mots)
# ---------------------------------------------------------------------------------------------------------------------

print(motsav)
print(motsar)
