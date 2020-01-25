from random import *

# liste des créneaux
l = 'lundi'
m = 'mercredi'
j = 'jeudi'
v = 'vendredi'
Maths= [['SH1',15.30,16.30,l],['SH2',16.30,17.30,l],['AR1',15.30,16.30,l],['AR2',16.30,17.30,l],['MM1',15.30,16.30,m],['TS1',13.30,14.30,m],['TS2',14.30,15.30,m], ['LC1',17.30,18.30,j],['IC1',15.30,16.30,l],['LS1',16.30,17.30,l],['OK1',9.30,10.30,v],['ADF1',15.30,16.30,l],['ADF2',16.30,17.30,l], ['LGL',15.30,16.30,l],['LGJ',17.30,18.30,j],['BZ1',16.30,17.30,m],['FD1',13.30,14.30,m],['FD2',14.30,15.30,m]]
Phys = [['GA1',15.30,16.30,l],['SCTL',15.30,16.30,l],['SCTJ',15.30,16.30,j],['JCP1',15.30,16.30,m],['JCP2',16.30,17.30,m],['JCP3',17.30,18.30,m],['HCL',16.30,17.30,l],['HCM',16.30,17.30,m]]
Al = [['JK',15.30,16.30,l]]
Angl = [['ML1',16.30,17.30,m],['ML2',17.30,18.30,m],['AG1',13.30,14.30,m],['AG2',14.30,15.30,m],['AG3',16.30,17.30,m],['AG4',17.30,18.30,m],['Mn1',16.30,17.30,m],['Mn2',17.30,18.30,m]]

L= [i for i in range (15)] # listes des exceptions pour chaque créneau de chaque groupe
Ex = [[0,0,0,0] for i in range (15)]
Ex[2] = [0,15.30,16.30,l]

M = Maths[:] # sauvegarde des listes
P = Phys[:]
A = Al[:]
Ag = Angl[:]
l1 = L[:7] # division des deux groupes (Physique et anglais)
l2 = L[8:]

    # attribution des créneaux
# Procédure d'affectation alétoire
def affectation (l1,l2,M,P,A,Ag):
    R,E,S = [],[],[]
    r1,r2 = [],[] # liste des affectations
    j = int(input("Veuillez entrer 1 si la semaine est paire, et 0 sinon")) # possibilité de récupérer la date ? sinon: 1 => r1 a Physique
    for gr in range (15):
        I = impossibilité (gr,M,P,Ag)
        if I == []:
            S.append (gr) #groupes simples
        else:
            E.append([gr,I]) # on récupère les groupes ayant des indisponibilités pour les traiter en premier
    EMaths = [] #exceptions pour les groupes à indisponibilités pour les créneaux de maths
    for i in E:
        if i[2] != []:
            EMaths.append(i[1],i[2])
    n = len(M)
    for groupe in EMaths:
        cre = randrange (n) # attribution des créneaux de maths
        Cre = M[cre] #exceptions traitees en premier
        while Cre in groupe[1]:
            cre = randrange(n)
            Cre = M[cre]
        n -= 1
        R[groupe[0]] = [Cre] # on fait une liste pour y ajouter les heures des autres matières
    for gr in S: # créneaux simples
        cre = randrange (n)
        Cre = M[cre]
        n -= 1
        R[groupe[gr]] = [Cre]
        # il faut encore créer les modules de physique et d anglais
        return (R)
    

# Procédure de gestion des exceptions
def impossibilité (gr, M, P, Ag): # gr est le numéro du groupe
    global Ex
    L = Ex[gr]
    print(L)
    R = []
    print (R)
    for i in range(len(M)): # ajout des codes des créneaux indisponibles pour chaque matière
        j = []
        if M[i][3] == L[3]: # égalité du jour
            if M[i][1] > L[1]: # impossibilité des heures
                j.append (M[i][0]) # trop tot
            if M[i][2] > L[2]:
                j.append(M[i][0]) # trop tard
    R.append (j)
    print (R)
    for i in range(len(P)):
        j = []
        if P[i][3] == L[3]:
            if (P[i][1]) > L[1] or (P[i][2] < L[2]):
                j.append (P[i][0])
    R.append (j)
    print (R)
    j = []
    for i in range(len(Ag)):
        if Ag[i][3] == L[3]:
            if (Ag[i][1] > L[1]) or (Ag[i][2] > L[2]):
                j.append (Ag[i][0])
    R.append (j)
    return (R) #liste R structure : [[crénaeaux maths : ['code des horaires']],[créneaux physique],[créneaux anglais]]

# création graphique des horaires
'print(affectation (l1,l2,M,P,A,Ag))'
print (impossibilité (2,M,P,Ag))


# Interface utilisateur
