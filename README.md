# REST-API-with-Django
Crawling movies data from IMDB website and using it with REST API.

Refer to this [Medium Blog](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c) on using Restful Framework with Django. 

# Crawling Data
In the 'movie' app there is data.py file which crawls data from this [url](https://www.imdb.com/chart/top?ref_=nv_mv_250) and stroes in a List Dictonary. 
With the REST Api I was able to generate the link of API along with the get and post request handling. 
The Restful 

The Users app does the basic task by using auth of django and displaying the serached movie on the basis of Rank, Movie Title, Rating and Year of Release. 

``` pip install djangorestframework ```
