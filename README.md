# REST-API-with-Django
Crawling movies data from IMDB website and using it with REST API.

Refer to this [Medium Blog](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c) on using Restful Framework with Django. 

# Crawling Data
In the 'movie' app there is data.py file which crawls data from this [url](https://www.imdb.com/chart/top?ref_=nv_mv_250) and stroes in a List Dictonary. 
With the REST Api I was able to generate the link of API.
The process of querying and converting tabular database values into JSON or another format is called serialization. When you’re creating an API, correct serialization of data is the major challenge.

The Users app does the basic task by using auth of django and displaying the serached movie on the basis of Rank, Movie Title, Rating and Year of Release. 
with :
```  pip install djangorestframework  ```
all the serializing task is handled by Restful.
View will import the serializers and ```ModelViewSet``` will handle all the Get and Post Request.
```  from rest_framework import serializers  ```
After setting the view and URLs accordinly with 
``` py manage.py runserver ``` the url takes to the Django Rest Framework Page

