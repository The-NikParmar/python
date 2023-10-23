# nested Dictionry

dx={
    'Name':"Nik",
    'fav_game':"football",
    'sub':"python"}

print(dx)

d1={
    'name':"nik",
    'fav_game':["football","cricket","hockey"],
    'sub':{'math':90,'sci':23,'py':23}
}


for k,v in dx.items():
    print(f'{k}={v}')


#access list as element from dict

print(d1['fav_game'][1])


#access dictionarty element from another dictionary
print(d1['sub']['sci'])
