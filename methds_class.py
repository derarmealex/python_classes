class Movies:
    """
    film library
    ...
    Attributes
    ----------
    name: str
        title of the movie
    year: int
        release year
    colour: str
        colour or black and white
    director: str
        director's name
    main_actor: str
        main actor's name
    main_actor2: str
        main actor's name
    main_actor3: str
        main actor's name
    ...
    Methods
    -------
    func():
        output referential info about the movie
    """
#    name = None
#    year = 0
#    colour = None
#    director = None
#    main_actor = None
#    main_actor2 = None
#    main_actor3 = None

#    __slots__ = ["name", "year", "colour", "director", "main_actor", "main_actor2", "main_actor3"]

    def __init__(self, name="-", year="-", colour="-", director="-", main_actor="-", main_actor2="-", main_actor3="-"):
        """
        set attributes for Movies
        ...
        Attributes
        ----------
        name: str
            title of the movie
        year: int
            release year
        colour: str
            colour or black and white
        director: str
            director's name
        main_actor: str
            main actor's name
        main_actor2: str
            main actor's name
        main_actor3: str
            main actor's name
        """
        self.colour = colour
        self.name = name
        self.__year = year
        self.director = director
        self.main_actor = main_actor
        self.main_actor2 = main_actor2
        self.main_actor3 = main_actor3

    def func(self):
        """
        flick
        ...
        output referential info about the movie
        if there's no more than one main actor, print '-' instead of the names
        """
        return f'{self.__year}, {self.name}, {self.colour}, director: {self.director}, actors: {self.main_actor}, {self.main_actor2}, {self.main_actor3}'

    def __repr__(self):
        return f'{self.__year}, {self.name}, {self.colour}, director: {self.director}, actors: {self.main_actor}, {self.main_actor2}, {self.main_actor3}'

f1 = Movies('Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud')
f2 = Movies('Het verloren paradijs', 1978, 'colour', 'Harry Kümel', 'Hugo Van Den Berghe', 'Willeke van Ammelrooy')
f3 = Movies('La Haine', 1995, 'black&white', 'Mathieu Kassovitz', 'Vincent Cassel', 'Saïd Taghmaoui', 'Hubert Kounde')

if __name__ == "__main__":

    Movies.main_actor4 = "-"                                        #
    print(Movies.main_actor4)                                       # -
#    f4 = Movies('La Haine', 1995, 'black&white', 'Mathieu Kassovitz', 'Vincent Cassel', 'Saïd Taghmaoui', 'Hubert Kounde', 'bibi')
# TypeError
    f3.main_actor3 = 'H. Koundé'
    f3.__year = 2000
# 1995, La Haine, black&white, director: Mathieu Kassovitz, actors: Vincent Cassel, Saïd Taghmaoui, H. Koundé
    f3._Movies__year = 2000
# 2000, La Haine, black&white, director: Mathieu Kassovitz, actors: Vincent Cassel, Saïd Taghmaoui, H. Koundé
#    movie_copy = eval(repr(f3))
#    print(movie_copy)
    print(f3.func())
