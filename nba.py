import urllib.request #needed to find requested data
from time import time #used to show speed of search
import re
import datetime #used to date each sqlite3 entry
import sqlite3 
url = "https://www.basketball-reference.com/players/" #url to site we are searching data for
print("Welcome to the JorTor NBA Player Stat Search Engine")
print(" ")
done = "" #this allows a while loop to exist
cheese = "I eat cheese" #needed a true statement for an elif to exist

#uses this class in order to save searched data in sqlite3
class NbaPlayer:
        def __init__(self, name, ppg, rebounds, assists, three, date):
            self.name = name
            self.ppg = ppg
            self.rebounds = rebounds
            self.assists = assists
            self.three = three
            self.date = date

#the loop basically contains all working parts, once loop is broken, the search is over
while done != "done":
    firstname = input("Enter Player's First Name: ")
    firstname = firstname.lower()
    twofirstname = firstname[0:2]
    lastname = input("Enter Player's Last Name: ")
    lastname = lastname.lower()
    onelastname = lastname[0:1]
    fivelastname = lastname[0:5]
    fullname = firstname.lower() + ' ' + lastname.lower()
    current_date = datetime.date.today()
    print(" ")
    if fullname == "isaiah thomas": #created because he has yet to play and yields no stats
        print("This player is injured and has not played this season.")
        print(" ")
        key = input("Type Done to exit, press Enter to continue searching: ")
        done = key.lower()
        print(" ")
    elif fullname == "kemba walker" or fullname == "anthony davis" or fullname == "jaren jacksonjr" or fullname == "larry nancejr": #all players that have 02 instead of 01 in url as they either share similar full names with another nba player, or are a jr
        before = time()
        print(" ")
        try:
            newurl = (url + onelastname + "/" + fivelastname + twofirstname + "02" + ".html") #in order to replicate needed url, I created this system that uses inputed first and last name to create valid url
            data = urllib.request.urlopen(newurl).read()
            data1 = data.decode('utf-8')
            a = re.search('data-tip="Points"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString1 = newString[29:33]
            newString1 = newString1.replace('<', '')
            print(
                firstname.upper() + ' ' + lastname.upper() + ' ' + "is currently averaging" +
                "\n" + str(newString1) + ' ' + "Points per Game,") #prints points per game
            a = re.search('data-tip="Total Rebounds"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString2 = newString[37:41]
            newString2 = newString2.replace('<', '')
            print(str(newString2) + ' ' + "Rebounds per Game,") #prints rebounds
            a = re.search('data-tip="Assists"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString3 = newString[30:34]
            newString3 = newString3.replace('<', '')
            print(str(newString3) + ' ' + "Assists per Game,") #prints assists
            a = re.search('data-tip="3-Point Field Goal Percentage"', data1)
            start = a.start()
            end = start + 70
            newString = data1[start:end]
            newString4 = newString[53:57]
            newString4 = newString4.replace('<', '')
            if newString4 == "-/p":
                newString4 = "0"
            print("Shooting" + ' ' + str(newString4) + '%' + ' ' + "from 3.") #prints three point percentage
            print(" ")
            after = time()
            speed = after - before
            speed1 = str(speed)
            speed2 = speed1[0:4]
            print('That took' + ' ' + speed2 + ' ' + "seconds to find.") # prints seconds it took in 0.00 fromat
            print(" ")

            import sqlite3

            conn = sqlite3.connect('statdata.db')
            c = conn.cursor()
            nba_name = fullname.upper()
            player = NbaPlayer(nba_name, newString1, newString2, newString3, newString4, current_date) #class defenition

            c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)', (player.name, player.ppg, player.rebounds, player.assists, player.three, player.date)) #sends data to sqlite3 precreated table

            conn.commit()
            
            conn.close()
            print("Data stored.")
            print(" ")
            helping = "nothelp"
            while helping != "help": #loop created to limit user input to just done, and Enter key
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print("")
        except:
            print(" ")
            print("Data already stored.") # if data has already been entered than sqlite3 will reject additional data with the same player name, hence the try won't complete sending it here (Note: it will send if stats change but as we have date sent with it date we can keep track of the most updated stats in sqlite3)
            print(" ")
            helping = "nothelp"
            while helping != "help":
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print("")       
    elif lastname == "osman": #made a custom for The Last Cedi because of an error by the website classifying him incorrectly in their generated url
        before = time()
        print(" ")
        try:
            newurl = (url + onelastname + "/" + fivelastname + "de" + "01" + ".html")
            data = urllib.request.urlopen(newurl).read()
            data1 = data.decode('utf-8')
            a = re.search('data-tip="Points"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString1 = newString[29:33]
            newString1 = newString1.replace('<', '')
            print(
                firstname.upper() + ' ' + lastname.upper() + ' ' + "is currently averaging" +
                "\n" + newString1 + ' ' + "Points per Game,")
            a = re.search('data-tip="Total Rebounds"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString2 = newString[37:41]
            newString2 = newString2.replace('<', '')
            print(newString2 + ' ' + "Rebounds per Game,")
            a = re.search('data-tip="Assists"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString3 = newString[30:34]
            newString3 = newString3.replace('<', '')
            print(newString3 + ' ' + "Assists per Game,")
            a = re.search('data-tip="3-Point Field Goal Percentage"', data1)
            start = a.start()
            end = start + 70
            newString = data1[start:end]
            newString4 = newString[53:57]
            newString4 = newString4.replace('<', '')
            if newString4 == "-/p":
                newString4 = "0"
            print("Shooting" + ' ' + newString4 + '%' + ' ' + "from 3.")
            print(" ")
            after = time()
            speed = after - before
            speed1 = str(speed)
            speed2 = speed1[0:4]
            print('That took' + ' ' + speed2 + ' ' + "seconds to find.")
            print(" ")
            
            import sqlite3

            conn = sqlite3.connect('statdata.db')
            c = conn.cursor()
            nba_name = fullname.upper()
            player = NbaPlayer(nba_name, newString1, newString2, newString3, newString4, current_date)

            c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)', (player.name, player.ppg, player.rebounds, player.assists, player.three, player.date))
            conn.commit()
            
            conn.close()
            print("Data stored.")
            print(" ")
            helping = "nothelp"
            while helping != "help":
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print("")
        except:
            print(" ")
            print("Data already stored.")
            print(" ")
            helping = "nothelp"
            while helping != "help":
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print(" ")
    elif lastname == "capela": #had to make another custom one for Clint Capela because of an error by the website classifying him incorrectly in their generated url
        before = time()
        print(" ")
        try:
            newurl = (url + onelastname + "/" + fivelastname + "ca" + "01" + ".html")
            data = urllib.request.urlopen(newurl).read()
            data1 = data.decode('utf-8')
            a = re.search('data-tip="Points"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString1 = newString[29:33]
            newString1 = newString1.replace('<', '')
            print(
                firstname.upper() + ' ' + lastname.upper() + ' ' + "is currently averaging" +
                "\n" + newString1 + ' ' + "Points per Game,")
            a = re.search('data-tip="Total Rebounds"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString2 = newString[37:41]
            newString2 = newString2.replace('<', '')
            print(newString2 + ' ' + "Rebounds per Game,")
            a = re.search('data-tip="Assists"', data1)
            start = a.start()
            end = start + 50
            newString = data1[start:end]
            newString3 = newString[30:34]
            newString3 = newString3.replace('<', '')
            print(newString3 + ' ' + "Assists per Game,")
            a = re.search('data-tip="3-Point Field Goal Percentage"', data1)
            start = a.start()
            end = start + 70
            newString = data1[start:end]
            newString4 = newString[53:57]
            newString4 = newString4.replace('<', '')
            if newString4 == "-/p":
                newString4 = "0"
            print("Shooting" + ' ' + newString4 + '%' + ' ' + "from 3.")
            print(" ")
            after = time()
            speed = after - before
            speed1 = str(speed)
            speed2 = speed1[0:4]
            print('That took' + ' ' + speed2 + ' ' + "seconds to find.")
            print(" ")
            
            import sqlite3

            conn = sqlite3.connect('statdata.db')
            c = conn.cursor()
            nba_name = fullname.upper()
            player = NbaPlayer(nba_name, newString1, newString2, newString3, newString4, current_date)

            c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)', (player.name, player.ppg, player.rebounds, player.assists, player.three, player.date))
            conn.commit()
            
            conn.close()
            print("Data stored.")
            print(" ")
            helping = "nothelp"
            while helping != "help":
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print("")
        except:
            print(" ")
            print("Data already stored.")
            print(" ")
            helping = "nothelp"
            while helping != "help":
                key = input("Type Done to exit, press Enter to continue searching: ")
                done = key.lower()
                if done == "done":
                    helping = "help"
                elif done == "":
                    helping = "help"
                else:
                    helping = "look at what I wrote"
            print(" ")
    elif cheese == "I eat cheese": #cheese allows elif to exist
        trying = "donttry"
        while trying != "try":
            retired = input("Is this player retired?(Yes/No): ") #because current players have their data in a seperate place on the website than current players do, i had to create two different "search engine" with different paramaters to search
            status = retired.lower()
            if status == "yes":
                trying = "try"
            elif status == "no":
                trying = "try"
            else:
                trying = "look at what I tried"
        print(" ")
        if status == "yes":
            try:
                before = time()
                bagel = "butter" # bagel will later be defined as "with butter" if a valid name is entered, while if a name that does not exist is entered, it will never reach the "with butter" and will be sent to except
                newurl = (url + onelastname + "/" + fivelastname + twofirstname + "01" + ".html")
                data = urllib.request.urlopen(newurl).read()
                data1 = data.decode('utf-8')
                a = re.search('data-tip="Points"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString1 = newString[37:41]
                newString1 = newString1.replace('<', '')
                print(
                    firstname.upper() + ' ' + lastname.upper() + ' ' + "averaged" +
                    "\n" + newString1 + ' ' + "Points per Game,")
                a = re.search('data-tip="Total Rebounds"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString2 = newString[45:49]
                newString2 = newString2.replace('<', '')
                print(newString2 + ' ' + "Rebounds per Game,")
                a = re.search('data-tip="Assists"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString3 = newString[38:42]
                newString3 = newString3.replace('<', '')
                print(newString3 + ' ' + "Assists per Game,")
                a = re.search('data-tip="3-Point Field Goal Percentage"', data1)
                start = a.start()
                end = start + 70
                newString = data1[start:end]
                newString4 = newString[61:65]
                newString4 = newString4.replace('<', '')
                if newString4 == "-/p":
                    newString4 = "0"
                print("Shooting" + ' ' + newString4 + '%' + ' ' + "from 3.")
                print(" ")
                after = time()
                speed = after - before
                speed1 = str(speed)
                speed2 = speed1[0:4]
                print('That took' + ' ' + speed2 + ' ' + "seconds to find.")
                print(" ")
                bagel = "with butter"
                
                import sqlite3

                conn = sqlite3.connect('statdata.db')
                c = conn.cursor()
                nba_name = fullname.upper()
                player = NbaPlayer(nba_name, newString1, newString2, newString3, newString4, current_date)

                c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)', (player.name, player.ppg, player.rebounds, player.assists, player.three, player.date))
                conn.commit()
                
                conn.close()
                print("Data stored.")
                print(" ")
                helping = "nothelp"
                while helping != "help":
                    key = input("Type Done to exit, press Enter to continue searching: ")
                    done = key.lower()
                    if done == "done":
                        helping = "help"
                    elif done == "":
                        helping = "help"
                    else:
                        helping = "look at what I wrote"
                    print(" ")
            except:
                if bagel == "with butter": # the second definition to make sure it is a valid player
                    print(" ")
                    print("Data already stored.")
                    print(" ")
                    helping = "nothelp"
                    while helping != "help":
                        key = input("Type Done to exit, press Enter to continue searching: ")
                        done = key.lower()
                        if done == "done":
                            helping = "help"
                        elif done == "":
                            helping = "help"
                        else:
                            helping = "look at what I wrote"
                        print(" ")
                else:
                    print(" ")
                    print("No player found")
                    print(" ")
                    helping = "nothelp"
                    while helping != "help":
                        key = input("Type Done to exit, press Enter to continue searching: ")
                        done = key.lower()
                        if done == "done":
                            helping = "help"
                        elif done == "":
                            helping = "help"
                        else:
                            helping = "look at what I wrote"
                        print(" ")
        elif status == "no": # for current nba players
            try:
                before = time()
                bagel = "butter"
                newurl = (url + onelastname + "/" + fivelastname + twofirstname + "01" + ".html")
                data = urllib.request.urlopen(newurl).read()
                data1 = data.decode('utf-8')
                a = re.search('data-tip="Points"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString1 = newString[29:33]
                newString1 = newString1.replace('<', '')
                print(
                    firstname.upper() + ' ' + lastname.upper() + ' ' + "is currently averaging" +
                    "\n" + newString1 + ' ' + "Points per Game,")
                a = re.search('data-tip="Total Rebounds"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString2 = newString[37:41]
                newString2 = newString2.replace('<', '')
                print(newString2 + ' ' + "Rebounds per Game,")
                a = re.search('data-tip="Assists"', data1)
                start = a.start()
                end = start + 50
                newString = data1[start:end]
                newString3 = newString[30:34]
                newString3 = newString3.replace('<', '')
                print(newString3 + ' ' + "Assists per Game,")
                a = re.search('data-tip="3-Point Field Goal Percentage"', data1)
                start = a.start()
                end = start + 70
                newString = data1[start:end]
                newString4 = newString[53:57]
                newString4 = newString4.replace('<', '')
                if newString4 == "-/p":
                    newString4 = "0"
                print("Shooting" + ' ' + newString4 + '%' + ' ' + "from 3.")
                print(" ")
                after = time()
                speed = after - before
                speed1 = str(speed)
                speed2 = speed1[0:4]
                print('That took' + ' ' + speed2 + ' ' + "seconds to find.")
                bagel = "with butter"
                print(" ")
                
                import sqlite3

                conn = sqlite3.connect('statdata.db')
                c = conn.cursor()
                nba_name = fullname.upper()
                player = NbaPlayer(nba_name, newString1, newString2, newString3, newString4, current_date)

                c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)', (player.name, player.ppg, player.rebounds, player.assists, player.three, player.date))
                conn.commit()
                
                conn.close()
                print("Data stored.")
                print(" ")
                helping = "nothelp"
                while helping != "help":
                    key = input("Type Done to exit, press Enter to continue searching: ")
                    done = key.lower()
                    if done == "done":
                        helping = "help"
                    elif done == "":
                        helping = "help"
                    else:
                        helping = "look at what I wrote"
                print("")
            except:
                if bagel == "with butter":
                    print(" ")
                    print("Data already stored.")
                    print(" ")
                    helping = "nothelp"
                    while helping != "help":
                        key = input("Type Done to exit, press Enter to continue searching: ")
                        done = key.lower()
                        if done == "done":
                            helping = "help"
                        elif done == "":
                            helping = "help"
                        else:
                            helping = "look at what I wrote"
                        print(" ")
                else: #sends all invalid names here
                    print(" ")
                    print("No player found")
                    print(" ")
                    helping = "nothelp"
                    while helping != "help":
                        key = input("Type Done to exit, press Enter to continue searching: ")
                        done = key.lower()
                        if done == "done":
                            helping = "help"
                        elif done == "":
                            helping = "help"
                        else:
                            helping = "look at what I wrote"
                        print(" ")
print("Thank you for using the JorTor NBA Player Stat Search Engine :)")