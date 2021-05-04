#pwparser.py: matches user data in dump to user data we already have
#Usage: $python3 pwparser.py

#imports
from sys import stdin, stdout
from typing import IO, Tuple, Union, List, Dict
from pickler import load_from_disk

#global data
dump_dict = {}                  #username to associated password list
dump_dict_reverse = {}          #password to associated username list
un_results = []                 #list of passwords
pw_results = []                 #list of usernames
option_o = False                #output filename specified
option_d = False                #dictionary filename specified
given_dictionary_filename = ""; #dictionary to read from
given_output_filename = ""      #name of file to write to
given_pswd = ""                 #password to search on
given_usnm = ""                 #username to search on

#TODO
#a: arg dictionary
def load_input(a: Dict[str, str]) -> None:
    global option_d, option_o, given_pswd, given_usnm, given_dictionary_filename, given_output_filename
    option_d = False
    option_o = False
    #'-o' Option
    if '-o' in a:
        option_o = True
        given_output_filename = a['-o'] + "_result.txt"
    elif '--output' in a:
        option_o = True
        given_output_filename = a['--output'] + "_result.txt"

    #'d' Option
    if '-d' in a:
        option_d = True
        given_dictionary_filename = a['-d']
    elif '--database' in a:
        option_d = True
        given_dictionary_filename = a['--database']

#if the user gives us a filename, we'll want to read that one
def parse_file(sin: IO[str]) -> None:
    print("loading given database...")
    for s in sin:
        e, p = read_line(s)
        dump_dict[e] = p
        dump_dict_reverse[p] = e

#otherwise, we'll want to pull from our default lists, 
#   which are database.pkl & reverse_database.pkl
def load_default() -> None:
    #print("loading default database...")
    global dump_dict, dump_dict_reverse
    dump_dict = load_from_disk("database.pkl")
    dump_dict_reverse = load_from_disk("reverse_database.pkl")

#parse a single line of the given file
def read_line(s: str) -> Tuple[str, str]:
    a = s.split()
    return str(a[0]), str(a[1])

#search by username
def search_by_username(usnm: str) -> List[str]:
    print("searching username...")
    if usnm in dump_dict:
        return dump_dict[usnm]
    else:
        return None

#search by password; match similar strings with Levenshtein distance
def search_by_password(pswd: str) -> List[str]:
    print("searching password...")
    if pswd in dump_dict_reverse:
        return dump_dict_reverse[pswd]
    else:
        return None
 

#write the results of our search to a file
#sout: IO stream we should print to
def write_results(sout: IO[str]) -> None:
    #username
    if given_usnm == "":
        sout.write("No email provided.\n")
    elif un_results == None or len(un_results) == 0:
        sout.write("A search on the victim's username \"" + given_usnm + "\"returned no results.\n")
    else:
        sout.write("A search on the victim's username \"" + given_usnm + 
                    "\" returned these possibly linked passwords:\n" + str(un_results) + "\n")
        
    #password
    if given_pswd == "":
        sout.write("No password provided.\n")
    elif pw_results == None or len(pw_results) == 0:
        sout.write("A search on the victim's password \"" + given_pswd + "\"returned no results.\n")
    else:
        sout.write("A search on the victim's password \"" + given_pswd + 
                    "\" returned these possibly linked usernames:\n" + str(pw_results) +"\n")

#read email address and password from file filename
def read_cp_output_lines(filename: str) -> List[str]:
    reader = open(filename, 'r')
    return reader

#essentially our main function; outputs to txt file with specified name
def search(a: Dict[str, str], c: Tuple[str, str]) -> None:
    global given_usnm, given_pswd, output_filename, un_results, pw_results
    #handle user input
    load_input(a)
    given_usnm = c[0]
    given_pswd = c[1]

    #handle -d option; decide what we're searching
    if option_d:
        reader = open(given_dictionary_filename, "r")
        parse_file(reader) #need to convert it to IO stream
    else:
        load_default()

    #handle -o option; where to output
    output_filename = ""
    if option_o:
        output_filename = given_output_filename
    else:
        assert False, "default output is now handled elsewhere.\n"
        output_filename = "output.txt"

    #heavy lifting
    un_results = search_by_username(given_usnm)
    pw_results = search_by_password(given_pswd)
    writer = open(output_filename, "a+")
    write_results(writer)
    writer.close()
    print("current search complete.")

#main function
if __name__ == "__main__":
    args = {"-o": "my_o"}
    #for testing, change the example username and password below
    # search(args, ['willow0007@juno.com', 'maddog'])
    users = read_cp_output_lines("example-in.txt")
    for user in users:
        info = user.split()
        print("considering user, password pair: " + info[1] + ", " + info[2])
        search(args, [info[1],info[2]])