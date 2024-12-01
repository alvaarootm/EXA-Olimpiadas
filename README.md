# Fundamentos de Programación
# Curso 23-24. Primer parcial. 

**Autor:**  José Riquelme

**Revisores:**  José María Luna, Beatriz Pontes, Toñi Reina, Alfonso Bengoa

Disponemos de un fichero CSV, llamado `olimpiadas.csv` con información de participaciones de países por deportes y género en los juegos olímpicos (JJOO), cuyas líneas son de esta forma:

```
Ciudad Olímpica,Fecha de Inauguración,País,Deporte,Número de Participantes,Género,Oro,Plata,Bronce,Sede
Seúl,1988-09-17,ALEMANIA,tiro,12,MUJER,0-2-1,NO
Barcelona,1992-07-25,HOLANDA,hípica,6,MUJER,3-0-1,NO
Tokio,1964-10-10,HOLANDA,boxeo,13,HOMBRE,3-0-0,NO
Los Ángeles,1984-07-28,HOLANDA,esgrima,9,MUJER,2-1-3,NO
Sydney,2000-09-15,FRANCIA,atletismo,4,MUJER,0-0-0,NO
Rio de Janeiro,2016-08-05,HOLANDA,tiro,16,HOMBRE,0-2-3,SI
```
La segunda línea de los datos mostrada arriba indica que, en los JJOO celebrados en Seúl, ALEMANIA participó en el deporte tiro con 12 participantes del género mujer. La primera competición para este deporte fue el 24 de septiembre de 1988. ALEMANIA obtuvo 0 medallas de oro, 2 medallas de plata y una medalla de bronce en el deporte tiro para el género mujer. Finalmente, no todas las competiciones se celebraron en la sede principal.

Cree una carpeta **src** para incluir los siguientes módulos Python:

- **olimpiadas.py** en el que deberá implementar las funciones de los ejercicios que se indican a continuación.

- **olimpiadas_test.py** en el que deberá incluir una función de prueba, con sus correspondientes parámetros, por cada función solicitada en el módulo `olimpiadas`.

### NamedTuples
En el proyecto debe usar **obligatoriamente** los siguientes tipos, que representan los datos de las medallas y del registro de la participación, respectivament:

```python
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
```
con el siguiente significado:

- **ciudad olimpica**: sede principal en la que se disputaron los JJOO, y que da nombre a los juegos. 
- **fecha inicio**: fecha en la que comenzó la competición del deporte al que hace referencia la fila del csv. 
- **pais**: país para el que se recogen los participantes y las medallas. 
- **deporte**: deporte para el que se recogen los participantes y las medallas. 
- **num_participantes**: número de participantes del país, deporte y género dados. 
- **genero**: género de los participantes. Puede ser HOMBRE o MUJER. 
- **medallas**: número de medallas de oro, plata y bronce para el país, deporte y género dados. 
- **sede**: contiene el valor SI si la competición para el deporte, país y género dados tuvo lugar en la sede principal, y NO si hubo alguna competición que se celebró en una ciudad distinta a la sede principal. 


### Ejercicio 1 (1 punto)
Defina una función ``lee_registros_olimpiadas`` que dados el nombre y ruta de un archivo csv (filename), devuelva una lista de tuplas de tipo `Registro` con los datos leídos del archivo. Defina las funciones auxiliares de
parseo que crea convenientes. Le puede ser de ayuda la función `datetime.strptime(fecha_str,'%Y-%m-%d')`  para el parseo de fechas. 

```python
def lee_registros_olimpiadas(ruta:str)->list[Registro]
```

