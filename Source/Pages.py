def stat_print(dictionary):
    ListKeyValuePair = []
    statblock = ""
    for key in dictionary.keys():
        if key == 'Race_Gender' or key =='Heritage Allowed':                                                            #Skips this info as is displayed else where
            pass
        else:
            TupleKeyValuePair = (key, dictionary[key])
            ListKeyValuePair.append(TupleKeyValuePair)
    x = 0
    y = 0
    spaces = 0
    while x <= len(ListKeyValuePair)-5:

        while y < 4:
            StringPartOne = str(ListKeyValuePair[x + y][0])                                                             #fuck if i know
            StringPartTwo = str(ListKeyValuePair[x + y][1])
            StringPartThree = StringPartOne + StringPartTwo
            if len(StringPartThree) > spaces:
                spaces = len(StringPartThree) + 4

            y += 1
        x += 4
        y = 0

    z = " "
    loss = ""
    x = 0
    y = 0
    kappa=4                                                                                                             #Kappa is number of items in line
    while x <= len(ListKeyValuePair):
        if x==(len(ListKeyValuePair)-(len(ListKeyValuePair)%4)):
            kappa =len(ListKeyValuePair)%4                                                                              #This kappa is number of items in last line
        while y < kappa:
            StringPartOne = str(ListKeyValuePair[x + y][0])
            StringPartTwo = str(ListKeyValuePair[x + y][1])
            StringPartThree = StringPartOne + StringPartTwo + ""
            tem = z
            if len(StringPartThree) < spaces:
                tem = z * (spaces - len(StringPartThree))
            StringPartThree = StringPartOne + tem + StringPartTwo + " "
            loss = (loss + StringPartThree)
            y += 1
        if x == 0:
           statblock = loss
        else:
           statblock = statblock + "\n\n" + loss

        loss = ""
        x += 4
        y = 0
    return statblock
def recurvespace(l,z):
    ll = l
    lisst = []
    x = 0
    a = 0
    s = z
    m = s
    z= False
    #print(round(len(l)/m))
    #print()
    while x <= (1 + round(int(len(ll) / m))):
        #print(s)
        #print(m)
        #print(x)
        if len(l) < m:
            #print("???")
            #s = len(l) - 1
            z= True
            lisst.append(l[0:len(l)])
            l = " "
            break
        if z== False and l[s] == " " :
            #print("!!")
            lisst.append(l[0:m])
            l = l[m:len(l)]
            x += 1
        elif z== False and l[s] != " ":
            #print(">"+str(s))
            try:
                while l[s + a] != " "and s==m:
                            a -= 1
                lisst.append(l[0:m + a + 1])
                l = l[m + a + 1:len(l)]
                a = 0
                x += 1
            except:
                print("Wrap length is too small")
                lisst=[]
                break
        #print()
    #print(int(len(ll) / m))
    #print(lisst)
    return lisst
def im(rr):
    cc=0
    ss=""
    while cc<27:
        if rr==cc:
            ss=f"C:\\Users\\silas\\PycharmProjects\\Arduin\\Images\\{cc}.png"
            break
        else:
            cc+=1
    return ss
def skills(dictionary):
#key =name
#value= list(advancement,modifier,rank,bonus,fmbl,crit,type,plateau)
#crit=(100-skillrank/10)
#fmbl=(11-skillrank/10)
#Power
    Cast=[0,dictionary['Reason'],0,0,11,100,'power','untrained']
    Channel=[0,0,0,0,11,100,'power','untrained']
    Entreaty=[0,dictionary['Essence'],0,0,11,100,'power','untrained']
    Mind=[0,dictionary['Ego'],0,0,11,100,'power','untrained']
#General
    Arcanalogy=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
#Knowledge
    Bionics=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Chemistry=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Clockwork=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Computers=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Explosives=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Glasswork=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Machining=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Material=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Science=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Miniaturization=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Physics=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Power_Sources=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Sensors=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Weapon_Smithing=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Meditation=[0,dictionary['Ego'],0,0,11,100,'General','untrained']
    Medical=[0,dictionary['Reason'],0,0,11,100,'General','untrained']
    Noetics=[0,dictionary['Ego'],0,0,11,100,'General','untrained']
    Recon=[0,dictionary['Wits'],0,0,11,100,'General','untrained']
    Self_Control=[0,dictionary['Ego'],0,0,11,100,'General','untrained']
    Wilderness=[0,dictionary['Wits'],0,0,11,100,'General','untrained']
