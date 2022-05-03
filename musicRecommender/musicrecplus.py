''' Group18
Created on 4/10/2022

@author:   Junhong Wu
           Songhan Yu          
	       Chenguang Wang     

Pledge:    I pledge my honor that I have adided by the Stevens Honor System.

CS515 - Group18 group project II
'''

PREF_FILE = 'musicrecplus.txt'

# ------------------ The Menu ------------------
def menu():  # Songhan Yu
    print('Enter a letter to choose an option:')
    print('e - Enter preference')
    print('r - Get recommendations')
    print('p - Show most popular artists')
    print('h - how popular is the most popular')
    print('m - Which user has the most likes')
    print('d - Delete preference')
    print('s - Show preference')
    print('q - Save and quit')
    userChoice = input()
    return userChoice

# ------------------ Functionality ------------------

def enterPreferences():  # This will replace the preferences already saved in the database under that user.
    '''User enters their preferences (artists they like) one at a time'''
    newPref = ''
    prefsLst = []
    newPref = input('Enter an artist that you like ( Enter to finish ):\n')
    while newPref != '':
        prefsLst.append(newPref.strip().title())
        newPref = input('Enter an artist that you like ( Enter to finish ):\n')
    prefsLst.sort()
    return prefsLst

def getRecommendations(currUser,prefs,userMap):  
    '''Get recommendations(Junhong Wu)'''
    bestUser = findClosestUser(currUser,prefs,userMap)
    if bestUser==None:
        return 0
    drop(prefs,userMap[bestUser])
    recommendations = drop(prefs,userMap[bestUser])
    return recommendations

def findClosestUser(currUser,prefs,userMap):
    '''Find the user whose preferences are closest to the current User. Return the best user's name'''
    bestUser=None
    bestScore=-1
    for user in userMap.keys():
        if(user.endswith("$")):
            continue
        else:
            socre=numMatches(prefs,userMap[user])
            if socre>bestScore and currUser != user and socre!=len(prefs):
                bestScore = socre
                bestUser = user
    return bestUser

def drop(list1,list2):
    '''Return a new list that contains only yhe elements in list2 that were Not in list1'''
    list3=[]
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i]==list2[j]:
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    while j<len(list2):
        list3.append(list2[j])
        j+=1
    return list3
def numMatches(list1, list2):
    '''return the number of elements that match between two sorted lists'''
    matches = 0 
    i=0
    j=0
    while i<len(list1) and j< len(list2):
        if list1[i] == list2[j].title():
            matches += 1
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
    return matches

def returnArtist(dic):
    '''Function help to get artists name and return as a list'''
    ArtList = []
    for Key in dic:
        if Key[-1] == '$':
            continue
        tempElem = dic[Key]
        for elemnt in tempElem:
            if tempElem.count(elemnt) == 1:
                ArtList.append(elemnt)
            elif tempElem.count(elemnt) > 1:
                ArtList.append(elemnt)
                tempElem = [i for i in tempElem if i != elemnt]
    return ArtList

def showMostPopularArtist(dic):  # Count word frequency. use a artistsDict
    '''Print the artists that are liked by the most users'''
    artistList = sorted(returnArtist(dic))
    if artistList == []:
        print("Sorry, no artist found")
    else:
        tempSet = []
        for elemnt in artistList:
            if elemnt not in tempSet:
                tempSet.append(elemnt)
        maxValue = artistList.count(tempSet[0])
        maxElemnt = tempSet[0]
        tempMulti = []
        for elemnt in tempSet:
            cont = artistList.count(elemnt)
            if cont > maxValue:
                maxValue = cont
                maxElemnt = elemnt
        for elemnt in tempSet:
            cont = artistList.count(elemnt)
            if maxValue == cont:
                tempMulti += [elemnt]
        if tempMulti != []:
            prin4line(sorted(tempMulti))
        else:
            print(maxElemnt)

def prin4line(i):
    '''prints out respective lines'''
    for x in i:
        print(x)

def howPopularIsTheMostPopularArtist(dic):  # print value of most popular artist in artistsDict
    '''Print the number of likes the most popular artist received'''
    artistList = sorted(returnArtist(dic))
    if artistList == []:
        print('Sorry, no artists found.')
    else:
        tempSet4how = []
        for elemnt in artistList:
            if elemnt not in tempSet4how:
                tempSet4how.append(elemnt)
        maxValue = artistList.count(tempSet4how[0])
        for elemnt in tempSet4how:
            cont = artistList.count(elemnt)
            if cont > maxValue:
                maxValue = cont
        print(maxValue)


