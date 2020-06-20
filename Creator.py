#started 2/1/2019 version 3.6.1

from tkinter import *
from tkinter import font
from re import *
from Source import Race_Querry,Pages

                                                        #### Functions
## Grid init Main Menu
def mainmenu():
    frameMain2.grid_forget()
    root.geometry("%sx%s+%s+%s" % (w,h,wid, hei))
    frameMain.grid()                                                                                                    # grid actually makes the things know where to show up
    shardra_pht.grid(sticky=N,columnspan=1)
    create.grid(row=1,pady=15)
    total_Random.grid(row=2,column=0,pady=15)
    close.grid(row=3,pady=15)

## Gender
def gend():
    global gender
    gender=gen.get()
    clrprint(None)
## Grid pg1
def pg1():
    global racialchoicen
    wid=int((root.winfo_screenwidth() / 6))
    hei=int((root.winfo_screenheight() / 2)-(1045/2))
    root.geometry("1270x1030+%s+%s" % (wid, hei))
    frameMain.grid_forget()
    frameMain3.grid_forget()
    frameMain2.grid()
    frameMain2.grid_propagate(0)
    character_pht.grid(row=0,column=0,pady=11)
    races.grid(row=1,column=0,pady=0,padx=5,rowspan=5)
    back.grid(row=6, column=0,pady=0,padx=5)
    forward.grid(row=6,column=5,columnspan=3, pady=10,padx=5,sticky=E)
    genderF.grid(row=1,column=1,pady=15,padx=10)
    genderM.grid(row=1,column=2,pady=15,padx=10)
    racesinfo_pht.grid(row=2,column=1,pady=0,padx=5,columnspan=5,rowspan=3)
    racesinfo_pht.grid_propagate()
    stats.grid(row=0,column=1,pady=5,padx=10,rowspan=3,columnspan=5,sticky=N)
    racialchoicen=0
    racechoice_number.config(text="Racial Points to Spend: %s" % (dictionary["Racial Points"][0] + racialchoicen))



## Stats clear and print
def pg2():
    global racialchoicex
    wid=int((root.winfo_screenwidth() / 6)-(1400/12))
    hei=int((root.winfo_screenheight() / 2) -90-(h/2))
    root.geometry("1400x1032+%s+%s" % (wid, hei))
    frameMain2.grid_forget()
    frameMain4.grid_forget()
    frameMain3.grid()
    frameMain3.grid_propagate(0)
    racechoice_g.grid(row=1,column=2,padx=4,pady=2,rowspan=5,sticky=E)
    racechoice_r.grid(row=1, column=0, padx=4, pady=2, rowspan=5, sticky=W)
    race_text_g.grid(row=0, column=2, padx=4, pady=4, rowspan =1,sticky=E)
    race_text_r.grid(row=0, column=0, padx=4, pady=4, rowspan =1,sticky=W)
    racechoice_text.grid(row=1, column=1, padx=4, pady=5, rowspan=5)
    racechoice_text.config(text="")
    back2.grid(row=6, column=0, pady=0,columnspan=1, padx=5,sticky=W)
    racechoice_number.grid(row=6, column=1, columnspan=1, padx=5,sticky=N)
    racechoice_cost.grid(row=0, column=1, columnspan=1,rowspan =2, pady=2, padx=5, sticky=N)
    forward2.grid(row=6, column=2, pady=10, padx=5,sticky=E)
    racialchoicex = 1
    racechoice_cost.config(text="Racial Choice Points to purchase: %s" % racialchoicex)
    #x=0
    #while x <len(dictionarychoices['lastclick']['curTwo']):
        #racechoice_g.activate(list(dictionarychoices['lastclick']['curTwo'])[x])
        #x+=1

    racechoice_g.delete(0, 100)

    dictionarychoices['lastclick']={'curOne': set(), 'curTwo': set(), 'lastOne': set(), 'lastTwo': set()}
    for key in dictionaryRacial[0]:
        if dictionaryRacial[0][key][2]==-1:
            racechoice_g.insert(END,str(key))
    try:
        racechoice_r.delete(0,90)
        count = 1
        for key in dictionaryRacial[0]:
            #print (key)
            if (races.curselection()[0] + 1) == dictionaryRacial[0][key][2]:
                racechoice_r.insert(count,str(key))
                count+=1
                #print(dictionaryRacial[0][key])
            elif key == "Undefined" and count ==1:
                racechoice_r.insert(count, str(key))

    except:
        racechoice_r.insert(1, str("Undefined"))
        #print(dictionaryRacial[0]["Undefined"])

