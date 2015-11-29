
class Movie:
    """Represents a movie, containing relevant information, such as title,
       trailer url, etc"""
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
