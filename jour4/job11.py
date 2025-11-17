def time_to_text(minute) :
    if type(minute) == int :
        if minute > 60 :
            nbr_heure = minute // 60
            nbr_minute = minute % 60
            print(f"{nbr_heure} heure(s) et {nbr_minute} minute(s)")
        else :
            print(f"{minute} minute(s)")
    else :
        print("Le nombre entré n'est pas valide")

time_to_text(150)
time_to_text(60)
time_to_text(120)
time_to_text(47)
time_to_text(1342)