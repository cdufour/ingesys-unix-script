fruits = ["poire", "pomme", "banane", "kiwi", "mangue"]
newList = [x for x in fruits if "a" in x]

print(newList)

def square(n):
    return n*n

numbers = [6,4,40,10,8,15]
squares = [square(n) for n in numbers if n >= 10]
print(squares)


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

students = [student1, student2, student3]

goodStudents = [s for s in students if s["isGoodLearner"]]
print(goodStudents)