Resultados esperados en el test:
```
Registros leídos: 199
Los dos primeros: [Registro(ciudad_olimpica='Seúl', fecha_inicio=datetime.date(1988, 9, 17), pais='ALEMANIA', deporte='tiro', num_participantes=12, genero='MUJER', medallas=Medalla(oro=0, plata=2, bronce=1), sede=False), Registro(ciudad_olimpica='Barcelona', fecha_inicio=datetime.date(1992, 7, 25), pais='HOLANDA', deporte='hípica', num_participantes=6, genero='MUJER', medallas=Medalla(oro=3, plata=0, bronce=1), sede=False)]

Los dos últimos: [Registro(ciudad_olimpica='Sydney', fecha_inicio=datetime.date(2000, 9, 15), pais='HOLANDA', deporte='atletismo', num_participantes=15, genero='HOMBRE', medallas=Medalla(oro=1, plata=1, bronce=0), sede=False), Registro(ciudad_olimpica='Barcelona', fecha_inicio=datetime.date(1992, 7, 25), pais='ALEMANIA', deporte='atletismo', num_participantes=8, genero='MUJER', medallas=Medalla(oro=0, plata=3, bronce=1), sede=False)]
```

### Ejercicio 2 (1 punto)
Defina una función `deporte_ambos_generos` que dadas una lista de tuplas de tipo `Registro` y el año de celebración de los JJOO, devuelva un conjunto con los deportes de la edición de los JJOO celebrada en ese año en los que participaron tanto hombres como mujeres.

```python
def deportes_ambos_generos(registros: list[Registro], año:int )->set[str]
``` 

Resultados esperados en el test:
```
Los deportes con participación de ambos géneros en el año 1984 son: {'vela', 'ciclismo', 'hípica', 'gimnasia', 'boxeo', 'remo', 'esgrima', 'halterofilia'}
Los deportes con participación de ambos géneros en el año 1992 son: {'tiro', 'esgrima', 'remo'}
Los deportes con participación de ambos géneros en el año 1988 son: {'atletismo', 'ciclismo', 'tiro', 'gimnasia', 'boxeo', 'esgrima', 'halterofilia', 'judo'}
```
### Ejercicio 3 (1 punto)
Defina una función ``deportes_mas_frecuentes`` que dadas una lista de tuplas de tipo `Registro`, un número entero `n` y un género, devuelva una lista de tuplas con el nombre y la frecuencia con los **n** deportes más frecuentes para el género dado. La lista deberá estar ordenada de mayor a menor frecuencia. Si el género es `None` se tiene en cuenta cualquier género.

```python
def deportes_mas_frecuentes(registros: list[Registro],n:int,genero:str)->list[tuple[str,int]]
``` 

Resultados esperados en el test
```
Los 4 deportes más frecuentes para el género HOMBRE son:
        [('esgrima', 11), ('tiro', 10), ('remo', 10), ('boxeo', 9)]
Los 5 deportes más frecuentes para el género MUJER son:
        [('tiro', 11), ('ciclismo', 11), ('halterofilia', 10), ('hípica', 9), ('esgrima', 9)]
```
### Ejercicio 4 (1.5 puntos)
Defina una función `deporte_con_mas_paises_distintos_con_oro` que dada una lista de tuplas de tipo `Registro` y un género, que puede tomar el valor `None`,  devuelva el deporte practicado por el género dado como parámetro en el que hay más países distintos que hayan ganado una medalla de oro. Si el género dado es `None`, no se tendrá en cuenta el género.

```python
def deporte_femenino_con_mas_paises_distintos_con_oro(registros: list[Registro], genero:str|None=None)-> str
```

Resultados esperados en el test:
```
El deporte para el género None en el que hay más países distintos con medallas de oro es: esgrima
El deporte para el género HOMBRE en el que hay más países distintos con medallas de oro es: tiro
El deporte para el género MUJER en el que hay más países distintos con medallas de oro es: esgrima 
```
### Ejercicio 5 (1.5 puntos)
Defina una función `deportes_mas_participantes_de_genero_por_juego` que dada una lista de tuplas de tipo `Registro`, un país y un género, un diccionario en el que las claves son los identificadores de los JJOO, y los valores son listas de tuplas (deporte, número de participantes) del país y género dados. La lista de los valores debe estar ordenada de más a menos participantes y solo debe tener los datos de los 3 deportes con más participantes (si los hay). El **identificador** de los juegos se forma con la ciudad olímpica seguida de los dos últimos dígitos del año de celebración de los juegos.


