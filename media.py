import fresh_tomatoes
from movie import Movie

civil_war = Movie("Captain America: Civil War", "https://youtube.com/watch?v=uVdV-lxRPFo", "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg")

martian = Movie("The Martian", "https://www.youtube.com/watch?v=Ue4PCI0NamI", "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg")
fresh_tomatoes.open_movies_page([civil_war, martian])
