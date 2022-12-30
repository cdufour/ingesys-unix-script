try:
    print("toto")
    [1,2,3][6]
except NameError:
    print("Problème de nom")
# except IndexError:
#     print("Problème d'index")
except:
    print("Erreur")

#print(toto)
#[1,2,3][6]