```python
def deportes_mas_participantes_de_genero_por_juego(registros: list[Registro],pais:str, genero:str) -> dict[str, list[str]]
``` 

Resultados esperados en el test:
```
Los 3 deportes con más participantes del género MUJER para el país ESPAÑA en cada uno de los juegos son:
        0-('Seúl88', [('ciclismo', 14), ('boxeo', 9), ('atletismo', 5)])
        1-('Tokio64', [('esgrima', 17), ('hípica', 10), ('vela', 4)])
        2-('Rio de Janeiro16', [('esgrima', 16), ('tiro', 5)])
        3-('Sydney00', [('hípica', 12), ('boxeo', 11), ('halterofilia', 7)])
        4-('Los Ángeles84', [('atletismo', 16), ('remo', 16), ('boxeo', 15)])
        5-('Barcelona92', [('atletismo', 15), ('boxeo', 6)])
Los 3 deportes con más participantes del género HOMBRE para el país ESPAÑA en cada uno de los juegos son:
        0-('Rio de Janeiro16', [('tiro', 17), ('ciclismo', 16), ('atletismo', 16)])
        1-('Sydney00', [('atletismo', 13)])
        2-('Barcelona92', [('tiro', 9)])
        3-('Seúl88', [('boxeo', 17)])
        4-('Tokio64', [('remo', 19), ('judo', 11), ('hípica', 11)])
        5-('Los Ángeles84', [('judo', 18)])
Los 3 deportes con más participantes del género MUJER para el país PORTUGAL en cada uno de los juegos son:
        0-('Los Ángeles84', [('halterofilia', 18), ('esgrima', 13)])
        1-('Barcelona92', [('halterofilia', 17), ('judo', 16), ('tiro', 14)])
        2-('Tokio64', [('remo', 17), ('esgrima', 9), ('tiro', 4)])
        3-('Sydney00', [('judo', 20), ('boxeo', 5)])
        4-('Seúl88', [('tiro', 17), ('atletismo', 12)])
Los 3 deportes con más participantes del género HOMBRE para el país PORTUGAL en cada uno de los juegos son:
        0-('Sydney00', [('remo', 20), ('judo', 14), ('boxeo', 8)])
        1-('Seúl88', [('tiro', 19), ('vela', 14), ('ciclismo', 13)])
        2-('Rio de Janeiro16', [('atletismo', 13), ('vela', 7)])
        3-('Los Ángeles84', [('remo', 17), ('hípica', 10), ('vela', 4)])
        4-('Barcelona92', [('gimnasia', 9), ('esgrima', 8)])
        5-('Tokio64', [('halterofilia', 19)])

```
### Ejercicio 6 (2 puntos)
Defina una función `deporte_con_todos_los_paises` que dada una lista de tuplas de tipo `Registro`, devuelva `True` si hay algún deporte en el que hayan participado todos los países, o `False` en caso contrario.

```python
def deporte_con_todos_los_paises(registros: list[Registro]) ->  bool
``` 

Resultados esperados en el test:
```
¿Hay algún deporte en el que hayan participado todos los países? True
```
### Ejercicio 7 (2 puntos)
Defina una función `anyo_con_mayor_incremento_participantes_de_pais` que dada una lista de tuplas de tipo `Registro` y un país, devuelva una tupla con el incremento y el año en el que mayor incremento de participantes (contando hombre y mujeres de cualquier deporte) se ha producido con respecto al año de celebración anterior.

```python
def anyo_con_mayor_incremento_participantes_de_pais(registros: list[Registro],pais: str) -> tuple[int, int] 
``` 

Resultados esperados en el test:
```
El año de la edición de los juegos olímpicos que ha tenido un mayor incremento de participantes para el pais ESPAÑA es 2016 con un incremento de 57
El año de la edición de los juegos olímpicos que ha tenido un mayor incremento de participantes para el pais PORTUGAL es 1988 con un incremento de 24
```