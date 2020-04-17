print('BEGIN TRANSACTION;')
rl = [
    'kogtrey',
    'VaccaFlacca',
    'MrBlueSky-729',
    'Klover'
    ]
apex = []
over = []
lol = [
    'Ulfrrr',
    'Rusk',
    'Shhy',
    'DiscoPotato99',
    'VegiKarp',
    'Jet Jaguar',
    'Maurtek',
    'Colz',
    'S3PH4R',
    'Archer66',
    'WishXII',
    'Dayze',
    'MoonMoonn',
    'Hefae',
    'Goes',
    'BearlyTwiggs',
    'Crashthehalls',
    'Cheeto11',
    'ClydeFrawwg',
    'Slop'
    ]
id = 1
for i in range(len(rl)):
    print("INSERT INTO \"eSports_user_game\" VALUES (" + str(id) + ",'" + rl[i] + "',1,NULL,NULL);")
    id = id + 1

for i in range(len(apex)):
    print("INSERT INTO \"eSports_user_game\" VALUES (" + str(id) + ",'" + apex[i] + "',2,NULL,NULL);")
    id = id + 1

for i in range(len(over)):
    print("INSERT INTO \"eSports_user_game\" VALUES (" + str(id) + ",'" + over[i] + "',3,NULL,NULL);")
    id = id + 1

for i in range(len(lol)):
    print("INSERT INTO \"eSports_user_game\" VALUES (" + str(id) + ",'" + lol[i] + "',4,NULL,NULL);")
    id = id + 1

print('COMMIT;')
