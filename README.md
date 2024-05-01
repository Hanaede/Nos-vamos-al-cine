# ¿Nos vamos al cine?

## Funcionamiento del programa
La idea es crear un programa que proporcione diferente tipo de información sobre películas. Para ello, se utilizará la API de [TMBD](https://www.themoviedb.org/documentation/api).

De momento, las opciones disponibles para consultar son:  
1. Buscar el código de una película según su nombre.
2. Buscar la siguiente información de una película proporcionando su código:
   - Título
   - Géneros
   - Argumento
   - Duración
   - Enlace a su web en IMDB
3. Películas recomendadas si te gusta una película concreta.
4. Obtener 5 películas "trending topic" semanal o del día en función del género de la misma. Además, se puede hacer por un género o por todos.
5. Mostrar géneros disponibles.

## Mejoras a futuro  
- Implementar más opciones en el menú, como por ejemplo:
  - Reviews
  - Videos
  - Series
  - Episodios de series
  - Actores/Actrices
  - Programación diaria de TV
  - ...
- Mejorar el código modularizando y mejorando la legibilidad.
- Controlar excepciones concretas.

 En definitiva, es un programa que puede escalar en número de opciones según las posibilidades de la API. Además, se pueden hacer versiones personalizadas para películas, series o TV.

 ## Fuentes

 ### Videos
- [Andy´s Tech Tutorials canal YT](https://www.youtube.com/watch?v=FlFyrOEz2S4&t=151s&ab_channel=Andy%27sTechTutorials)
- [Makes Sense canal YT](https://www.youtube.com/watch?v=vlenVDbJKsA&ab_channel=makessense)
- [How to make API calls to MovieDB](https://www.youtube.com/watch?v=WSvRFYPQyko&t=1057s&ab_channel=makessense)
- [How to set environment variables in Mac]([https://](https://www.youtube.com/watch?v=-cASjkF94dc&ab_channel=MacOSXTutorialsandAppreviewsfromHowTech))
- [Taller consumir API con Python - CodigoFacilito](https://www.youtube.com/watch?v=12NPmrdoKKs&t=4s&ab_channel=codigofacilito)

### API TMBD
 - [API TMBD](https://developer.themoviedb.org/reference/intro/getting-started)


### Webgrafía
 - [Apuntes Rafa del Castillo](https://github.com/rdelcastillo/DAW-Python/blob/master/notebooks/5.1%20Rest%20Api%20en%20Python.ipynb)
 - [Real Python](https://realpython.com/api-integration-in-python/)
 - [HTTP error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses)