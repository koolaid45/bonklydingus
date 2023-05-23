
import random
from time import sleep
bongus = list({" is how its done", "is what we live for", " is whats going on", " is what we praise to", " overpowers everyone"})
Begin = list({"b","d","g","skr","sh","shl","chol"})
Mid = list({"onk","ing","ink","oink","oing","ong","ung","unk"})
End1 = list({"y","ly"})
End2 = list({"us","lus","aloo"})
while True:
    g = str(random.choice(Begin) + random.choice(Mid) + random.choice(End1) + " " + random.choice(Begin) + random.choice(Mid) + random.choice(End2) + random.choice(bongus))
    print(g)
    sleep(1)