#Interpersonal
    Beast_Ken=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
    Business=[0,dictionary['Wits'],0,0,11,100,'Interpersonal','untrained']
    Culture=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
    Gnosis=[0,dictionary['Essence'],0,0,11,100,'Interpersonal','untrained']
    Intel=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
    Military=[0,dictionary['Wits'],0,0,11,100,'Interpersonal','untrained']
    Perform=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
    Pneuma=[0,dictionary['Essence'],0,0,11,100,'Interpersonal','untrained']
    Social=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
    UnderWorld=[0,dictionary['Wits'],0,0,11,100,'Interpersonal','untrained']
    Urban=[0,dictionary['Charisma'],0,0,11,100,'Interpersonal','untrained']
#Maneuver
    Acrobatucs=[0,dictionary['Adroitness'],0,0,11,100,'Maneuver','untrained']
    Athletics=[0,dictionary['Strength'],0,0,11,100,'Maneuver','untrained']
    Clandestine=[0,dictionary['Reflexes'],0,0,11,100,'Maneuver','untrained']
    Combat=[0,dictionary['Wits'],0,0,11,100,'Maneuver','untrained']
    Crime=[0,dictionary['Reflexes'],0,0,11,100,'Maneuver','untrained']
    Gaurd=[0,dictionary['Reflexes'],0,0,11,100,'Maneuver','untrained']
    Lorica=[0,0,0,0,11,100,'Maneuver','untrained']
    Missilery=[0,dictionary['Adroitness'],0,0,11,100,'Maneuver','untrained']
    Pilot=[0,dictionary['Reflexes'],0,0,11,100,'Maneuver','untrained']
    Ride=[0,dictionary['Adroitness'],0,0,11,100,'Maneuver','untrained']
    Shield=[0,dictionary['Reflexes'],0,0,11,100,'Maneuver','untrained']
    Style=[0,0,0,0,11,100,'Maneuver','untrained']
    Weapon=[0,0,0,0,11,100,'Maneuver','untrained']
#Mechanical
    Ceremony=[0,dictionary['Essence'],0,0,11,100,'Mechanical','untrained']
    Engineering=[0,dictionary['Reason'],0,0,11,100,'Mechanical','untrained']
    Manufacture=[0,dictionary['Reason'],0,0,11,100,'Mechanical','untrained']
    Mechanic=[0,dictionary['Reflexes'],0,0,11,100,'Mechanical','untrained']

''' 
{dictionary['Adroitness']}
{dictionary['Reflexes']}
{dictionary['Strength']}
{dictionary['Siz']}
{dictionary['Mass'}
{dictionary['Constitution']}
{dictionary['Wits']}
{dictionary['Reason']}
{dictionary['Essence']}
{dictionary['Ego']}
{dictionary['Charisma']}
{dictionary['Fear']}
{dictionary['Shock']}
{dictionary['Disease']}
{dictionary['Poison']}
{dictionary['Damage Resistance']}
{dictionary['Magic Resistance']}
{dictionary['Psychic Resistance']}
{dictionary['Defense']}
{dictionary['Magic Defense']}
{dictionary['Psychic Defense']}
{dictionary['Recovery']}
{dictionary['Learning']}
{dictionary['Race_Gender']
{dictionary['Coordination'}
{dictionary['Count Factor']
{dictionary['Mental Acuity'}
{dictionary['Body'}
{dictionary['Aptitude'}
{dictionary['Leadership'}
{dictionary['Perception'}
{dictionary['Move'}
{dictionary['Dodge'}
{dictionary['Running Jump'}
{dictionary['High Jump'}
{dictionary['Broad Jump'}
{dictionary['Climb'}
{dictionary['Swim'}
{dictionary['Health'}
'''
