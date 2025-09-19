import random
import math
import numpy as np
from copy import deepcopy

costRowChange=10
distanceWeight=4
disp=[
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,-1,-1,0,0]
] #0 posto utilizzabile, -1 posto vuoto o inesistente.

cognomi = [
    "BERTAINA", "BERTOLOTTI", "BONACCORSO", "BRERO", "BRUNO", "CAPOFERRI" ,"DARBESIO", "EL FOURATI", "EL JABER", "FISSOLO",
    "FRACCHIA", "GARELLO", "GENOVESE", "IZZA", "KACMOLI", "LAPALORCIA", "LERDA", "PANI", "PERANO", "PIRRA",
    "STEFFENINO", "TARICCO"
]


def fromLinetoDisp(postiOraLine):
    postiOraDisp = deepcopy(disp)
    negOneCount=0
    for x in range(len(disp)):
        for y in range(len(disp[0])):
            if disp[x][y]>-1:
                postiOraDisp[x][y]=postiOraLine[y+x*(len(disp[0]))-negOneCount]
            else:
                negOneCount+=1
    return postiOraDisp









def dist(x,y,x1,y1):
    return distanceWeight*math.sqrt((x-x1)**2+(y-y1)**2)+ costRowChange*abs(x1-x)






def calcProb(ArrayOne,x,y):
    for x1 in range(len(disp)):
        for y1 in range(len(disp[0])):
            if (disp[x1][y1] > -1):
                ArrayOne[x1][y1]=dist(x,y,x1,y1)





def determinPlace(ArrayP,x,y,newPosti):
    remain=[]
    for i in range(len(cognomi)):
        if cognomi[i] not in newPosti:
            remain.append(cognomi[i])
    #print(remain)
    #print(newPosti)
    s=0
    probs=[]
    for i in range(len(remain)):

        probs.append(i)
        #print(probs)
    for i in range(len(remain)):
        probs[i]=round(ArrayP[i][x][y]*10)
        s+=probs[i]
            #print(s)
    #print(probs)


    if s==0:
        return remain[0]
    num=random.randint(1,s)
    #print(num)
    count=0
    for i in range(len(remain)):
        if num<=probs[i]:
            return remain[i]
        else:
            num-=probs[i]







def creaPosti(postiOra):
    ArrayP = [deepcopy(disp) for _ in cognomi]  # array che contiene matrici con le probabilità di ogni cognome

    for i in range(len(cognomi)):
        x,y=getIndex(postiOra,i)
        calcProb(ArrayP[i],x,y)
        #print(ArrayP[i])




    newPosti=[]
    for x in range(len(disp)):
        for y in range(len(disp[0])):
            if disp[x][y]>-1:
                newPosti.append(determinPlace(ArrayP, x, y, newPosti))
    newPostin=[cognomi.index(item) for item in newPosti]
    return(newPostin)

def negOneCounter(t):
    ar=[i for j in disp for i in j]
    s=0
    for k in range(t):
        if ar[k]==-1:
            s+=1
    if(ar[t])==-1:
        for k in range(t,len(ar)):
            if (ar[k]==-1):
                s+=1
    return s


def getIndex(dispAr, i):
    t = dispAr.index(i)
    #print("t" +str(t))
    row = t // len(disp[0])

    offset = negOneCounter(t)
    #print(offset)
    col = t - row * len(disp[0]) + offset
    #print("col "+str(col))
    col = min(col, len(disp[0]) - 1)
    return row, col


def checkDouble(vecPosti,postiOra):
    #print(fromLinetoDisp(vecPosti))
    for item in range(len(cognomi)):
        #print(item)
        xo, yo = getIndex((vecPosti), item)
        xn, yn = getIndex((postiOra), item)
        #print("xo,yo="+str(xo)+","+str(yo)+",xn,yn="+str(xn)+","+str(yn))
        if (yo % 2 == 0)and (fromLinetoDisp(vecPosti)[xo][yo]!=-1):
            oldComp = fromLinetoDisp(vecPosti)[xo][ yo + 1]
            if(yn%2==0):
                newComp = fromLinetoDisp(postiOra)[xn][ yn + 1]
            else:
                newComp = fromLinetoDisp(postiOra)[xn][yn - 1]

            if oldComp == newComp:
                #print(item)
                return 1


def generaPosti(postiOra1):
    postiOra=[cognomi.index(i) for i in postiOra1]
    #print(postiOra)
    vecPosti=deepcopy(postiOra)
    postiOra = creaPosti(postiOra)
    #print(vecPosti)
    #print(postiOra)
    #print(fromDisptoNameDisp(postiOra))
    while checkDouble(vecPosti,postiOra):
        postiOra=creaPosti(deepcopy(vecPosti))
        #print(fromLinetoDisp(postiOra))
    #print(postiOra)
    return [cognomi[i] for i in postiOra]

def fromDisptoNameDisp(dispIn):
    disp1=fromLinetoDisp(deepcopy(dispIn))
    namedisp=deepcopy(disp1)
    for x in range(len(disp)):
        for y in range(len(disp[0])):
            if disp[x][y]>-1:
                namedisp[x][y]=cognomi[disp1[x][y]]

                
    return namedisp

#fine codice 

def checkForDoubles(posti):
    k=0
    doubles=[]
    for i in range(len(posti)):
        j=i+1
        while(j<len(posti)):
            if(posti[i]==posti[j]):
                doubles.append([i,j])
                k=1
            j+=1
    if k==1:
        for item in doubles:
            posti[item[0]]='error'
            posti[item[1]]='error'
    return k

def transform(posti):
    k=checkForDoubles(posti)
    print(k)
    for i in range(len(posti)):
        if posti[i] not in cognomi:
            posti[i]='error'
            k=1
    return posti,k