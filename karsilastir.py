followers=list()
followings=list()
takip_etmeyenler=list()
takip_edenler=list()
with open("followers.txt", "r", encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        followers.append(satır)
with open("followings.txt", "r", encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        followings.append(satır)
for i in followings:
    for x in followers:
        if i==x:
            takip_edenler.append(i)

follows=set(followers)
following=set(followings)

not_followers=following.difference(takip_edenler)

print(len(not_followers))

with open("takip_etmeyenler.txt", "w", encoding="utf-8") as file1:
    for i in not_followers:
        file1.write(i+"\n")
