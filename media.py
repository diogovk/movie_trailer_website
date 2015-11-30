import fresh_tomatoes
from movie import Movie

civil_war = Movie(
    "Captain America: Civil War", "2016", "https://youtube.com/watch?v=uVdV-lxRPFo",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg")

martian = Movie(
    "The Martian", "2015", "https://www.youtube.com/watch?v=Ue4PCI0NamI",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg")

kung_fury = Movie(
    "Kung Fury", "2015", "https://www.youtube.com/watch?v=72RqpItxd8M",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Kung_Fury_Poster.png")

kingsman = Movie(
    "Kingsman: The Secret Service", "2014", "https://www.youtube.com/watch?v=y45q0lfEHfg",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg")

ironman = Movie(
    "Iron Man", "2008", "https://www.youtube.com/watch?v=8hYlB38asDY",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG")

fresh_tomatoes.open_movies_page([
    civil_war, martian, kung_fury, kingsman, ironman
    ])
