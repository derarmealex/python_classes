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
    def __init__(self, name, year, colour, director, main_actor, main_actor2='-', main_actor3='-'):
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
        self.year = year
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
        return f'{self.year}, {self.name}, {self.colour}, director: {self.director}, actors: {self.main_actor}, {self.main_actor2}, {self.main_actor3}'

f1 = Movies('Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud')
f2 = Movies('Het verloren paradijs', 1978, 'colour', 'Harry Kümel', 'Hugo Van Den Berghe', 'Willeke van Ammelrooy')
f3 = Movies('La Haine', 1995, 'black&white', 'Mathieu Kassovitz', 'Vincent Cassel', 'Saïd Taghmaoui', 'Hubert Kounde')

if __name__ == "__main__":
    #print(Movies.__doc__)                                            # film library...
    #help(Movies)                                                     # film library...
    #print(func.__doc__)                                              # NameError
    #print(f2.director)
    #print(f3.colour)
    #print(f2.main_actor3)
    #print(f2.main_actor2)
    #print(Movies)
    #print(Movies('year', 'c', 'director', 'main_actor', 'name'))
    #print(f3.main_actor3)
    f3.main_actor3 = 'Hubert Koundé'
    #del f3.main_actor3
    #del f3
    print(f3.func())
    print(Movies.func(f3))
    #print(f1.func())
    #print(dir(f1))
    #print(f3.colour)
    #print(dir(Movies))
    print(type(f1))
