def draw_stars(arr):
    star_array = [4, 6, 1, 3, 5, 7, 25]
    for index in star_array:
        print index * '*'
        

draw_stars([4, 6, 1, 3, 5, 7, 25])


def draw_stars_dos(arr):
    new_array = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for index in new_array:
        if type(index) == int:
            print index * '*'
        if type(index) == str:
            new_str = len(index) * index[:1]
            print new_str.lower()

draw_stars_dos([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

