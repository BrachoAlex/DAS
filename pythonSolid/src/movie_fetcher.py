import requests
import re
import csv
from bs4 import BeautifulSoup

# I have split the main function into two new classes, MovieScraper and MovieProcessor, in order to adhere to the Single
# Responsibility Principle (SRP). The MovieScraper class is now responsible for retrieving the movie data from the
# website, while the MovieProcessor class is responsible for processing the data and writing it into a file.
# The Open/Closed Principle (OCP) is also taken into consideration in the new code by  how it is separated and
# how variables and processes are handled. This means that new methods or classes can be implemented without worrying
# too much about modifying existing ones. For example, retrieving the data from another website: We can create a new
# class that implements the same "MovieScrapper" interface and plug it into the main function without any problem.
# I divided the code in a way we don't need subclasses, so the Liskov Substitution Principle (LSP) does not apply, but
# we could create a "movie" class that encapsulates the attributes of a movie and modify the MovieScraper class to
# return a list of "movie" objects instead, if necessary. However, I believe that this would be excessive for the
# problem we are trying to solve.
# The ISP (interface segregation principle) is not so explicit in the code, but the "MovieScrapper" class and the
# "MovieExporter" class are well-defined and narrow interfaces that follow the SRP.
# In the Class "MovieScraper" we can see a clear example of the code following the Dependency Inversion Principle (DIP)
# by how it depends on the requests module and the BeautifulSoup library, but it uses them through abstractions like
# the requests.get() and BeautifulSoup.select() methods, respectively. This makes it easy to change the implementation
# of these dependencies in the future if needed.

class MovieScraper:
    def __init__(self, url):
        self.url = url

    def get_movies_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')

        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

        movie_data = []
        for index in range(0, len(movies)):
            # Separating movie into: 'place',
            # 'title', 'year'
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = {"movie_title": movie_title,
                    "year": year,
                    "place": place,
                    "star_cast": crew[index],
                    "rating": ratings[index],
                    "vote": votes[index],
                    "link": links[index],
                    "preference_key": index % 4 + 1}
            movie_data.append(data)
        return movie_data


class MovieProcessor:
    def __init__(self, movie_data):
        self.movie_data = movie_data

    def process_data(self):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in self.movie_data:
                writer.writerow({**movie})


def main():
    scraper = MovieScraper('http://www.imdb.com/chart/top')
    movie_data = scraper.get_movies_data()

    processor = MovieProcessor(movie_data)
    processor.process_data()


if __name__ == '__main__':
    main()

