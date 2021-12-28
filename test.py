BE=[["le club de football londonien est qualifié","sport"],
    ["le défenseur a marqué le dernier but","sport"],
    ["aucun club anglais n'a encaissé de but","sport"],
    ["le maroc a redressé son économie","économie"],
    ["la covid a touché l'économie marocaine","économie"],
    ["plusieurs entreprises sont en faillite","économie"],
    ["le gouvernement envisage un nouveau confinement","politique"],
    ["le parlement a validé la loi 36.30","politique"],
    ["le gouvernement est parvenu à un accord","politique"]]
BT=[["le gouvernement se rassemblera mardi",""],
    ["le défenseur français a renouvelé avec son club",""],
    ["les entreprises américaines ont suspendu leurs activités",""]]

#Création du VA
VA=[]
for i in range(len(BE)):
    for j in range(len(BE[i][0].split())):
        if not BE[i][0].split()[j] in VA:
            VA.append(BE[i][0].split()[j])

#Création de txt2num
def txt2num(t,VA):
    VN=[]
    T=t.split()
    for j in range(len(VA)):
        cmpt=0
        for i in range(len(T)):
            if T[i]==VA[j]:
                cmpt=cmpt+1
        VN.append(cmpt)    
    return VN

#Conversion en BEnum, BTnum
BEnum=[]
for i in range(len(BE)):
    BEnum.append([txt2num(BE[i][0],VA),BE[i][1]])
BTnum=[]
for i in range(len(BT)):
    BTnum.append([txt2num(BT[i][0],VA),BT[i][1]])

#Définition de euclidienne
from math import sqrt
def euclidienne(X,Y):
    d=0
    for i in range(len(X)):
        d=d+(X[i]-Y[i])**2        
    return sqrt(d)

#définition de KNN
def knn(k,t,B):
   #créer la table des distances t-B
    tD=[]
    for i in range(len(B)):
        tD.append([euclidienne(t,B[i][0]),B[i][1]])
   #trier la tD
    for i in range(len(tD)-1):
        for j in range(i):
            if tD[i][0]>tD[j][0]:
                temp=tD[i]
                tD[i]=tD[j]
                tD[j]=temp
    print(tD)
   #calculer les k premiers de la tD
    #créer les tables tC et tO
    tC=[]
    tO=[]
    for i in range(len(BEnum)):
        if not BEnum[i][1] in tC:
            tC.append(BEnum[i][1])
            tO.append(0)
    #remplir la table tO
    for i in range(k):
        for j in range(len(tC)):
            if tD[i][1]==tC[j]:
                tO[j]=tO[j]+1
    print(tO)
   #retourner la classe prédite
    indmax=tO.index(max(tO))
    return tC[indmax]
