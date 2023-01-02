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


