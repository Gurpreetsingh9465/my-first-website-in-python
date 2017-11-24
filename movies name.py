import movie
import fresh_tomatoes
import website
logan = movie.Movie("LOGAN", "Hero with blades",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=RH3OxVFvTeg")
toystory = movie.Movie("Toy Story", "toys come alive",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=2s")
harrypotter = movie.Movie("Harry Potter", "cursed child",
                          "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
                          "https://www.youtube.com/watch?v=VyHV0BRtdxo")
manofsteel = movie.Movie("man of steel", "superman",
                         "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                         "https://www.youtube.com/watch?v=T6DJcgm3wNY")
avengers = movie.Movie("Avengers", "superheroes come together",
                       "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                       "https://www.youtube.com/watch?v=tmeOjFno6Do")
thor = movie.Movie("Thor-ragnarock", "thor's life in danger",
                   "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/c/ce/Thor-Ragnarok-Poster%282%29.jpg/revision/latest/scale-to-width-down/324?cb=20170410165955",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")
name = [logan, toystory, harrypotter, manofsteel, avengers, thor]
fresh_tomatoes.open_movies_page(name)