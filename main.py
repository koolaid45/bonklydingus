
import random
from time import sleep


Begin1 = {"b","d","g","skr","sh","shl","chol"}
Mid1   = {"onk","ing","ink","oink","oing","ong","ung","unk"}
End11  = {"y","ly"}
End21  = {"us","lus","aloo"}
bongus = list({" is how its done", "is what we live for", " is whats going on", " is what we praise to", " overpowers everyone"})
Begin = list(Begin1)
Mid = list(Mid1)
End1 = list(End11)
End2 = list(End21)

while True:
    
    g = str(random.choice(Begin) + random.choice(Mid) + random.choice(End1) + " " + random.choice(Begin) + random.choice(Mid) + random.choice(End2) + random.choice(bongus))
    print(g)
    sleep(1)