def pg3():
    wid = int((root.winfo_screenwidth() / 6) - (1400 / 12))
    hei = int((root.winfo_screenheight() / 2) - 90 - (h / 2))
    root.geometry("1400x1032+%s+%s" % (wid, hei))
    frameMain3.grid_forget()
    frameMain4.grid()
    frameMain4.grid_propagate(0)
    back3.grid(row=6, column=0, pady=0, columnspan=1, padx=5, sticky=W)
    forward3.grid(row=6, column=1, pady=10, padx=5, sticky=E)
    Culturechoice.grid(row=0, column=0, padx=4, pady=2, rowspan=5, sticky=W)
    Culturechoicetext.grid(row=1, column=1, padx=4, pady=5, rowspan=5)
    Culturechoicetext.config(text="                                                                                                                                                                                                                                                                                                                                                                               ")
    for key in dictionaryRacial[1]:
        Culturechoice.insert(END,str(key))

def pg4():
    pass

def culture(event,self,count):

                                                                                                                        # Used below code to write all info to files
    #cultureAlText=open("C:\\Users\\silas\\PycharmProjects\\Arduin\\Text\\Cultures\\1CultureAll.txt","a")
    #cultureAlText.write(self.get(self.curselection()) + Race_Querry.raceBlurbs(dictionaryRacial[count][self.get(self.curselection())][5],210)[0])
    #cultureAlText.write("\n\n")
    #nameFile = self.get(self.curselection())
    #f = open(f"C:\\Users\\silas\\PycharmProjects\\Arduin\\Text\\Cultures\\{nameFile}.txt", "x")
    #f.write(self.get(self.curselection()) + Race_Querry.raceBlurbs(dictionaryRacial[count][self.get(self.curselection())][5], 210)[0])

    Culturechoicetext.config(text=(self.get(self.curselection()) + Race_Querry.raceBlurbs(dictionaryRacial[count][self.get(self.curselection())][5],210)[0]))
def choiceselection(event,self):
    global racialchoicex
    global racialchoicen
    global dictionarychoices
    global dictionary
    selection=self.curselection()
    racechoice_text.config(text=" ")

    #if type(selection) != type((1,)):      #May be useless
    #    selection = (selection,)
    #else:
    #    pass

    if self==racechoice_g:
        dictionarychoices['lastclick']['lastTwo']=dictionarychoices['lastclick']['curTwo']
        dictionarychoices['lastclick']['curTwo']=set(selection)
        last_set = dictionarychoices['lastclick']['lastTwo']
        current_set=dictionarychoices['lastclick']['curTwo']=set(selection)
    else:
        dictionarychoices['lastclick']['lastOne'] = dictionarychoices['lastclick']['curOne']
        dictionarychoices['lastclick']['curOne'] = set(selection)
        last_set = dictionarychoices['lastclick']['lastOne']
        current_set = dictionarychoices['lastclick']['curOne'] = set(selection)

    if len(current_set) > len(last_set):
        racechoice_text.config(text=self.get(list(current_set-last_set)[0])+":"+ "\n"+ \
                                    Race_Querry.raceBlurbs(dictionaryRacial[0][self.get\
                                        (list(current_set-last_set)[0])][3],145)[0])
        racialchoicex = dictionaryRacial[0][self.get(list(current_set - last_set)[0])][0]
        racialchoicen= racialchoicen-dictionaryRacial[0][self.get(list(current_set - last_set)[0])][0]
    elif len(current_set) < len(last_set):
        racechoice_text.config(text=self.get(list(last_set-current_set)[0])+":"+"\n"+ \
                                    Race_Querry.raceBlurbs(dictionaryRacial[0][self.get\
                                        (list(last_set-current_set)[0])][3],145)[0])
        racialchoicex = dictionaryRacial[0][self.get(list(last_set-current_set)[0])][0]
        racialchoicen = racialchoicen + dictionaryRacial[0][self.get(list(last_set-current_set)[0])][0]

    racechoice_cost.config(text="Racial Choice Points to purchase: %s" %racialchoicex)
    racechoice_number.config(text="Racial Points to Spend: %s" % (dictionary["Racial Points"][0]+racialchoicen))

