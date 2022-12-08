import pandas as pd

# 

def readxslx(url, num):
    exel = pd.read_excel(url)
    
    lista=[]
    
    columnas = exel.columns


    columnas = columnas.tolist()
    columnas2 =columnas[num]
    val = exel[columnas2]


    for elemento in val:
        lista.append(elemento)
    return lista

