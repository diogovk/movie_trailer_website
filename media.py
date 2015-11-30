import fresh_tomatoes
from movie import Movie

civil_war = Movie(
    "Captain America: Civil War", "2016",
    "https://youtube.com/watch?v=uVdV-lxRPFo",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",  # NOQA
    "Political interference in the Avenger's activities causes a rift between "
    "former allies Captain America and Iron Man.")

martian = Movie(
    "The Martian", "2015", "https://www.youtube.com/watch?v=Ue4PCI0NamI",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
    "During a manned mission to Mars, Astronaut Mark Watney is presumed dead "
    "after a fierce storm and left behind by his crew.")

kung_fury = Movie(
    "Kung Fury", "2015", "https://www.youtube.com/watch?v=72RqpItxd8M",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Kung_Fury_Poster.png",
    "In 1985, Kung Fury, the toughest martial artist cop in Miami, goes back "
    "in time to kill the worst criminal of all time - kung fuhrer Hitler.")

kingsman = Movie(
    "Kingsman: The Secret Service", "2014",
    "https://www.youtube.com/watch?v=y45q0lfEHfg",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",  # NOQA
    "A spy organization recruits an unrefined, but promising street kid into "
    "the agency's ultra-competitive training program, just as a global threat "
    "emerges from a twisted tech genius.")

ironman = Movie(
    "Iron Man", "2008", "https://www.youtube.com/watch?v=8hYlB38asDY",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "After being held captive in an Afghan cave, an industrialist creates a "
    "unique weaponized suit of armor to fight evil.")


def main():
    # Generate the page and open it in a browser window
    fresh_tomatoes.open_movies_page([
        civil_war, martian, kung_fury, kingsman, ironman
        ])

if __name__ == '__main__':
    main()
