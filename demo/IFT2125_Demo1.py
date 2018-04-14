
# coding: utf-8

# # IFT 2125 - TP 1 - 12 janvier
# ## Stephanie Larocque

# In[1]:


import numpy as np #pour les operations mathematiques sur les matrices, par exemple

import matplotlib.pyplot as plt # graphiques


# ## Question 1
# 
# Implementer en python un algorithme pour calculer le plus petit commum multiple (ppcm) de deux nombres $a$ et $b$

# In[2]:


def pgcd(a,b): # Algorithme d'Euclide
    while b!= 0 :
        a, b = b, a%b
    return a

def ppcm(a,b): # Car a*b = ppcm(a,b)*pgcd(a,b) <---- on peut le voir grace a la decomposition en nombres premiers
    return a * b // pgcd(a, b)


# In[3]:


print(pgcd(24, 42))
print(ppcm(4, 14))


# ## Question 2
# 
# Declarer une liste, un tuple et un set contenant les elements 1,2,3,4 en python et enoncer les principales diﬀerences. Implementer une methode de tri d’une liste.
# 

# In[4]:


liste = [1,2,3,4] # ordonne, repetition possible, , muable
tup = (1, 2, 3, 4) # ordonne, repetition possible, immuable****
ensemble = {1,2,3,4} # pas ordonne, pas repetition, muable


# In[5]:


l1 = [1,2,2]
print("liste", l1)
e1 = {1,1,2}
print("set", e1, "supprime les elements repetes")


# In[6]:


#Une liste peut contenir nimporte quoi (pas uniquement des elements de meme type)
l2 = ["allo", 4, 1.5]
print(l2)


# In[7]:


#On peut ajouter des elements aux listes et aux ensembles, mais pas aux tuples (car immuables)
liste.append(5)
print(liste)
liste.append(1)
print(liste)
ensemble.add(5)
print(ensemble)
#tup.append(5) #<--- donne une erreur


# In[8]:


def insertion_sort(l):
    
    n = len(l) #taille d'une liste
    
    for i in range(n-1): #i = 0, 1, 2, ..., n-2 ### range(n) = range(0, n, 1), range(n, 0, -2)
        index_min = i
        for j in range(i+1, n):
            if l[j]<l[index_min]:
                index_min = j
        l[i], l[index_min] = l[index_min], l[i]
        print("Step", i," :", l)
    return l
    
    
    


# In[9]:


insertion_sort([10,3,1,4,5, 2])


# ## Question 3
# Implementer en Python un algorithme pour calculer naivement det(A):
# 
# $$ \det(A) = \sum_{j = 1}^m (-1)^{i+j}\ a_{ij}\ \det(A_{ij})$$

# In[10]:


def sub_matrix(A, i, j):
    #enlever ligne i (axis = 0 pour les lignes)
    A = np.delete(A, (i), axis = 0)
    #enelver colonne j (axis = 1 pour les colonnes)
    A = np.delete(A, (j), axis = 1)
    return A

def det(A):
    i = 0
    m = len(A)# nb de lignes dans la matrice A
    
    if m==1: # La recursion doit s'arreter
        return A[0,0]
    else:
        x = 0
        for j in range(m): 
            x +=( (-1)**(i+j) ) * A[i,j] * det(sub_matrix(A, i, j))
        return x
    
    


# In[11]:


A = np.array(   [[1,2,30],[4,5,6],[7,8,9]]  )
print("Determinant of ")
print( A, " is ", det(A))

print("Pour verifier, methode determinant de numpy donne : ", np.linalg.det(A))


# ## Questions des etudiants

# In[12]:


def f(a):
    return a, a + 1

print("f(4) : ", f(4))
print("f(4)[0] : ", f(4)[0] ,"<-- pour aller rechercher le premier element, 4")
y  = f(4)
print("y : ",f(4), "<-- un tuple contenant l'output de la fonction f")


# In[13]:


# Addition de tuples ou de listes = concatenation
tup = (1,2)
tup2 = (2,3)
tup+tup2

l1 = [1,2]
l2 = [2,3]
l1+l2


# In[14]:


# Addition d'array numpy = addition au sens mathematique
a = np.array([1,2])
a2 = np.array([2,3])
a3 = np.ones(2)
print(a3)
a+a2+a3


# In[15]:


A = np.array(   [[1,2,30, 1],[4,5,6, 1],[7,8,9,1]]  )
print(len(A)) # Nombre de lignes
print(len(A[0])) # Nombre de colonnes

