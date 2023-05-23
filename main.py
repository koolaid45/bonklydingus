from discord_webhook import DiscordWebhook
import random
from time import sleep
from datetime import datetime, date


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
    today = str(date.today())
    now = datetime.now()
    hours = int(now.strftime("%H"))
    newhour = hours
    if hours>12:
        newhour=hours-12
        L = str(newhour)+"PM"
    else:
        newhour = hours
        L = str(newhour)+"AM"
    current_time = now.strftime(L+" | Minutes:%M | Seconds:%S | Date:"+today)
    g = str(random.choice(Begin) + random.choice(Mid) + random.choice(End1) + " " + random.choice(Begin) + random.choice(Mid) + random.choice(End2) + random.choice(bongus)+" -- "+ current_time)
    print(g)
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1077435895990452234/1Fm0Te2pRYZrU3gts_gr1rMPiPLZPI1uqtmZLggPw762XHg5Hl_Zd3FTo3-3L2srWrNx', content=g)
    response = webhook.execute()
    f = open("ohboy.log","a")
    f.write(g+"\n")
    f.close()
    sleep(1)