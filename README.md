
## P1: Movie Trailer Website

"Server-side code" that stores a list of movies, including box art imagery and a movie trailer URL. 
Then from this list, static page will be generated allowing visitors to browse their movies and watch the trailers.

To execute type:

```
python media.py
```

With that, the file fresh_tomatoes.html will be generated, and it'll be opened in your browser.

#### Adding more movies

To add more movies, edit the file `media.py` creating a new entry in the format:

```python
my_movie = Movie(<title>, <trailer_url>, <poster_url)
```

Then add this new entry to the list at the end of the file.
For example:

```python
fresh_tomatoes.open_movies_page([civil_war, martian, my_movie])
```
