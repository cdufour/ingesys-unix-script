d = {}
print(type(d)) # dict

student1 = {
    "age": 25,
    "lname": "PASCAL",
    "fname": "Blaise",
    "isGoodLearner": True,
    "grades": [17, 12, 19.5]
}

student2 = {
    "age": 36,
    "lname": "DEL PIERO",
    "fname": "Alessandro",
    "isGoodLearner": False,
    "grades": [10, 10, 10]
}

student3 = {
    "age": 58,
    "lname": "TOURGE",
    "fname": "Ivan",
    "isGoodLearner": True,
    "grades": [19, 7.5, 2.5]
}

# Affichage de la première note obtenue par student1
print(student1["grades"][0])

# Itération sur les clés d'un dictionnaire
for k in student1:
    print(k, "=>", student1[k])

# Liste de dict
students = [student1, student2, student3]

evaluation = "bon"
for s in students:
    if not s["isGoodLearner"]:
        evaluation = "mauvais"
    else:
        evaluation = "bon"

    print("%s est un %s étudiant" % (s["fname"], evaluation))