from functools import reduce
import operator
import pandas as pd
import geopandas as gpd


def getFromDict(diccionario,mapa):
    return reduce (operator.getitem,mapa,diccionario)



def getlistdata(result, category_name):
    
    listdata = []

    for dic in result:
        dictdata = {}

        dictdata["name"]= getFromDict(dic, name)
        dictdata["latitud"]= getFromDict(dic, lat)
        dictdata["longitud"]= getFromDict(dic, long)
        dictdata["category"]= category_name
    
        listdata.append(dictdata)
        
    return listdata


def makegeomap(df):
    return  gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.longitud, df.latitud))


def contar(lista):
    cuenta = {
        "111pix": 0,
        "Team Rubber":0,
        "Undertone" :0,
        "muzu tv": 0
    }

    for name in lista: 
        if name == "111pix":
            cuenta[name] += 1
        elif name == "Team Rubber":
            cuenta[name] += 1
        elif name == "Undertone":
            cuenta[name] += 1
        else :
            cuenta[name] +=1
    
    return cuenta