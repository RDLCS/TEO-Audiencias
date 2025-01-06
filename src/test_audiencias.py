from audiencias import*

def test_lee_audiencias(audiencias:List[audiencia],programa:str)->None:
    print(f"Audiencias del programa {programa}:")
    print(audiencias[:20])

def test_calcula_ediciones(audiencias:List[audiencia],programa)->None:
    print(f"Número de ediciones del programa {programa}: {calcula_ediciones(audiencias)}")

def test_filtra_por_ediciones(audiencias:List[audiencia],edicion:List[int],programa:str)->None:
    print(f"Audiencias de las ediciones {edicion} del programa {programa}:")
    print(filtra_por_ediciones(audiencias,edicion))

def test_media_por_ediciones(audiencias:List[audiencia],programa:str)->None:
    print(f"Media de audiencias por ediciones del programa {programa}:")
    print(medias_por_ediciones(audiencias))

def test_muestra_evolucion_audiencias(audiencias:List[audiencia],programa:str)->None:
    print(f'Evolución de audiencias del programa {programa}')
    muestra_evolucion_audiencias(audiencias,programa)

def test_muestra_media_por_ediciones(audiencias:List[audiencia],programa:str)->None:
    print(f"Media de las audiencias de {programa} por edición")
    muestra_media_por_ediciones(audiencias,programa)

if __name__=='__main__':
    audiencias_GH=lee_audiencias('data/GH.csv')
    audiencias_MC=lee_audiencias('data/MasterChef.csv')
    #test_lee_audiencias(audiencias_GH,'Gran Hermano')
    #test_lee_audiencias(audiencias_MC,'Master Chef')
    #test_calcula_ediciones(audiencias_GH,'Gran Hermano')
    #test_calcula_ediciones(audiencias_MC,'Master Chef')
    #test_filtra_por_ediciones(audiencias_GH,[1,2,3],'Gran Hermano')
    #test_filtra_por_ediciones(audiencias_MC,[4,5],'Master Chef')
    #test_media_por_ediciones(audiencias_GH,'Gran Hermano')
    #test_media_por_ediciones(audiencias_MC,'Master Chef')
    #test_muestra_evolucion_audiencias(audiencias_GH,'Gran Hermano')
    #test_muestra_evolucion_audiencias(audiencias_MC,'Master Chef')
    test_muestra_media_por_ediciones(audiencias_GH,'Gran Hermano')
    test_muestra_media_por_ediciones(audiencias_MC,'Master Chef')