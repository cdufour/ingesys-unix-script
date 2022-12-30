#raise Exception("blabla")

def check(x):
    if x < 0:
        #print("négatif")
        raise Exception("Negative number forbidden")

try:
    check(4)
except:
    print("Problème")

print("*** The End ***")