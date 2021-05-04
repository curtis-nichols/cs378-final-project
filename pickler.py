#pickler.py
#Usage: $python3 pickler.py

#imports
from sys import stdin, stdout
from typing import IO, Tuple, Union, List, Dict
import pickle

#parse a single line of the given file
#s is the line
#c is the char to split on
def read_line(s: str, c: str) -> Tuple[str, str]:
    a = s.replace(';',' ').replace(':',' ').split()
    out1 = str(a[0])
    out2 = ""
    if len(a) > 1:
        out2 = str(a[1])
    out2 = out2.rstrip("\n")

    return str(out1), str(out2)

#convert data dump to dictionary for our use
def read_dump(filename) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    out1 = {}
    out2 = {}
    reader = open(filename, 'r')
    for line in reader:
        un, pw = read_line(line, ";") #username, password
        if un not in out1:
            out1[un] = [pw]
        else:
            out1[un].append(pw)
        if pw not in out2:
            out2[pw] = [un]
        else:
            out2[pw].append(un)

    return out1,out2

#save dictionary to disk so we don't have to read it every time
def save_to_disk(db: Dict[str, List[str]], filename:str = "database.pkl") -> None:
    dbfile = open(filename, 'ab')
    pickle.dump(db, dbfile)
    dbfile.close()

#load dictionary from disk
def load_from_disk(filename:str = "database.pkl") -> Dict[str, List[str]]:
    dbfile = open(filename, 'rb')
    db = pickle.load(dbfile)
    dbfile.close()
    return db

#here we can convert a new file to dictionary,
if __name__ == "__main__":
    default_filename = "database.pkl"
    fn = "???"
    option = 3
    assert (option == 1 or option == 2 or option == 3), "invalid option; try 1 or 2.\n"

    #read in file to dictionary; pickle it
    if option == 1:
        db1, db2 = read_dump("datadump.txt")
        save_to_disk(db1, default_filename)
        save_to_disk(db2, "reverse_"+default_filename)

    elif option == 3:
        data1 = load_from_disk(default_filename)
        data2 = load_from_disk("reverse_" + default_filename)
        max_us = 0
        max_ps = 0
        curr_us = 0
        curr_ps = 0
        most_ps_un = ""
        most_us_pw = ""
        for u in data1:
            pwlist = data1[u]
            if pwlist != None:
                curr_ps = len(pwlist)
                if curr_ps > max_ps and u != "":
                    max_ps = curr_ps
                    most_ps_un = u
        for p in data2:
            unlist = data2[p]
            if unlist != None:
                curr_us = len(unlist)
                if curr_us > max_us and p != "":
                    max_us = curr_us
                    most_us_pw = p
        
        print("Username with most passwords was \"" + most_ps_un + "\" with " + str(len(data1[most_ps_un])) + " passwords: " + str(data1[most_ps_un]))
        print("Password with most usernames was \"" + most_us_pw + "\" with " + str(len(data2[most_us_pw])) + " usernames: " + str(data2[most_us_pw]))


    #load in file from dictionary (this is for debugging)
    else: #if option == 2
        data1 = load_from_disk(default_filename)
        data2 = load_from_disk("reverse_" + default_filename)
        #print(data1)
        #print(data2)

    print("successfully executed option " + str(option) + "!\n")