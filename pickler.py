#pickler.py
#Usage: $python3 pickler.py

#imports
from sys import stdin, stdout
from typing import IO, Tuple, Union, List
import pickle

option = 1

#convert data dump to dictionary for our use
def read_dump(filename) -> dictionary[str, list[str]]:
    return None

#save dictionary to disk so we don't have to read it every time
def save_to_disk(filename, data: dictionary[str, list[str]]) -> None:
    dbfile = open(filename, 'ab')
    pickle.dump(db, data)
    dbfile.close()

#load dictionary from disk
def load_from_disk(filename = "defaultdb.pkl") -> dictionary[str, list[str]]:
    dbfile = open(filename, 'rb')
    data = pickle.load(dbfile)
    dbfile.close()
    return data

#here we can convert a new file to dictionary,
if __name__ == "__main__":
    default_filename = "defaultdb.pkl"
    fn = "???"
    assert (option == 1 or option == 2), "invalid option; try 1 or 2.\n"

    #read in file to dictionary; pickle it
    if option == 1:
        data = read_dump(fn)
        save_to_disk(default_filename, data)

    #load in file from dictionary (this is for debugging)
    else: #if option == 2
        data = read_dump(default_filename)
        print(data)

    print("successfully executed option " + option + "!\n")