from bs4 import BeautifulSoup
import requests
import re
from .models import Movie
# Download IMDB's Top 250 data
def data_fetch():

    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    imdb = []

    # Store each item into dictionary (data), then put those into a list (imdb)
    for index in range(0, len(movies)):
        # Seperate movie into: 'place', 'title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index))-(len(movie))]
        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index]}
        imdb.append(data)


    for item in imdb:
    
        Movie.objects.create(movie_title=item["movie_title"], year=item["year"],  place=item["place"], star_cast=item["star_cast"], rating=item["rating"])
    