def naive_search(text, pattern, case_sensitive = True):
    """
    Implémentation de la recherche naïve d'un motif 'pattern' dans le texte 'text'.
    Retourne la liste des indices des occurrences trouvées
    """
    t = len(text)    # Longueur du texte
    p = len(pattern) # Longueur du motif
    if t == 0 or p == 0 or p>t:# Si le texte ou le motif est vide ou +grand que le texte -> liste vide
        return []
    results = []
    for i in range(t-p+1): #i indice sur le texte
        j = 0 #indice sur le motif
        if case_sensitive:
            while (j<p and text[i+j]==pattern[j]):
                j+=1
        else:
            while (j<p and text[i+j].upper()==pattern[j].upper()):
                j+=1
        if j==p: # trouvé
            results.append(i)
    return results

def shift(m, case_sensitive=True):
    S = {}  # On initialise un dictionnaire vide
    
    # On parcourt le motif (sauf le dernier caractère)
    for k, letter in enumerate(m[:-1]):
        if case_sensitive:
            S[letter] = (len(m) - 1) - k  # On ajoute ou met à jour la valeur pour le caractère
        else:
            S[letter.upper()] = (len(m) - 1) - k  # On ajoute ou met à jour la valeur pour le caractère
    return S

def search(text, pattern, case_sensitive=True):
    t = len(text)    # Longueur du texte
    p = len(pattern) # Longueur du motif
    if t == 0 or p == 0 or p>t:# Si le texte ou le motif est vide ou +grand que le texte -> liste vide
        return []
    # Construction de la table de décalage
    jumps = shift(pattern, case_sensitive=case_sensitive)
    i = 0
    results = []
    while i <= t-p: # tant qu'on n'est pas à la fin du texte
        j = p - 1 # on se place au dernier caractère du motif
        if case_sensitive:
            while j >= 0 and text[i + j] == pattern[j]:# On recule dans le motif tant que les caractères correspondent
                j -= 1
        else:
            while j >= 0 and text[i + j].upper() == pattern[j].upper():# On recule dans le motif tant que les caractères correspondent
                j -= 1
        if j == -1: # occurence trouvée
            results.append(i)
            i+=1
        else:
            if case_sensitive:
                hops = jumps.get(text[i+j], p) # on récupère le décalage
            else:
                hops = jumps.get(text[i+j].upper(), p) # on récupère le décalage
            decalages_effectues = (p-1)-j
            decalage_effectif = hops - decalages_effectues
            if decalage_effectif < 0: # cas foireux, on décale de 1...
                decalage_effectif = 1
            i+=decalage_effectif
    return results