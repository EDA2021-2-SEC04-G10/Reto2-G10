"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artist': None,
           'artwork': None}

    catalog['artist'] = lt.newList('ARRAY_LIST')

    catalog['artwork'] = lt.newList('ARRAY_LIST')

  
    catalog['Medium'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None)
    return catalog
    

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    a = newArtist(artist['ConstituentID'],artist['DisplayName'],
                  artist['ArtistBio'],artist['Nationality'],
                  artist['Gender'],artist['BeginDate'],
                  artist['EndDate'],artist['Wiki QID'],
                  artist['ULAN'])
    lt.addLast(catalog['artist'], a)

def addArtwork(catalog, artwork):
    """
    Adiciona un artista a la lista de artistas
    """
    ar = newArtwork(artwork['ObjectID'],artwork['Title'],
                    artwork['ConstituentID'],artwork['Date'],
                    artwork['Medium'],artwork['Dimensions'],
                    artwork['CreditLine'],artwork['AccessionNumber'],
                    artwork['Classification'],artwork['Department'],
                    artwork['DateAcquired'],artwork['Cataloged'],
                    artwork['URL'],artwork['Circumference (cm)'],
                    artwork['Depth (cm)'],artwork['Diameter (cm)'],
                    artwork['Height (cm)'],artwork['Length (cm)'],
                    artwork['Weight (kg)'],artwork['Width (cm)'],
                    artwork['Seat Height (cm)'],artwork['Duration (sec.)'])
    lt.addLast(catalog['artwork'], ar)

# Funciones para creacion de datos

def newArtist(constituentID, displayName, artistBio, nationality, 
              gender, beginDate, endDate, wikiQID, ulan):
    """
    Esta estructura almancena los artistas.
    """
    artist = {'ConstituentID': '', 'DisplayName': '','ArtistBio': '',
           'Nationality': '', 'Gender': '', 'BeginDate': '', 'EndDate': '',
           'Wiki QID': '', 'ULAN': ''}
    artist['name'] = constituentID
    artist['DisplayName'] = displayName
    artist['ArtistBio'] = artistBio
    artist['Nationality'] = nationality
    artist['Gender'] = gender
    artist['BeginDate'] = beginDate
    artist['EndDate'] = endDate
    artist['Wiki QID'] = wikiQID
    artist['ULAN'] = ulan
    return artist
    
def newArtwork(objectID, title, constituentID, date, medium, dimensions, creditLine,
               accessionNumber, classification, department, dateAdquired, cataloged,
               url, circumference, depth, diameter, height, length, weight, width,
               seatHeight, duration):
    """
    Esta estructura almancena los artistas.
    """
    artwork = {'ObjectID': '', 'Title': '','ConstituentID': '',
           'Date': '', 'Medium': '', 'Dimensions': '', 'CreditLine': '',
           'AccessionNumber': '', 'Classification': '', 'Department': '', 
           'DateAcquired': '','Cataloged': '', 'URL': '', 'Circumference (cm)': '', 
           'Depth (cm)': '', 'Diameter (cm)': '', 'Height (cm)': '', 'Length (cm)': '',
           'Weight (kg)': '', 'Width (cm)': '', 'Seat Height (cm)': '', 'Duration (sec.)': ''}
    artwork['ObjectID'] = objectID
    artwork['Title'] = title
    artwork['ConstituentID'] = constituentID
    artwork['Date'] = date
    artwork['Medium'] = medium
    artwork['Dimensions'] = dimensions
    artwork['CreditLine'] = creditLine
    artwork['AccessionNumber'] = accessionNumber
    artwork['Classification'] = classification
    artwork['Department'] = department
    artwork['DateAcquired'] = dateAdquired
    artwork['Cataloged'] = cataloged
    artwork['URL'] = url
    artwork['Circumference (cm)'] = circumference
    artwork['Depth (cm)'] = depth
    artwork['Diameter (cm)'] = diameter
    artwork['Height (cm)'] = height
    artwork['Length (cm)'] = length
    artwork['Weight (kg)'] = weight
    artwork['Width (cm)'] = width
    artwork['Seat Height (cm)'] = seatHeight
    artwork['Duration (sec.)'] = duration
    
    return artwork

def newMedium(medio):

    medium = {'name': '',
           'total_artworks': 0,
           'artworks': None,
           'count': 0.0}
    medium['name'] = medio
    medium['artworks'] = lt.newList()
    return medium

def addMedium(catalog, medium):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo y se
    actualiza el indice de identificadores del tag.
    """
    newMedio = newMedium(medium['name'])
    mp.put(catalog['Medium'], medium['name'], newMedio)
    


# Funciones para creacion de datos

# Funciones de consulta

def getArtworkByMedium(catalog, name):
   
    medium = mp.get(catalog['Medium'], name)
    artworks = lt.newList()
    if medium:
        artworks = lt.newListaddLast(me.getValue(medium)['artworks'])
    return artworks

def nObrasTecnica(catalog, size, name):
    medium = mp.get(catalog['Medium'], name)
    artworks = lt.newList()
    if medium:
        artworks = lt.addLast(artworks, me.getValue(medium)['artworks'])
    f = sortArtworkByYear(artworks['Date'], len(artworks))
    for i in f:
        if i < size:
            g = lt.newList()
            lt.addLast(g, f[i])
    return g            

    



def getYear(catalog, artwork):
    obra = catalog['artwork'].get(artwork)
    year = obra.get('Date')

    return year


# Funciones utilizadas para comparar elementos dentro de una lista



def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) < int(year2)):
        return 1
    else:
        return 0


# Funciones de ordenamiento

def sortArtworkByYear(catalog, size):
    sub_list = lt.subList(catalog['artwork'], 1, size)
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list, compareYears)
    return sorted_list