def whichUserLikesTheMostArtists(dic):  # find all users who like the most artists 
    '''Print the full name(s) of the user(s) who like(s) the most artists'''
    flag= 0
    tempSet4User = []
    for Key in dic:
        if Key[-1] == '$':
            continue
        if len(dic[Key]) > flag:
            flag = len(dic[Key])
    for Key in dic:
        if Key[-1] == '$':
            continue
        if flag == len(dic[Key]):
            tempSet4User.append(Key)
    if tempSet4User != []:
        prin4line(sorted(tempSet4User))
    else:
        print("Sorry , no user found.")



def saveAndQuit(dic):
    '''user chooses to quit, the current database should be written to the musicrecplus.txt, replacing old contents (if any)'''
    finalNewContents = ''
    with open("musicrecplus.txt", "w") as f:
        for user in dic:
            finalNewContents += str(user) + ":" + ",".join(dic[user]) + "\n"

        f.write(finalNewContents)



# ------------------ Basics ------------------

def loadUsers(filename):
    ''' loadUsers preferences from database'''
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().title().split(":")
            singersList = singers.split(",")
            singersList.sort()
            dic[username] = singersList
    return dic


def saveUserPreference(username, prefs, dic, filename):
    '''save user's preference form database to file'''
    dic[username] = prefs  # a new preference that need to be added

    originalMap = loadUsers(filename)
    rewriteTxt = ''
    with open(filename, "w") as f:
        for user in dic:
            if user == username:
                if prefs == None:  # if user type in 'enter' directly, prefs == None. We have to handle this corner case.
                    dic[user] = originalMap[username]

            rewriteTxt += str(user) + ":" + ",".join(dic[user]) + "\n"

        f.write(rewriteTxt)


def getPreferences(username, dic):
    '''get user's preferences if new user input newpreferences, old user skip'''
    if username in dic:  # old user
        prefs = dic[username]
    else:
        # new user
        newPref = ''
        prefs = []
        newPref = input('Enter an artist that you like (Enter to finish):\n')
        while newPref != '':
            prefs.append(newPref.strip().title())
            newPref = input('Enter an artist that you like (Enter to finish):\n')
        prefs.sort()
    return prefs

def deletePreferences(prefs):
    '''delete preferences form user'''
    print("Prefs is", prefs)
    print('please enter the preferences you want to delete')
    deleteprefs=input().title()
    if deleteprefs in prefs:
        prefs.remove(deleteprefs)
        print('preferences has been delete')
    else:
        print("prefences not exist")
    return prefs

def showPreferences(prefs):
    '''show user's Preferences'''
    print("Prefs is", prefs)


    
def enterUsername(): 
    '''enter username'''
    print('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):')
    username = input().title()
    return username


def main():
    try:
        dic = loadUsers(PREF_FILE)
    except FileNotFoundError:
        f=open(PREF_FILE,'w')
        dic = loadUsers(PREF_FILE)
        f.close()
    username = enterUsername()

    prefs = getPreferences(username, dic)
    saveUserPreference(username, prefs, dic, PREF_FILE)

    userChoice = menu()
    while userChoice != 'q':
        if userChoice == 'e':
            newPrefs = enterPreferences()
            dic[username]=newPrefs
            saveUserPreference(username, newPrefs, dic, PREF_FILE)  # After the user finishes entering preferences, the database should be updated immediately so that the other functions proceed using the new preferences.
            userChoice = menu()  # After the user finishes entering preferences, they should be returned to the menu, which should be awaiting their next choice.
        elif userChoice == 'r':
            recs=getRecommendations(username, dic[username], dic)
            if recs==0:
                print("No recommendations available at this time .")
            else:
                for artist in recs:
                    print(artist)
            userChoice = menu()
        elif userChoice == 'p':
            showMostPopularArtist(dic)
            userChoice = menu()
        elif userChoice == 'h':
            howPopularIsTheMostPopularArtist(dic)
            userChoice = menu()
        elif userChoice == 'm':
            whichUserLikesTheMostArtists(dic)
            userChoice = menu()
        elif userChoice == 'd':
            prefs= deletePreferences(prefs)
            dic[username]=prefs
            userChoice = menu()
        elif userChoice == 's':
            prefs=dic[username]
            showPreferences(prefs)
            userChoice = menu()
        else:
            print("please input a correct user choice")
            userChoice = menu()

    saveAndQuit(dic)
    
main()



