# GeoSpacial_data_project

![geo](https://github.com/amorenorp/GeoSpacial_data_project/blob/main/img/geolocation-of-city-1024x683.jpg)


## Descripción : 
***
El objetivo de este proyecto es encontrar una localización para una empresa de Gaming.
La ubicación perfecta debe satisfacer los requisitos de los empleados. 
Vamos a intentar encontrar una localización que tenga cerca: 
- Stabucks
- Colegios
- Bares de copas
- Restaurantes veganos

Partimos de una base de datos que contiene la informacion de miles de empresas y su respectiva ubicación:  `companies.json` obtenido de https://data.crunchbase.com/docs. 


## Desarrollo:
***
Decidí ubicarme en Londres.
Haciendo uso de la `API` de `foursquare` busqué todos los Starbucks de Londres. 
Decidí utilizar de refenrencia el Starbucks situado en las coordenadas **(51.513 , -0.133)**. 
Con esas coordenadas utilicé el mismo proceso de llamas a la API de foursquare para encontrar los colegios, bares de copas y restaurantes veganos cerca. 

A su vez localicé los oficinas en un radio de 200m de esas coordenadas, utilizando `find` de `MongoDB`.

Ahora solo falta calcular a qué distancia tiene cada oficina cada requisito. 
Para ello `importamos : geopy.distance`.

Con esto llegamos a una conclusión sobre la localización perfecta para nuestra empresa de gaming. 

Encontrareís todo el proceso y el resultado final en el jupyter notebook `geo_spacial.ipynb`




### *Referencias y bibliotecas:*
***
- [https://docs.mongodb.com/manual/geospatial-queries/]

- [https://data.crunchbase.com/docs]

- [https://developer.foursquare.com/]

- [https://pypi.org/project/folium/0.1.5/]

- [https://github.com/CartoDB/cartoframes]
