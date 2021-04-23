import os

#make more stuff configurable later
commandsFile = "hotspot_setup_commands.txt"
#commandsFile = "test.txt"

def performSetup() -> bool:
    #read in shell commands to execute
    f = open(commandsFile, "r")
    commandsToRun = [line.rstrip() for line in f]
    f.close()

    print(commandsToRun)

    for command in commandsToRun:
        successRequired = True
        if(command[0] == "#"):
            successRequired = False
            command = command[1:]
        output = os.system(command)
        print(command, output)
        if successRequired and output != 0:
            print("A command was unsuccessful, edit the command file and try running this again!")
            return False
    
    print("The hotspot was successfully set up and configured to redirect to your Apache2 website!")
    return True

if __name__ == "__main__":
    performSetup()

