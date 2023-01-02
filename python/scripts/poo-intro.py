class Student:
    # propriétés
    first_name = ""
    last_name = ""

    # propriété privée (private)
    __age = 0

    # méthodes (fonction dans une classe)
    def test(self):
        print("test")

    # accesseurs (getters)
    def get_age(self):
        return self.__age

    def get_first_name(self):
        return self.first_name

    # mutateurs (setters)
    def set_age(self, age):
        self.__age = age


# instanciation
s1 = Student()
s2 = Student()
#print(type(s1))

s1.first_name = "Toto" # accès en écriture
print(s1.first_name)
print(s1.get_first_name())
print(s2.first_name)

# invocation d'une méthode à partir d'un objet
s1.test()
s2.test()

#print(s1.age)
print(s1.get_age())

s1.set_age(18)
print(s1.get_age())

s2.set_age(99)
print(s2.get_age())

print("\n---------------------------------------------\n")

class Vehicle:
    __num_wheels = 0
    __max_speed = 100

    # méthodes
    # constructeurs
    def __init__(self, num_wheels, max_speed=100):
        #print("Hello from constructor method !")
        self.__num_wheels = num_wheels
        self.__max_speed = max_speed

    def get_num_wheels(self):
        return self.__num_wheels

    def get_max_speed(self):
        return self.__max_speed


v1 = Vehicle(2, 90)
v2 = Vehicle(4, 180)

print(v1.get_num_wheels())
print("Vitesse max du véhicule v1:", v1.get_max_speed())
print("Vitesse max du véhicule v2:", v2.get_max_speed())

