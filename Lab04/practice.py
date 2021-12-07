def print_genres(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

genres = {
    "Боевик": 1,
    "Вестерн": 2,
    "Детектив": 3,
    "Драма": 4,
    "Комедия": 5,
    "Ужасы": 6,
}
print_genres(genres)