def bmi_calc():
    height = float(input("Podaj wzrost w cm: ")) / 100
    weight = float(input("Podaj wage: "))
    score = weight / (height * height)
    if score < 18.5:
        print("Masz niedowage !")
    elif 18.5 <= score <= 24.99:
        print("Wynik prawidlowy :)")
    elif 25 <= score <= 29.99:
        print("Masz otylosc I stopnia !")
    elif 30 <= score <= 34.99:
        print("Masz otylosc II stopnia !")
    elif score >= 40:
        print("Masz otylosc III stopnia ( Olbrzymia ) !")

    print(score)


bmi_calc()