def clrprint(event):                                                                                                    # Clears text on window page
    global dictionary
    global dictionarychoices
    global racialchoicen
    if races.curselection()==():
        pass
    else:
        stats['state'] = NORMAL
        stats.delete(1.0,20.120)
        dictionary=Race_Querry.race_stats((races.curselection()[0] + 1),gender)
        stats.insert(END,Pages.stat_print(dictionary))
        racesinfo.config(file=Pages.im(races.curselection()[0] + 1))
        stats['state'] =DISABLED

        dictionarychoices["race"]=(races.curselection()[0] + 1)
        dictionarychoices["specific racial"]= []
        dictionarychoices["general racial"]=[]
        dictionarychoices['lastclick']={'curOne':set(),'curTwo':set(),'lastOne':set(),'lastTwo':set()}
        race_text_r.config(text="%s Racial Choices" %dictionary["Race_Gender"][0])
        racechoice_number.config(text= "Racial Points to Spend: %s" %dictionary["Racial Points"][0])


                                                    #### Root Configuration and declerations

                                                                                                                        # creates initial window component
root = Tk()
root.title ("Arduin Character Creator")                                                                                 # Changes name of window
root.resizable(0,0)                                                                                                     # makes it so user can't change size
w = 454
h = 892
race_name ="undefined"
gender = 0
gen = IntVar()
gen.set(1)
racialchoicen=0
racialchoicex=1
dictionarychoices={'race':0,'specific racial':[],'general racial':[],'lastclick': {'curOne':set(),'curTwo':set(),'lastOne':set(),'lastTwo':set()}}
dictionaryRacial=[Race_Querry.race_choice(),Race_Querry.culture()]
dictionary=(Race_Querry.race_stats(0,gender))
hei = int((root.winfo_screenheight() / 2) -((h/2)+25))                                                                  # gets height of screen
wid = int((root.winfo_screenwidth() / 2)-(w/2))                                                                         # gets width of screen
                                                                                    # sets initial screen size and loc
#root.rowconfigure('all', minsize=10)                                                                                   # configures all rows
#root.columnconfigure('all', minsize=10)                                                                                # configures all columns



                                                        #### Font
annoying = font.Font(family="old english text MT", size=15)                                                             # old english font for menu
notannoying = font.Font(family="times",size=16,weight="bold")
equal = font=('TkFixedFont', 16)

                                                        #### MainMenu
frameMain = Frame(root, relief=RIDGE, width=400, height=900, bd=5,bg="black")                                           # main menu screen

## Widgets
                                                                                                                        # three buttons on main menu
create=Button(frameMain,text="Enter The Realm Prepared",bg="cyan",font=annoying,\
              command=pg1,relief=RAISED,bd=4)
total_Random= Button(frameMain, text ="Not All Who Wander Are Lost",bg="yellow",\
                     font=annoying,relief=RAISED,bd=4)
close = Button(frameMain, text ="You're Only Mortal After All",command=root.quit,bg="red",\
               font=annoying,relief=RAISED,bd=4)

## Photo
shardra = PhotoImage(file="C:\\Users\\silas\\PycharmProjects\\Arduin\\Images\\Shardra.png")
shardra_pht = Label(frameMain, height=650, width=440,image=shardra,anchor=N)                                            # shirtless lady pic cause lore?




                                                        #### Page 1
frameMain2 = Frame(root, relief=RIDGE, width=1270, height=1030,bg="black",bd=5)                                         # Races Page


## Widgets
stats=Text(frameMain2,height=19,width=120,bg="#efe2a0",relief=RIDGE,bd=5)
stats.insert(END,Pages.stat_print(dictionary))
stats['state'] = DISABLED      # makes text field non editable


