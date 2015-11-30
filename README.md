
## P1: Movie Trailer Website

"Server-side code" that stores a list of movies, including box art imagery and a movie trailer URL. 
Then from this list, a static page is generated allowing visitors to browse their movies and watch the trailers.

To execute type:

```
python media.py
```

With that, the file fresh_tomatoes.html will be generated, and it'll be opened in your browser.

#### Adding more movies

To add more movies, edit the file `media.py` creating a new entry in the format:

```python
my_movie = Movie(<title>, <year>, <trailer_url>, <poster_url>, <storyline>)
```

Then add this new entry to the list at the end of the file.
For example:

```python
fresh_tomatoes.open_movies_page([civil_war, martian, my_movie])
```

I got help from the following links:

http://stackoverflow.com/questions/19695784/how-can-i-make-bootstrap-columns-all-the-same-height (CSS element height)
http://imdb.com (Movies storylines and years)
http://wikipedia.com (Movies poster images)
https://github.com/adarsh0806/ud036_StarterCode (fresh_tomatoes)
