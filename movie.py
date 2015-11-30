
class Movie(object):
    """A movie, containing information such as title, trailer url, etc

    Keyword Arguments:
        - title -- title of the movie

        - trailer_youtube_url -- youtube URL containing the trailer of movie

        - poster_image_url -- URL pointing to a poster of the movie

        - year -- Year of release

        - storyline -- Short plot of the movie
   """

    def __init__(self, title, year, trailer_youtube_url, poster_image_url, storyline):
        self.title = title
        self.year = year
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.storyline = storyline