back=Button(frameMain2,text="BACK YOU FOOLS",font=notannoying,command=mainmenu,width=20)
forward=Button(frameMain2,text="Next step",font=notannoying,width=10,command=pg2)
genderM=Radiobutton(frameMain2,text="Male",variable=gen, value=1,command=gend,bg="#efe2a0",relief=RIDGE,bd=2)
genderF=Radiobutton(frameMain2,text="Female",variable=gen,value=2,command=gend,bg="#efe2a0",relief=RIDGE,bd=2)

races=Listbox(frameMain2,font=notannoying,relief=RIDGE,selectmode=SINGLE,width=22,height=26,cursor="heart",\
              selectbackground="goldenrod",bg="#efe2a0",bd=2,exportselection=False)
count=1
while count <27:
    races.insert(count,(Race_Querry.race_stats(count,0)["Race_Gender"][0]))
    count+=1
races.bind('<ButtonRelease-1>', clrprint)                                                                               ### Event to trigger command


                                                        ###Page 2
frameMain3=Frame(root,relief=RIDGE, width=1400, height=1032,bg="black",bd=5)
back2=Button(frameMain3,text="Previous step",font=notannoying,command=pg1,width=20)
forward2=Button(frameMain3,text="Next step",font=notannoying,width=10,command=pg3)
racechoice_g=Listbox(frameMain3,relief=RIDGE,selectmode=MULTIPLE,width=40,height=58,\
              selectbackground="goldenrod",bg="#efe2a0",bd=2,exportselection=False)
racechoice_r=Listbox(frameMain3,relief=RIDGE,selectmode=MULTIPLE,width=40,height=58,\
              selectbackground="goldenrod",bg="#efe2a0",bd=2,exportselection=False)
racechoice_text=Label(frameMain3,width=123,height=58, relief=RIDGE,text="",justify=LEFT,anchor=N)
race_text_r=Label(frameMain3,width=34,height=1, relief=RIDGE,text="%s Racial Choices" %dictionary["Race_Gender"][0])
race_text_g=Label(frameMain3,width=34,height=1, relief=RIDGE,text="General Racial Choices")
racechoice_number=Label(frameMain3,relief=RIDGE,width=30,height=2,font=notannoying,\
    text=("Racial Choice Points Available: %s" %racialchoicen))
racechoice_cost=Label(frameMain3,relief=RIDGE,width=30,height=2,font=notannoying,\
    text=("Racial Choice Points to purchase: %s" %racialchoicex))

racechoice_r.bind('<ButtonRelease-1>',lambda event:choiceselection(event,racechoice_r))
racechoice_g.bind('<ButtonRelease-1>',lambda event:choiceselection(event,racechoice_g))


                                                        ###Page 3
frameMain4=Frame(root,relief=RIDGE, width=1400, height=1032,bg="black",bd=5)
back3=Button(frameMain4,text="Previous step",font=notannoying,command=pg2,width=20)
forward3=Button(frameMain4,text="Next step",font=notannoying,width=10,command=pg4)
Culturechoice=Listbox(frameMain4,relief=RIDGE,selectmode=SINGLE,width=40,height=58,\
              selectbackground="goldenrod",bg="#efe2a0",bd=2,exportselection=False)
Culturechoicetext=Label(frameMain4,height=60, relief=RIDGE,justify=LEFT,anchor=N)

## Photo
                                                                                                                        # never winter nights photo

character = PhotoImage(file="C:\\Users\\silas\\PycharmProjects\\Arduin\\Images\\nvn.png")
character_pht=Label(frameMain2,height=278,width=237,relief=RIDGE,bd=5,image=character)
racesinfo = PhotoImage(file="C:\\Users\\silas\\PycharmProjects\\Arduin\\Images\\Capture.png")
racesinfo_pht=Label(frameMain2,height=594,width=844,relief=RIDGE,bd=3,image=racesinfo)

Culturechoice.bind('<ButtonRelease-1>',lambda event:culture(event,Culturechoice,1))


                                                        #### Gui Start
                                                                                                                        # starts the gui

mainmenu()
root.mainloop()

#print(root.winfo_height())