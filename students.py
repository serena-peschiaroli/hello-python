students = {
    "Giuseppe Gullo" : [("Matematica", 9, 0),
                        ("Italiano", 7, 3),
                        ("Inglese", 7.5, 4),
                        ("Storia", 7.5, 4),
                        ("Geografia", 5, 7)],
    "Antonio Barbera" : [("Matematica", 8, 1),
                        ("Italiano", 6, 1),
                        ("Inglese", 9.5, 0),
                        ("Storia", 8, 2),
                        ("Geografia", 8, 0)],
    "Emiliano Ruozzo" : [("Matematica", 7.5, 2),
                        ("Italiano", 6, 2),
                        ("Inglese", 4, 3),
                        ("Storia", 8.5, 2),
                        ("Geografia", 8, 7)],
}

##aggiungere un nuovo record

students["Albert Einstein"] = [
    ("Matematica",10, 0),
    ("Italiano", 10, 0),
    ("Inglese", 10, 0),
    ("Storia", 10, 0),
    ("Geografia", 10,0)
    
]

print(students)

##aggiungere una nuova materia

students["Giuseppe Gullo"].append("Fisica", 9.5, 0)
students["Antonio Barbera"].append("Fisica", 8, 1)
students["Emiliano Ruozzo"].append("Fisica", 8, 3)
students["Albert Einstein"].append("Fisica", 10, 0)


##stampa le info di un solo studente

print(students["Giuseppe Gullo"][0])

print(students["Emiliano Ruozzo"][2])

##stampa solo il voto di Antonio Barbera in geografia

print(students["Antonio Barbera"][4][1])