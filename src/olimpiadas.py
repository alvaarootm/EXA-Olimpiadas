from typing import NamedTuple
from datetime import *
import csv
from collections import Counter, defaultdict
Medallas = NamedTuple('Medallas',
        [('oro',int),
         ('plata',int),
         ('bronce',int)]) 
Registro = NamedTuple('Registro', 
        [('ciudad_olimpica',str),
         ('fecha_inicio',date),
         ('pais',str),
         ('deporte',str),
         ('num_participantes',int),
         ('genero',str),
         ('medallas',Medallas),
         ('sede',bool)])  

#Ej 1

def parsea_medalla(medalla: str) -> Medallas:
    """Parsea una cadena en el formato 'oro:plata:bronce' a una tupla Medalla."""
    oro, plata, bronce = map(int, medalla.split(':'))
    return Medallas(oro, plata, bronce)

def parsea_bool(sede: str) -> bool:
    """Parsea una cadena 'True'/'False' a un booleano."""
    return sede.strip().lower() == 'true'

def lee_registros_olimpiadas(ruta: str) -> list[Registro]:
    """Lee un archivo CSV y lo convierte en una lista de tuplas de tipo Registro."""
    registros = []
    
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for Registro in lector:
            # Parseamos cada campo
            ciudad_olimpica = ciudad_olimpica['ciudad_olimpica']
            fecha_inicio = datetime.strptime(fecha_inicio['fecha_inicio'], '%Y-%m-%d').date()
            pais = pais['pais']
            deporte = deporte['deporte']
            num_participantes = int(num_participantes['num_participantes'])
            genero = genero['genero']
            medallas = parsea_medalla(medallas['medallas'])
            sede = parsea_bool(sede['sede'])
    registros.append(Registro)
    
    return registros

#Ej 2

def deportes_ambos_generos(registros: list[Registro], año: int) -> set[str]:
    """Devuelve un conjunto con los deportes en los que participaron tanto hombres como mujeres en un año dado."""
    deportes_hombres = set()
    deportes_mujeres = set()

    for registro in registros:
        if registro.fecha_inicio.year == año:
            if registro.genero == 'HOMBRE':
                deportes_hombres.add(registro.deporte)
            elif registro.genero == 'MUJER':
                deportes_mujeres.add(registro.deporte)

    return deportes_hombres, deportes_mujeres

#Ej 3

def deportes_mas_frecuentes(registros: list[Registro], n: int, genero: str) -> list[tuple[str, int]]:
    """Devuelve una lista de los n deportes más frecuentes para un género dado, con su frecuencia."""
    deportes = [registro.deporte for registro in registros if genero is None or registro.genero == genero]
    frecuencia_deportes = Counter(deportes)
    return frecuencia_deportes.most_common(n)

#Ej 4

def deporte_con_mas_paises_distintos_con_oro(registros: list[Registro], genero: str | None = None) -> str:
    """Devuelve el deporte con más países distintos que hayan ganado medallas de oro para un género dado."""
    deportes_paises = defaultdict(set)

    for registro in registros:
        if genero is None or registro.genero == genero:
            if registro.medallas.oro > 0:
                deportes_paises[registro.deporte].add(registro.pais)

    # Calculamos el deporte con más países distintos con medallas de oro
    return max(deportes_paises, key=lambda deporte: len(deportes_paises[deporte]))

#Ej 5

def deportes_mas_participantes_de_genero_por_juego(registros: list[Registro], pais: str, genero: str) -> dict[str, list[tuple[str, int]]]:
    """Devuelve un diccionario con los deportes con más participantes de un género y país por JJOO."""
    juegos = defaultdict(list)

    for registro in registros:
        if registro.pais == pais and registro.genero == genero:
            identificador_juegos = f"{registro.ciudad_olimpica}{str(registro.fecha_inicio.year)[-2:]}"
            juegos[identificador_juegos].append((registro.deporte, registro.num_participantes))

    # Ordenamos y filtramos los tres deportes con más participantes por cada JJOO
    resultado = {}
    for juego, deportes in juegos.items():
        deportes_ordenados = sorted(deportes, key=lambda x: x[1], reverse=True)[:3]
        resultado[juego] = deportes_ordenados

    return resultado

#Ej 6