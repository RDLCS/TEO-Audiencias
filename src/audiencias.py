from typing import NamedTuple,Tuple,DefaultDict,Dict,List,Set,Optional
import csv
from matplotlib import pyplot as plt

audiencia=NamedTuple('audiencia',[('edicion',int),('share',float)])

def lee_audiencias(ruta:str)->List[audiencia]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f)
        for edicion,share in iter:
            edicion=int(edicion)
            share=parseo_share(share)
            lista.append(audiencia(edicion,share))
    return lista

def parseo_share(porcentaje:str)->float:
    porcentaje=porcentaje.strip(' ')
    if '0' not in porcentaje:
        cero='0'+porcentaje
    else:
        cero=porcentaje
    return float(cero)

def calcula_ediciones(audiencias:List[audiencia])->int:
    conj=set()
    for a in audiencias:
        conj.add(a.edicion)
    return len(conj)

def filtra_por_ediciones(audiencias:List[audiencia],edicion:List[int])->List[audiencia]:
    lista=list()
    for a in audiencias:
        if a.edicion in edicion:
            lista.append(a)
    return lista

def medias_por_ediciones(audiencias:List[audiencia])->Dict[int,float]:
    dicc=dict()
    for a in audiencias:
        if a.edicion not in dicc:
            dicc[a.edicion]=list()
        dicc[a.edicion].append(a.share)
    for c,v in dicc.items():
        media=sum(v)/len(v)
        dicc[c]=media
    return dicc

def muestra_evolucion_audiencias(audiencias:List[audiencia],programa:str)->plt:
    shares=list()
    for a in audiencias:
        shares.append(a.share)
    plt.title(f"Evolución de audiencias del programa {programa}")
    plt.plot(shares,label='audiencia')
    plt.legend()
    plt.show()

def muestra_media_por_ediciones(audiencias:List[audiencia],programa:str)->plt:
    dicc=medias_por_ediciones(audiencias)
    ediciones=sorted(dicc.keys())
    medias=list()
    for e in ediciones:
        medias.append(dicc[e])
    plt.title(f"Medias de shares por edición del programa {programa}")
    plt.xlabel('ediciones')
    plt.ylabel('media')

    plt.bar(ediciones,medias)
    plt.xticks(ediciones,ediciones,fontsize=8)
    plt.show()