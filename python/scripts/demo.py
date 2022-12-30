from time import sleep

while True:
    f = open("files/toto.log", "a")
    f.write("dodo\n")
    f.close
    sleep(2)
    

