#pwparser.py: matches user data in dump to user data we already have
#Usage: $python3 pwparser.py

#imports
from sys import stdin, stdout
from typing import IO, Tuple, Union, List, Dict
from pickler import load_from_disk
import nltk                     #$pip3 install nltk

#global data
dump_dict = {}                  #username to associated password list
dump_dict_reverse = {}          #password to associated username list
un_results = []                 #list of passwords
pw_results = []                 #list of usernames
option_o = False                #output filename specified
option_d = False                #dictionary filename specified
#option_ld = False              #Levenshtein distance limit specified
given_dictionary_filename = ""; #dictionary to read from
given_output_filename = ""      #name of file to write to
given_pswd = ""                 #password to search on
given_usnm = ""                 #username to search on

def load_input() -> None:
    global option_d, option_o, given_pswd, given_usnm, given_dictionary_filename, given_output_filename
    option_d = True
    option_o = False
    if option_d:
        given_dictionary_filename = "example-passwords.txt"
    if option_o:
        given_output_filename = "my_output.txt"
    given_usnm = "kevin@123.net"
    given_pswd = "password1"

#TODO
#a: arg dictionary
def load_input_2(a: Dict[str, str]) -> None:
    global option_d, option_o, given_pswd, given_usnm, given_dictionary_filename, given_output_filename
    option_d = False
    option_o = False
    #'-o' Option
    if '-o' in a:
        option_o = True
        given_output_filename = a['-o']
    elif '--output' in 'a':
        option_o = True
        given_output_filename = a['--output']

    #'d' Option
    if '-d' in a:
        option_d = True
        given_dictionary_filename = a['-d']
    elif '--database' in a:
        option_d = True
        given_dictionary_filename = a['--database']

#if the user gives us a filename, we'll want to read that one
def parse_file(sin: IO[str]) -> None:
    for s in sin:
        e, p = read_line(s)
        dump_dict[e] = p
        dump_dict_reverse[p] = e

#otherwise, we'll want to pull from our default lists, 
#   which are dd.pickle & dd-reverse.pickle
def load_default() -> None:
    global dump_dict, dump_dict_reverse
    dump_dict = load_from_disk("database.pkl")
    dump_dict_reverse = load_from_disk("reverse_database.pkl")

#parse a single line of the given file
def read_line(s: str) -> Tuple[str, str]:
    a = s.split()
    return str(a[0]), str(a[1])

#search by username
def search_by_username(usnm: str) -> List[str]:
    if usnm in dump_dict:
        return dump_dict[usnm]
    else:
        print("usnm not in dd")
        return None

#search by password; match similar strings with Levenshtein distance
def search_by_password(pswd: str) -> List[str]:
    if pswd in dump_dict_reverse:
        return dump_dict_reverse[pswd]
    else:
        print("pswd not in ddr")
        return None
 

#write the results of our search to a file
#sout: IO stream we should print to
def write_results(sout: IO[str]) -> None:
    #username
    if given_usnm == "":
        sout.write("No email provided.\n")
    else:
        sout.write("A search on the victim's email address \"" + given_usnm + 
                    "\" returned these results:\n" + str(un_results) + "\n")
        
    #password
    if given_pswd == "":
        sout.write("No password provided.\n")
    else:
        sout.write("A search on the victim's password \"" + given_pswd + 
                    "\" returned these results:\n" + str(pw_results) +"\n")

#essentially our main function; outputs to txt file with specified name
def search(a: Dict[str, str], c: Tuple[str, str]) -> None:
    global given_usnm, given_pswd, output_filename, un_results, pw_results
    #handle user input
    load_input_2(a)
    given_usnm = c[0]
    given_pswd = c[1]

    #handle -d option; decide what we're searching
    if option_d:
        reader = open(given_dictionary_filename, "r")
        parse_file(reader) #need to convert it to IO stream
    else:
        #assert False, "load_default is now handled elsewhere. Names probably aren't lining up!\n"
        print("hit load_default()")
        load_default()

    #handle -o option; where to output
    output_filename = ""
    if option_o:
        output_filename = given_output_filename
    else:
        assert False, "default output is now handled elsewhere.\n"
        output_filename = "output.txt"

    #heavy lifting
    print("searching u, p: " + given_usnm + ", " + given_pswd + "\n")
    un_results = search_by_username(given_usnm)
    pw_results = search_by_password(given_pswd)
    writer = open(output_filename, "w+")
    write_results(writer)
    writer.close()

#main function
if __name__ == "__main__":
    args = {"-o": "my_o"}
    search(args, ['rylen4@juno.com', 'maddog'])