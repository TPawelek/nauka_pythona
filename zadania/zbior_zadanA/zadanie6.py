def is_plindrome():
    first_word = input('Wpisz slowo: ').lower()

    second_word = first_word[::-1]
    if first_word == second_word:
        print("Podane slowo jest palindromem.")
    else:
        print("Podane slowo nie jest palindromem.")


is_plindrome()
