
class Movie(object):
    """A movie, containing information such as title, trailer url, etc

    Keyword Arguments:
        - title -- title of the movie

        - trailer_youtube_url -- youtube URL containing the trailer of movie

        - poster_image_url -- URL pointing to a poster of the movie
   """

    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
