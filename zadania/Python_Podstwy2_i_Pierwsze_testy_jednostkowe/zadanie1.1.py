def print_dict(d):
    for key in d:
        print("{0}:{1}".format(key.replace("name","nazwa"), d[key]))


if __name__ == "__main__":
    samolot = {'name': 'boeing',
               'przebieg': 1000,
               'type': 'pasazerski'}
    print_dict(samolot)
